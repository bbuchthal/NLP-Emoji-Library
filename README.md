# Emoji Lexicon

This project aims to enrich the current sentiment analysis libraries by creating a probabilistic lexicon of emojis that more accurately prescribe the sentiment of a tweet.  We hope that by creating a lexicon that maps emojis to likelihoods of various sentiments, researchers will be able to incorporate our emoji lexicon into their own sentiment analysis pipeline, to further enrich their sentiment analysis and to complete tasks such as irony and sarcasm detection.

## Getting Started

These instructions will get you a copy of the project up and get the sentiment of the tweets.

### Tweets Streaming

First install all required packages

```
npm install twit
npm install csv-write-stream
```

run the streaming program

```
node index.js
```

### Sentiment Analysis
first in the same folder root directory, run stanford NLP backend

```
java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
```

run the sentiment analysis program

```
python sentiment.py
```

### Output
* the tweets collected will be in tweets.csv
* the tweets sentiment result will be in tweetsentiment.csv

## Building Lexicon

In the same folder root directory, run lexicon building program.

The program takes two arguments. The first argument is the tweets sentiment csv file, eg. tweetsentiment.csv. The second argument is optional. If provided a number n, it would find the first n tweets in different sentiments; or else, it would run through the whole csv file.

```
python3 create_dictionary.py tweetsentiment.csv 800
```

### Output

* the emoji lexicon will be in lexicon.json

## Built With

* python 3