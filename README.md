# CSCM20_Project
 Master's final project - sentiment analysis of Twitter data using VADER and SVM machine learning

Coronavirus disease 2019 (COVID-19) is the illness caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), first discovered in Wuhan City, Hubei Province, China. The COVID-19 pandemic has dramatically changed the way individuals live their lives since the virus’s first discovery in China in 2019. For a large number of individuals, this novel coronavirus has not only presented health risks but also risks to their physical and mental wellbeing as they have become victims of unfair prejudice. This has been caused by fear of the virus which has led to a wave of anti-Asian sentiment and discrimination, as well as a sharp increase in hate crimes.  This change in sentiment has been well-documented, with reports of victims being spat on, and otherwise being physically and verbally assaulted in the street becoming commonplace. Statistics show that this is reflected online, with social media sites seeing a dramatic increase in negative posts referring to Asian people. One NHS doctor wrote that to stay silent is to allow “anti-Asian sentiment - and racist attacks to damage our society, the repercussions of which will likely persist beyond the pandemic”  (Coates, 2020). It is highly likely that this anti-Asian sentiment still exists and the repercussions are still being felt. There is an obligation to attempt to uncover this prejudice if it exists, and that is the ambition of this project - to examine the extent to which anti-Asian sentiment has changed in the UK over the course of the pandemic by analysing Twitter data.

# Keywords for search query:
a combination of East and South East Asian countries and nationalities and racial slurs for Asian people
Racial slurs taken from a public online database of racial slurs
Full list can be seen in **'rawkeywordlist.csv'**

In **'asianKeywordOrderedBySum.ipynb'** Keywords are extracted from csv and placed in order of relevance (most used to least used) by examining each word's use in January 2019 and January 2020
Any keyword that was used 0 times in both months is removed (twitter's search query is limited to 1024 characters)
Final keyword list found in **'finalAsianKeywords'**

# Tweet Counts

In **'tweetCountsAsianKeywords.ipnb'** a query is created using the finalAsianKeywords to search for tweets coming from the UK from January 2019 to June 2022 
Using this query I display changing levels of matching tweets

# Collecting data

In **'tweetScrape.ipnb'** I collect matching tweets using the keyword list, over the period Jan 2019 - June 2020
tweets are saved in **'twitterDataOutput.csv'**
nearly 500,000 matching tweets were collected

# Sentiment Analysis using VADER

In **'vaderSentimentAnalysis.ipynb'** I carry out sentiment analysis using VADER 
Tweets are assigned a value of positive, negative, or neutral 
I display wordclouds displaying most commonly used words in the three groups
I display a graph showing changing levels of positive, negative, and neutral tweets over time



