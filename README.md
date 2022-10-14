# Anti-Asian sentiment in the UK during the Covid-19 pandemic: analysing Twitter data through sentiment analysis using SVM and VADER machine learning

Coronavirus disease 2019 (COVID-19) is the illness caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), first discovered in Wuhan City, Hubei Province, China. The COVID-19 pandemic has dramatically changed the way individuals live their lives since the virus’s first discovery in China in 2019. For a large number of individuals, this novel coronavirus has not only presented health risks but also risks to their physical and mental wellbeing as they have become victims of unfair prejudice. This has been caused by fear of the virus which has led to a wave of anti-Asian sentiment and discrimination, as well as a sharp increase in hate crimes.  This change in sentiment has been well-documented, with reports of victims being spat on, and otherwise being physically and verbally assaulted in the street becoming commonplace. Statistics show that this is reflected online, with social media sites seeing a dramatic increase in negative posts referring to Asian people. One NHS doctor wrote that to stay silent is to allow “anti-Asian sentiment - and racist attacks to damage our society, the repercussions of which will likely persist beyond the pandemic”  (Coates, 2020). It is highly likely that this anti-Asian sentiment still exists and the repercussions are still being felt. There is an obligation to attempt to uncover this prejudice if it exists, and that is the ambition of this project - to examine the extent to which anti-Asian sentiment has changed in the UK over the course of the pandemic by analysing Twitter data.

# Keywords for search query:
a combination of East and South East Asian countries and nationalities and racial slurs for Asian people.
Racial slurs taken from a public online database of racial slurs.
Full list can be seen in **'rawkeywordlist.csv'**.

In **'asianKeywordOrderedBySum.ipynb'** Keywords are extracted from csv and placed in order of relevance (most used to least used) by examining each word's use in January 2019 and January 2020.
Any keyword that was used 0 times in both months is removed (twitter's search query is limited to 1024 characters).
Final keyword list found in **'finalAsianKeywords'**.

# Tweet Counts

In **'tweetCountsAsianKeywords.ipnb'** a query is created using the finalAsianKeywords to search for tweets coming from the UK from January 2019 to June 2022.
Using this query I display changing levels of matching tweets.

# Collecting data

In **'tweetScrape.ipnb'** I collect matching tweets using the keyword list, over the period Jan 2019 - June 2020.
tweets are saved in **'twitterDataOutput.csv'**.
nearly 500,000 matching tweets were collected.

# Sentiment Analaysis Using SVM

In **sentimentAnalysisSVM_PreprocessingData.ipynb** I prepare the sentiment140 dataset (a dataset of 1.6 million tweets labelled positive or negative). I do not alter the original data, but instead create a new dataset that includes the label, the original tweet, and several different processed versions (with numbers, punctuation, links etc removed, stopwords removed, and all words are lemmatized and one unlemmatized version). In order from least processed to most processed collumns: tweet > cleanTweet > unLemNoStops (stop words removed but no lemmatization) > lemmatizedTweet.

In **sentimentAnalysisSVM_Models.ipynb** I display some insights on the dataset and I train several versions of a linearSVC model and display accuracy / f1 scores for these models. 

![SVM sentiment analysis by week](https://github.com/ORJackson/CSCM20_Project/blob/main/images/SVM%20LinearSVC/SVM%20(LinearSVC)%20sentiment%20analysis%20negative%20tweets%20as%20a%20percentage%20of%20total%20Tweets%20collected%20per%20month.png)

# Sentiment Analysis using VADER

In **'vaderSentimentAnalysis.ipynb'** I carry out sentiment analysis using VADER.
Tweets are assigned a value of positive, negative, or neutral.
I display wordclouds displaying most commonly used words in the three groups.
I display a graph showing changing levels of positive, negative, and neutral tweets over time.



![Vader sentiment analysis](https://github.com/ORJackson/CSCM20_Project/blob/main/images/VADER/VADER1(preprocessing1).png)

