import requests
import pandas as pd
import time
import random
import os

# Load dataset
file_path = "updated_dataset_with_genres.csv"  # File where progress is saved
if os.path.exists(file_path):
    df = pd.read_csv(file_path)  # Resume from saved file
else:
    df = pd.read_csv("./processed_reviews.csv")  # Start fresh (this included only the english reviews)
    df["genres"] = ""  # Add an empty genres column if not present

total_rows = len(df)  # Total number of rows
start_time = time.time()  # Track script start time

# Headers to mimic a real browser request
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
]

def get_headers():
    return {"User-Agent": random.choice(USER_AGENTS)}

# Dictionary to store fetched genres 
genre_cache = {}

# Dynamic sleep time 
sleep_time = 1.0
max_retries = 5

# Function to get genres from Steam API
def get_game_genres(appid):
    global sleep_time  # Modify sleep time dynamically

    if appid in genre_cache:
        return genre_cache[appid]  # Use cached value

    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"

    for attempt in range(max_retries):  # Retry up to max_retries times
        try:
            response = requests.get(url, headers=get_headers(), timeout=5)

            if response.status_code == 429:
                print(f"429 Too Many Requests for {appid}. Sleeping {sleep_time:.2f}s")
                time.sleep(sleep_time)
                sleep_time *= 1.5  # Increase sleep time 
                continue  # Retry request

            response.raise_for_status()  # Raise other HTTP errors

            data = response.json()
            if str(appid) in data and data[str(appid)]["success"]:
                genres = data[str(appid)]["data"].get("genres", [])
                genre_list = ", ".join(genre["description"] for genre in genres)
                genre_cache[appid] = genre_list  # Store in cache
                sleep_time = max(0.5, sleep_time * 0.9)  # Decrease sleep time slightly if successful
                return genre_list

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {appid}: {e}. Retrying in {2 ** attempt} seconds...")
            time.sleep(2 ** attempt)  # Exponential backoff

    genre_cache[appid] = "Unknown"
    return "Unknown"

# Sequentially process only missing rows
for index, row in df.iterrows():
    if not isinstance(row["genres"], str) or row["genres"] == "":  # Check if genre is missing
        df.at[index, "genres"] = get_game_genres(row["appid"])

        # Sleep to prevent rate-limiting 
        time.sleep(sleep_time)

        # Save progress every 100 rows
        if index % 100 == 0 or index == total_rows - 1:
            df.to_csv(file_path, index=False)
            elapsed_time = time.time() - start_time
            percent_done = (index + 1) / total_rows * 100
            est_total_time = (elapsed_time / (index + 1)) * total_rows
            est_time_remaining = est_total_time - elapsed_time
            print(f"Processed {index + 1}/{total_rows} rows ({percent_done:.2f}%)")
            print(f"Elapsed Time: {elapsed_time:.2f}s | Estimated Time Remaining: {est_time_remaining:.2f}s")
            print(f"✅ Progress saved to {file_path}")

# Final save
df.to_csv(file_path, index=False)
print("✅ Genres successfully added!")