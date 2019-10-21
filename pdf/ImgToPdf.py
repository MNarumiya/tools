import os
import img2pdf
from pathlib import Path
from PIL import Image
import shutil

#単処理
def ImageToPdf(inputpath):
    while(1):
        print("is resize?:[y/n]")
        ans = input()
        if (ans == 'y' or ans == 'n'):
            is_resize = ans == 'y'
            break
    if (is_resize):
        imagepath = resizeImg(inputpath)
    else:
        imagepath = inputpath
    outputpath = Path(str(inputpath) + '/' + inputpath.name + ".pdf")
    lists = sorted(list(imagepath.glob("*")))#単フォルダ内を検索
    #pdfを作成
    with open(outputpath, "wb") as f:
        #jpg,pngファイルだけpdfに結合
        #Pathlib.WindowsPath()をstring型に変換しないとエラー
        f.write(img2pdf.convert([str(i) for i in lists if i.match("*.jpg") or i.match("*.png")]))
    print(outputpath.name + " :Done")
    size_mb = round(float(outputpath.stat().st_size) / (2**20), 1)
    print("file size: " + str(size_mb) + "MB")

    if (is_resize):
        shutil.rmtree(imagepath)
        print("remove resize file")

def resizeImg(imagepath):
    # カラー用のリサイズをするか否か
    while(1):
        print("which specify size, height or width?:[h/w]")
        ans = input()
        if (ans == 'h' or ans == 'w'):
            break
    while(1):
        print("put on size:[number]")
        size_str = input()
        if (size_str.isdecimal()):
            size = int(size_str)
            break

    PL = [p for p in Path(imagepath).glob('*') if p.match("*.jpg") or p.match("*.png")]
    # for i, p in enumerate(sorted(PL)):
    #     print(p)
    half_img_path = Path(str(imagepath) + '/resize')
    half_img_path.mkdir(exist_ok=True)
    print("make file : " + str(half_img_path))
    
    for f in sorted(PL):
        img = Image.open(f)
        
        if (img.width >= size or img.height >= size):
            scale = size/img.height if (ans == "h") else size/img.width
        else:
            scale = 1.0
        img_resize = img.resize((int(img.width * scale), int(img.height * scale)))
        img_title, fext = f.name.split('.')
        img_resize.save(str(half_img_path) + '/' + img_title + '_resize'+ '.'  + fext)
    print("resize : Done")
    return half_img_path

#複数フォルダをループ処理する
def main():
    #作業フォルダ
    print("put in your work folder path: ")
    base_path = Path(input())

    if (base_path.exists()):
        # リサイズする
        ImageToPdf(base_path)

    else:
        print("not found img file")
        return

if __name__ == "__main__":
    main()