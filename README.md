## How to build and run the code
Run "make install" in the terminal. This will run the Makefile, creating a folder for the virtual environment, installing dependencies from requirements.txt, and register the virtual environment as a Jupyter kernel named "Python (venv)". If running on VS code, open the notebook. In the top right, select "Python (venv)". Then, run the notebook as desired. If you are using our pretrained BERT model, simply run the code blocks until you create the documents and labels, then go down to the code block which loads the model.

If the makefile does not work, try the following steps:
1. (optional) Create a virtual environement
Run "python -m venv venv" in the VS code terminal

2. (optional) Activate the environment
Mac: source .venv/bin/activate
Windows Powershell: . .venv\Scripts\Activate.ps1


3. Install dependencies
Run "pip install -r requirements.txt"

4. Register environment for notebook use
Run "pip install ipykernel"
Run "python -m ipykernel install --user --name=venv --display-name "Python (.venv)""

## How to replicate BERT results
Simply download one of the datasets from Kaggle at the link in the data section. Put the data in the directory, then run the cleaned.py file to get the cleaned data with only english records. We recommend trying the dataset with weighted scores above 0.8 as it is already quite large and our cleaned.py file is hardcoded to accept a file with the same name as this dataset. We also offer a subset of the data "cleaned_data.csv" which removes the need to run this file. Note that this was not the data we tested with but a small subset of 10 records. Then, run blocks 1-16 of main.ipynb, which preprocesses the data and creates a BERT model. If you downloaded our pretrained model below, run blocks 1-15 and then run block 18 (which loads the model). Code blocks 19-22 can be run to evaluate the model afterwards.

The yaml file in our code should automatically run the notebook after each push. However, using our pretrained model does not require running all blocks.

