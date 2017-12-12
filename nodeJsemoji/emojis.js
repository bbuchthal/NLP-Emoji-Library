const emojisStr = '😂😊😭❤️💕✨😘👏🔥🙂🙃😔😒😏😡😨';
const emojis = [...emojisStr]
  .filter(emoji => emoji.length > 0)
  .filter(emoji => emoji !== '\uFE0F');
  
module.exports = emojis;
