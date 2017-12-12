# -*- coding: utf-8 -*-
import sys
import csv

# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf-8')
from pycorenlp import StanfordCoreNLP
from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

output = ''
emojiGroup = []

with open( 'tweets.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
    	tmp = strip_punctuation(row[1])
    	emojiGroup.append(row[2])
    	tmp = tmp.replace('.','')+'. '
    	output += tmp

nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate(output,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 10000000000,
                   })

with open('tweetsentiment.csv','w') as file:
	columnTitleRow = "id, text, originalSentiment, emoji\n"
	file.write(columnTitleRow)
	for s in res["sentences"]:
		index = s["index"]
		words = " ".join([t["word"] for t in s["tokens"]])
		words = words.replace(',', ' ')
		score = s["sentimentValue"]
		row = str(index) + "," + words + "," + score + "," + emojiGroup[index] + "\n"
		file.write(row)
		print(row)




	   