# Anti-East and Southeast Asian sentiment in the UK during the COVID-19 pandemic: Twitter sentiment analysis using SVM machine learning and VADER

## Abstract

**Background:** In the UK reports of hate crimes against East and Southeast Asians rose by 300% after the COVID-19 pandemic began. There was an increase of 1662% in Asian-targeted hate speech online in 2020 compared to 2019 (Cipirska, 2021). However, no UK-specific research into changes in sentiment towards East and Southeast Asians over the pandemic has yet been carried out. When investigating optimum preprocessing techniques for Support Vector Machine (SVM) sentiment analysis, I found that the results from  the research are often contradictory. 
**First Research Question:** “To what extent has UK-based sentiment on Twitter towards East and Southeast Asia and Asians changed over the COVID-19 pandemic?”. 
**Second Research Question:** “What are the optimum preprocessing techniques for carrying out SVM-powered sentiment analysis on Twitter data?”. 
**Methods:** I carried out experimentation using the sentiment140 dataset to produce results on the optimum preprocessing techniques for sentiment analysis with SVM. Using the Twitter API, I collected 448,802 tweets that used one keyword related to East and Southeast Asia posted in the UK between January 2019 and June 2022. Making use of the results from the preprocessing experimentation, I first carried out sentiment analysis using an SVM (LinearSVC) classifier (with an F1-score of 0.82). I then carried out sentiment analysis using the rule-based classifier VADER. 
**Results:** Through preprocessing experimentation I found that stop word removal, short word removal, and lemmatization negatively impact classification performance. Several other techniques were shown not to improve performance but could be useful for noise reduction. Sentiment analysis powered by SVM and VADER both demonstrated a peak of negative sentiment in March 2020. Comparing this month with March 2019 SVM results show the proportion of negative tweets referencing an East and Southeast Asian keyword increased by 66.8%, and VADER results show an increase of 60.6%. 
**Conclusion:** UK-based negative sentiment towards East and Southeast Asians increased online as the COVID-19 pandemic developed.   My results show that stop word removal, short word removal, and lemmatization negatively affected SVM-powered classifier performance. Other techniques tested did not improve performance, but I conclude that they are useful for noise reduction, in line with the opinions of other researchers. Those techniques include: lowercasing; removal of user mentions, URLs, non-alphabet characters, and unnecessary whitespace; the translation of HTML symbols, emojis, and abbreviations; expanding contractions; and normalising repeated characters.

## Keywords for search query:
a combination of East and South East Asian countries and nationalities and racial slurs for Asian people.
Racial slurs taken from a public online database of racial slurs.
Full list can be seen in **'rawkeywordlist.csv'**.

In **'asianKeywordOrderedBySum.ipynb'** Keywords are extracted from csv and placed in order of relevance (most used to least used) by examining each word's use in January 2019 and January 2020.
Any keyword that was used 0 times in both months is removed (twitter's search query is limited to 1024 characters).
Final keyword list found in **'finalAsianKeywords'**.

## Tweet Counts

In **'tweetCountsAsianKeywords.ipnb'** a query is created using the finalAsianKeywords to search for tweets coming from the UK from January 2019 to June 2022.
Knowing how many tweets would be returned by the query was useful to understand how long it would take to return all matching tweets.

## Collecting data

In **'tweetScrape.ipnb'** I collect matching tweets using the keyword list, over the period Jan 2019 - June 2020.
Tweets are saved in **'twitterDataOutput.csv'**.
Nearly 500,000 matching tweets were collected.

## SVM preprocessing Experiemntation

In **sentimentAnalysisSVMExperimentation.ipynb** I experiment with different preprocessing techniques using SVM (LinearSVC) classifiers trained on sentiment140 dataset. The models' performances are assessed based on their F1-score. Having found the best preprocessing techniques I carry out hyperparameter tuning.

## Sentiment Analaysis Using SVM

In **sentimentAnalysisSVM.LinearSVC.ipynb** I use the preprocessing techniques and hyperparameter tuning results uncovered in experimentation to create a classifier (trained on sentiment140) and carry out sentiment analysis on the twitter dataset.

![SVM sentiment analysis](https://github.com/ORJackson/CSCM20_Project/blob/main/images/Updated%20graphs/SVM%20positive%20and%20negative.png)
![SVM proportion of negative tweets by week](https://github.com/ORJackson/CSCM20_Project/blob/main/images/Updated%20graphs/SVM%20neg%20week.png)

## Sentiment Analysis using VADER

In **sentimentAnalysisVADER.ipynb** I carry out sentiment analysis using VADER.


![VADER sentiment analysis](https://github.com/ORJackson/CSCM20_Project/blob/main/images/Updated%20graphs/VADER%20positive%20negative%20and%20neutral.png)
![VADER proportion of negative tweets by week](https://github.com/ORJackson/CSCM20_Project/blob/main/images/Updated%20graphs/VADER%20neg%20week.png)


## To run / recreate this project

In order to run this project access to Twitter API v2 is required with academic research access.


See **virtualEnvGuide.md** to create a virtual env. All dependencies are displayed in requirements.txt. See how to display all dependencies.

Create a .env file with: 

BEARER-TOKEN = 
API-KEY =
API-SECRET-KEY = 

