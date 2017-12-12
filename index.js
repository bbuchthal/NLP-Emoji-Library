const Twitter = require('twit');
const emojis = require('./emojis');
var fs = require('fs');
var csvWriter = require('csv-write-stream')

const twitter = new Twitter({
  consumer_key:         'xvvwwphj05QbZLvFrM705e99o',
  consumer_secret:      'p9wLPyKid96IpMDXki50je19sew4Q5fQmS5vvpetSno5yklxIj',
  access_token:         '773943536458817536-8z2cVnCssxjSfdhwgbOt7UqAUmOHebl',
  access_token_secret:  'ASUNkh4HAVFnIZYZL2Hkgstb5GDSuhWVAY1wzNcZuVgao'
});

const stream = twitter.stream('statuses/filter', {
  track: emojis,
  language: 'en'
});

let emoji = '😂😊😭❤️💕✨😘👏🔥🙂🙃😔😒😏😡😨';

const stats = {};
var writer = csvWriter({headers: ['id','text', 'emojis']})
writer.pipe(fs.createWriteStream('tweets.csv'))
const tweetStreamer = tweet => {

  const second = Math.floor(Date.now() / 1000);
  if (stats[second] !== undefined) {
    stats[second]++;
  } else {
    stats[second] = 1;
  }
  let text = `${tweet.text}`;
  let textArr = text.split('');
  let storeArr = '';
  let checkArr = [];
  for (i = 0; i < textArr.length; i++) {
    if (emoji.includes(textArr[i])){
      if (!(checkArr.indexOf(textArr[i]) !== -1)){
        storeArr += textArr[i];
        checkArr.push(textArr[i])
        console.log(textArr[i])

      }
    }
  }
  strippedTweet = text.replace(/(\r\n|\n|\r)/gm,"");
  writer.write([`${tweet.id}`, strippedTweet,storeArr])
  
}


stream.on('tweet', tweetStreamer);


process.on('SIGINT', () => {
  console.log('Stats:');
  Object.keys(stats).forEach(second => {
    console.log(`[${second}]: ${stats[second]} tweets`);
  });
  process.exit();
});
