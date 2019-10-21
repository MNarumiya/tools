# 概要
## ファイル構造
```
- README.md
- ImgToPdf.py
- minimizePdf.py
- mergePdf.py
```

## 全体としての共通の準備
- 仮想環境の立ち上げ
    ```
    python3 -m venv venv
    ```

- Pathlibのインストール
    ```
    pip install Pathlib
    ```

## 全体としての共通の操作
1. まず, 仮想環境の有効化
    ```
    . venv/bin/activate
    ```

2. 終了するときは, 仮想環境を終わらせる
    ```
    deactivate
    ```

# 画像を統合してPDFにする
プログラムは, `ImgToPdf.py`

## 準備
- img2pdfのインストール
    ```
    pip install img2pdf
    ```



# PDFのサイズ圧縮
プログラムは, `minimizePdf.py`

## 準備
- GhostScriptのインストール
    ```
    brew install ghostscript
    gs --version
    # 9.27
    ```



## 操作方法
1. pythonでプログラム実行
    ```
    python mergePdf.py
    ```



# PDFの結合
プログラムは, `mergePdf.py`

## 準備
- PyPDF2のイントール
     ```
     pip install PyPDF2
     ```

## 手順


## 操作方法
1. pythonで実行
    ```
    python mergePdf.py
    ```
    - 応答に答える形でファイルを結合していく
        ```
        put in pdf file or put [q] key: 
        # pdf_path1.pdf pdf_path1.pdf pdf_path3.pdf
        (以下略)
        ```


# 参考
- [PDF をコマンドラインから圧縮する | Qiita](https://qiita.com/peaceiris/items/f1f4c9734b98cf9c7113)
- [pythonで複数画像をPDFファイルに変換する | Qiita](https://qiita.com/meznat/items/31d947ed4826350fd9fa)
- [Python, PyPDF2でPDFを結合・分割（ファイル全体・個別ページ） | note.nkmk.me](https://note.nkmk.me/python-pypdf2-pdf-merge-insert-split/)
- [Python, PyPDF2でPDFのパスワードを設定・解除（暗号化・復号） | note.nkmk.me](https://note.nkmk.me/python-pypdf2-pdf-password/)
- [Python, pathlibでファイル名・拡張子・親ディレクトリを取得 | note.nkmk.me](https://note.nkmk.me/python-pathlib-name-suffix-parent/)
- [PDFをPython（PyPDF2）で操作する - PDF・暗号化PDFファイルの読み込み | そうなんでげす](https://www.soudegesu.com/post/python/open-pdf-with-pypdf2/#%E5%A4%B1%E6%95%97%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3)
- 