## Steam Review Sentiment Analysis
Link to Midterm Youtube Video: https://youtu.be/9W7UCZSQ-lc
Link to Final Youtube Video: [youtube.com/watch?v=GRjRmayWeyo](https://www.youtube.com/watch?v=GRjRmayWeyo)

## Description
Steam is an online marketplace where consumers can purchase digital commodities, primarily video game keys. One distinct characteristic of Steam is its review system, where users can choose to recommend or not recommend a game they have played to other prospective buyers. The goal of this project is to conduct sentiment analysis on steam reviews to see how they might predict game review positivity.

## Goals
This project aims to analyze specific features in the description of a game review (e.g. certain keywords like "good story" or "great graphics") and how they affect the positivity of a review. 

## Data
We used the following dataset from Kaggle: https://www.kaggle.com/datasets/kieranpoc/steam-reviews/data. The dataset contains records for individual reviews, as well as key features for these reviews such as what game they reviewed and a steam generated helpfulness score. We will primarily focus on the content of the user review.

## Feature Vectorization
By making use of models such as Bag of words, TF-IDF, and Latent Semantic Analysis, we can turn the contents of each review into meaningful features for our models. Bag of words and TF-IDF represent two different methods of measuring vocabulary frequency across documents. Via LSA, it becomes possible to computationally reason about the semantics of particular words. LSA creates a low rank approximation of the data that allows similar words to be captured.

Bag of words and LSA did not work well with our Naive Bayes model (see modeling), and as a result we did not do any further work with them. In theory, Bag of Words might be more sensitive to the length of the document (and therefore the presence of unique vocabulary) and common words such as “the” or “is” might dominate probability calculations in naive Bayesian models. TF-IDF addresses these issues by downweighting common words and normalizing by document length. The reasoning behind LSA’s poor performance is that features become correlated as a result of dimensionality reduction. Theoretically, this violates the assumptions of conditional independence that Naive Bayesian models are built on.

Between the midterm and the final, we tried implementing VADER along with both the bag of words and TF-IDF feature matrices. However, VADER provided no significant increases in performance at a high computational cost. Lastly, our BERT model used a base BERT tokenizer that considered the text uncased.

## Modeling
We pre-processed the data by first filtering out English reviews only to limit the size of our data and chose the game PAYDAY 2 to be our focus. We then represented our data using TF-IDF to capture word frequencies and importance, respectively. After that, we created a Naive Bayes classifier to model our data. We chose Naive Bayes to be the best approach since it assigns probabilities to words and allows us to find the best features or words that people say are good about the game. However, we recognize that since most of the PAYDAY 2 reviews contains mostly positive reviews, the accuracy may not be representative of the data.

By the end of the project, we had expanded to all english reviews regardless of game with a weighted helpfulness score above 0.8. Still, this amounted to hundreds of thousands of records. Some new models we tried included linear regression, logistic regression, and BERT. BERT performed by far the best, with a testing set accuracy and f-1 score of 0.938 and 0.967 respectively.

## Visualization
We used word clouds, scatter charts and bar charts to visualize the frequencies of certain key phrases that appeared in the data. As for the word clouds, we created a dictionary that mapped words to their importance using TF-IDF. We filtered out function words (i.e "the", "and", "an", etc.) and have two word cloud models: one that visualizes general words and one that focuses only on adjectives. In conjuction with the word cloud models, we also include bar charts to highlight the importance of the top 20 features.

Here is a bar chart displaying the top words most informative to the Naive Bayes classifier, showing the highest contributors to predicting recommended (green) and not recommended (red) reviews. Many of these words reflect PAYDAY 2-specific vocabulary and known platform sentiments.
<div style="display: flex; justify-content: space-around;">
    <img src="assets/topN.png" alt="Word Cloud with all words (besides function words) for PAYDAY 2" width="100%">
</div>
<br>

Here's the word cloud and bar charts for top "general" words found in reviews of PAYDAY 2. 
<div style="display: flex; justify-content: space-around;">
    <img src="assets/payday2_all_wordcloud.png" alt="Word Cloud with all words (besides function words) for PAYDAY 2" width="45%">
    <img src="assets/Payday2_allwords_bar.png" alt="Corresponding bar chart of Top 20 words" width="45%">
</div>
<br>

Here's the word cloud and bar charts for top adjectives found in those same reviews of PAYDAY 2. 
<div style="display: flex; justify-content: space-around;">
    <img src="assets/payday2_adj.png" alt="Word Cloud with top adjectives for PAYDAY 2" width="45%">
    <img src="assets/payday2_adj_bar.png" alt="Corresponding bar chart of Top 20 words" width="45%">
</div>
<br>

We used bar charts and a scatterplot to compare the length of the review and whether or not the review was "Voted Up" or "Voted Down" (in other words, whether or not it was a positive review).
<div style="display: flex; justify-content: space-around;">
    <img src="assets/median_rev_len_vs_vote_status.png" alt="Bar chart comparing median review length with the review's vote status." width="45%">
    <img src="assets/scatter.png" alt="Scatterplot comparing median review length with the review's vote status." width="45%">
</div>
<br>

We used a 2D and 3D t-SNE visualization of the reviews, which shows that recommended and not recommended reviews do not form distinct clusters, suggesting sentiment is distributed subtly rather than forming separable groups.
<div style="display: flex; justify-content: space-around;">
    <img src="assets/2dSNE.png" alt="Bar chart comparing median review length with the review's vote status." width="45%">
    <img src="assets/3dSNE.png" alt="Scatterplot comparing median review length with the review's vote status." width="45%">
</div>
<br>

After creating a BERT model, we analyzed the attention heads of the model, telling us the relationships between words that the model keys in on for given sample sentences. Below is an example of a sample negative review, where the model appears to do well identifying some low level semantic relationships between the words. For example, there exist strong attention heads between the words "hard to recommend" and "not a fan" (although the strength is overshadowed by the attention heads to the line separator that comes later). There are other times when the model isn't quite sure how to handle the language, as in the latter picture. For example, "text art" can be common among steam reviews. When faced with text art, the uniform symbols are quite difficult for the model to identify key relationships, instead opting to generally create attention heads with tokens close in proximity.
<div style="display: flex; justify-content: space-around;">
    <img src="assets/layer_7_sample_sentence.jpg" alt="layer 7 sample sentence" width="45%">
    <img src="assets/review_art.jpg" alt="review art" width="45%">
</div>
<br>

Here is a classification matrix of the BERT model on a random sample of 10000 reviews (the classification matrix took extremely long to load) and some performance metrics. Unfortunately, it seems that the model does not handle negative reviews very well. That is, there are many false positives in the confusion matrix and the model appears to guess that the review is positive almost all of the time. There may be some room for optimism, as the testing accuracy on the whole testing set and f1-score were 0.938 and 0.967 respectively.
<div style="display: flex; justify-content: space-around;">
    <img src="assets/bert_confusion_matrix.jpg" alt="confusion matrix" width="45%">
</div>
<br>



## Test Plan
We plan on randomly selecting 20% of the records from the Kaggle dataset for testing and 80% of the records for training.
In the future, we plan on choosing alternative models that account for multiple words, word order and grammatical choices.

##  Google Colab link:
https://colab.research.google.com/drive/13i5jrVx0f_AFSONIkNkGbxOgZwippBAg?usp=sharing

## Link to pretrained model:
https://drive.google.com/file/d/1Uat70L-x_utodAIRKzGQFxvv-u9JlcRD/view?usp=sharing 
