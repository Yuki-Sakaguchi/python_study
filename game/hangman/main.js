// hangman(ES6)
// nodeで書いてみる

var readlineSync = require("readline-sync");

class Hangman {
  /**
   * ハングマンの初期設定
   * @param {String} word 
   */
  constructor(wordList) {
    // 初期設定
    this.wordList = wordList;
    this.word = this.wordList[Hangman.createRandom(0, wordList.length-1)];
    const word = this.word;
    this.wrong = 0;
    this.rletters = (function() {
      const tmp = [];
      for (let i = 0; i < word.length; i++) tmp.push(word[i]);
      return tmp;
    })();
    this.board = (function() {
      const tmp = [];
      for (let i = 0; i < word.length; i++) tmp.push('_');
      return tmp;
    })();
    this.isWin = false;
    this.stages = [
      '',
      '______    ',
      '|    |    ',
      '|    O    ',
      '|   /|\\   ',
      '|   / \\   ',
      '|         ',
    ];
    
    //  ゲーム実行
    console.log('-----------------------\nハングマンへようこそ！\n-----------------------');
    this.play();
  }
  
  /**
   * ゲーム
   */
  play() {
    while (this.wrong < this.stages.length-1) {
      console.log('\n===\n');
      console.log('１文字を予想してください');
      const input = readlineSync.question();

      const cind = this.rletters.indexOf(input);
      if (cind != -1) {
        // 正解
        this.board[cind] = input;
        this.rletters[cind] = '$';
      } else {
        // 不正解
        this.wrong++;
      }

      // 回答を表示
      console.log('\n【回答】');
      let word = '';
      for (let i = 0; i < this.board.length; i++) {
        word += this.board[i];
      }
      console.log(word);

      const e = this.wrong+1;
      console.log('\n【ハングマン】');
      for (let i = 0; i < e; i++) {
        console.log(this.stages[i]);
      }

      // 勝ちの場合
      if (this.board.indexOf('_') == -1) {
        console.log('\nあなたの勝ちです');
        console.log(`正解は【${this.word}】でした！`);
        this.isWin = true;
        break;
      }
    }

    // 負けの場合
    if (!this.isWin) {
      console.log('\nあなたの負けです');
      console.log(`正解は【${this.word}】でした！`);
    }
  }

  static setWordList(wordList) {

  }

  /**
   * ランダムを生成
   * @param {Number} min 
   * @param {Number} max 
   */
  static createRandom(min, max) {
    return Math.floor(Math.random() * (max + 1 - min)) + min;
  }
}

// ゲームの実行
new Hangman([
  'banana',
  'apple',
  'orange',
  'coffee',
  'tea',
]);