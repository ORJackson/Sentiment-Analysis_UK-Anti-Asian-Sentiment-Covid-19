#Keywords are taken from a list of Asian related racial slurs
#list of countries from East Asia and Southeast asia and the nationalities of those countries 

import pandas
from pandas import *

keyWordData = read_csv('rawkeywordlist.csv')
words = keyWordData['keyword'].tolist()

seen = []

#if hyphens not desired use this:

for word in words:
    newWord = word.rstrip()
    newWord = newWord.lower()
    if newWord in seen:
        continue      
    if "-" in newWord:
        unHyphenated = newWord.replace("-", " ")
        if unHyphenated not in seen:
            seen.append(unHyphenated)
            continue 
        else:
            continue 
    seen.append(newWord)



#if hyphens desired use this:

# for word in words:
#     newWord = word.rstrip()
#     newWord = newWord.lower()
#     if newWord in seen:
#         continue        
#     seen.append(newWord)
#     if " " in newWord:
#         hyphenated = newWord.replace(" ", "-")
#         if hyphenated not in seen:
#             seen.append(hyphenated)
#     if "-" in newWord:
#         unHyphenated = newWord.replace("-", " ")
#         if unHyphenated not in seen:
#             seen.append(unHyphenated)


sortedSeen = sorted(seen)

df = pandas.DataFrame(data={"keyword" : sortedSeen})
df.to_csv("./AsianKeywords.csv", sep=",", index=False)

query = ""

for word in sortedSeen:
    query = query + word + " OR "

print(query)




