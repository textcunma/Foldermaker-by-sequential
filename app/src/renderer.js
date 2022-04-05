const choiceBtn=document.getElementById('choiceBtn');
let fileList=[];                                        //ファイルリストを定義
const fs = require('fs');
const path = require('path');

choiceBtn.addEventListener('change', ev => {
    let root=path.dirname(ev.target.files[0].path);   //選択されたフォルダパス

    for (let i = 0; i < ev.target.files.length; i++) {
        let file = ev.target.files[i];          //ファイルに関する情報（ファイル名、パス名など）を取得
        let ext=file.name.split('.').pop();     //拡張子取得
        if (ext=="jpg" || ext=="png"){          //拡張子判定
            let name=file.name.split('.')[0];   //ファイル名取得
            let newpath=path.join(root, name);                  //移行先のパス名（ファイル名を除く）
            let from=file.path;                                 //移行前のファイル位置
            let to=path.join(newpath, file.name);               //移行後のファイル位置

            if (fileList.indexOf(name) !== -1) {    //ファイルリストに存在していたら...
                //既存フォルダにファイルを移行
                fs.rename(from, to, function(err) {
                    if ( err ) console.log('ERROR: ' + err);
                });
            }else{                                  //ファイルリストに存在していなかったら...
                //ファイル名種類記録
                fileList.push(name);

                //新規フォルダを作成
                fs.mkdir(newpath, (err) => {
                    if (err) { throw err; }
                });

                //ファイルを移行
                fs.rename(from, to, function(err) {
                    if ( err ) console.log('ERROR: ' + err);
                });
            }
        };
    }
    alert("移行完了しました");  //終了報告
});