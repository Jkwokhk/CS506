# CS506

Steam Review Sentiment Analysis

Description
Steam is an online marketplace where consumers can purchase digital commodities, primarily video game keys. One distinct characteristic of Steam is its review system, where users can choose to recommend or not recommend a game they have played to other prospective buyers. The goal of this project is to conduct sentiment analysis on steam reviews to see how they might predict player counts.

Goals
This project aims to analyze how game reviews (sentiment) impact player retention rates and identify key factors that contribute to high or low player retention. By combining Natural Language Processing (NLP) with statistical analysis and machine learning, we can discover insights that help game developers improve engagement.

Data
We plan on using the following dataset from Kaggle: https://www.kaggle.com/datasets/kieranpoc/steam-reviews/data. The dataset contains records for inidividual reviews, as well as key features for these reviews such as what game they reviewed and a steam generated helpfulness score. We also plan on using the Steam API to measure playercounts over time.

Modeling
We plan on using multi-layer perceptron which works on a "bag of words" model that tests for the appearance of certain key words after removing irrelevant language such as "the" or "are." By combining this bag of words with other key features in the dataset such as whether the reviewer recommended the game, we can determine what features are important to player retention by attempting to predict player counts themselves. PCA might also be particularly useful in conducting dimensionality reduction.

Visualization
Due to the high dimensionality of our data, we plan on using scatter plots to model relationships between 2 features and T-SNE plots for aggregated data views. For natural language predictors, we plan on using a heat map to show the most important language for determining player retention. We plan on using bar charts to visualize the frequencies of certain key phrases.

Test Plan
We plan on randomly selecting 20% of the records from the Kaggle dataset for testing and 80% of the records for training.
