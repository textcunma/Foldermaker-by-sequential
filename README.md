# 連番画像に合わせたフォルダ生成
「○○.01.jpg」「○○.02.jpg」などの場合に「○○」という名称のフォルダを生成します。
Tkinterを用いて作成し、pyinstallerを用いて実行ファイルにしています。
![image](./assets/image.jpg)

- test.exe　実行ファイル
- test .py   ソースコード

### 注意事項
「ピリオド(.)」を検出しているアルゴリズムのため、「○○01.jpg」のような名称ではなく、
「**○○.01.jpg**」のようなものでなければいけません。

### 参考サイト
[【Python】tkinterでファイル&フォルダパス指定画面を作成する](https://qiita.com/dgkmtu/items/2367a73f7e2d498e6075)

### 発想元
https://twitter.com/bearshu/status/1466669324928958464?s=20