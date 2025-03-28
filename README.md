# CS506

## Steam Review Sentiment Analysis

## Description
Steam is an online marketplace where consumers can purchase digital commodities, primarily video game keys. One distinct characteristic of Steam is its review system, where users can choose to recommend or not recommend a game they have played to other prospective buyers. The goal of this project is to conduct sentiment analysis on steam reviews to see how they might predict game review positivity.

## Goals
This project aims to analyze specific features in the description of a game review (e.g. certain keywords like "good story" or "great graphics") and how they affect the positivity of a review. 

## Data
We plan on using the following dataset from Kaggle: https://www.kaggle.com/datasets/kieranpoc/steam-reviews/data. The dataset contains records for individual reviews, as well as key features for these reviews such as what game they reviewed and a steam generated helpfulness score. We also plan on using the Steam API to measure playercounts over time. We will primarily focus on the content of the user review.

## Modeling
We plan on using multi-layer perceptron which works on a "bag of words" model that tests for the appearance of certain key words after removing irrelevant language such as "the" or "are." By combining this bag of words with other key features in the dataset such as whether the reviewer recommended the game, we can determine what features are important to review positivity by attempting to cluster natural language. PCA might also be particularly useful in conducting dimensionality reduction. We will also plan on categorizing games and their respective reviews by genre in order to conduct a more meaningful analysis.

## Visualization
Due to the high dimensionality of our data, we plan on using scatter plots to model relationships between 2 features and T-SNE plots for aggregated data views. For natural language predictors, we plan on using a heat map to show the most important language for review positivity. We plan on using bar charts to visualize the frequencies of certain key phrases.

## Test Plan
We plan on randomly selecting 20% of the records from the Kaggle dataset for testing and 80% of the records for training.

##Google Colab link:
https://colab.research.google.com/drive/13i5jrVx0f_AFSONIkNkGbxOgZwippBAg?usp=sharing
