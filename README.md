# Emoji Lexicon

* ### Tweets Streaming

	* First install all required packages
		```
		npm install twit
		npm install csv-write-stream
		```
	* run the streaming program
		```
		node index.js
		```

* ### sentiment analysis
	* first in the same folder root directory, run stanford NLP backend
		```
		java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
		```
	* run the sentiment analysis program
		```
		python sentiment.py
		```


* ### Output
	* the tweets collected will be in tweets.csv
	* the tweets sentiment result will be in tweetsentiment.csv
