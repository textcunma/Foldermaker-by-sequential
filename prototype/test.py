import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

directory_name=""   #指定されたディレクトリの名前
filenames=[]            #選択された複数ファイルの名前
nametype_list= []       #連番画像の名前の種類

# 同じ連番画像であるか判定
def sameNumber(filePath):
    fileName = os.path.basename(filePath)
    file = fileName.split(".")[0]
    return file

# ファイル選択後の処理
def filedialog_clicked():
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    
    global filenames
    filenames = filedialog.askopenfilenames(filetype = fTyp, initialdir = iFile)
    entry.set(filenames)
    
    #ディレクトリ名を取得（複数ディレクトリ同時選択は考慮しない）
    global directory_name
    directory_name=os.path.dirname(filenames[0])
    
    #連番画像の名前の種類を把握
    global nametype_list
    for f in filenames:
        nametype_list.append(sameNumber(f))    
    nametype_list=list(set(nametype_list))
    
    directory.set(nametype_list)


# 実行ボタン後の処理
def run():
    global nametype_list
    # ディレクトリを作成
    for type in nametype_list:
        os.makedirs(directory_name+"/"+type+"/", exist_ok=True)
    
    global filenames
    #ファイルをコピーして移動
    for f in filenames:
        fileName = os.path.basename(f)
        file = fileName.split(".")[0]

        shutil.copy(f, directory_name+"/"+file+"/")

    messagebox.showerror("お知らせ", "完了しました")

def main():
    root = Tk()                                 # ウィンドウを作成
    root.title("連番ファイルフォルダ分けツール") # ウィンドウのタイトルを設定
    root.geometry("500x150")                    # ウィンドウのサイズを設定
    root.resizable(width=False, height=False)   # ウィンドウのサイズ変更不可
    
    
    # headerの作成
    header = tk.Frame(root, pady=5, padx=5, relief=tk.RAISED)
    header.grid(row=0, column=0, sticky=E)
    
    # ヘッダー：「ファイル選択」ラベル
    inputfiles_Label = ttk.Label(header, text="ファイル選択", padding=(5, 2))
    
    #ヘッダー： 「ファイル選択」入力欄
    entry=StringVar()
    inputfiles_entry = ttk.Entry(header,textvariable=entry,width=30)

    #ヘッダー： 「ファイル選択」ボタン
    inputfiles_button = ttk.Button(header, text="選択", command=filedialog_clicked)
    
    #ヘッダー設置
    inputfiles_Label.pack(padx=40,side=LEFT)
    inputfiles_entry.pack(side=LEFT)
    inputfiles_button.pack(side=LEFT)
    
    # ボディーの作成
    body = ttk.Frame(root, padding=10)
    body.grid(row=1,column=0,sticky=W)
    directory=StringVar()
    title = ttk.Label(body, text="ファイル種類名", padding=(5, 2))
    title.pack(padx=40,side=LEFT)
    body_label = ttk.Label(body, textvariable=directory, padding=(5, 2))
    body_label.pack(padx=40,side=LEFT)

    # フッターの作成
    footer = ttk.Frame(root, padding=10)
    footer.grid(row=5,column=0,sticky=W)
    
    # 実行ボタンの設置
    runBtn = ttk.Button(footer, text="実行", command=run)
    runBtn.pack(fill = "x", padx=30, side = "left")

    root.mainloop()

if __name__ == "__main__":
    main()