import pandas as pd

df = pd.read_csv("weighted_score_above_08.csv")
new_df = df[(df["language"]=="english") & (df["game"]=="Stardew Valley")]
new_df.to_csv('cleaned_data.csv', index=False)