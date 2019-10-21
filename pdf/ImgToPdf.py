import img2pdf
from pathlib import Path
from PIL import Image
import shutil
from util import isMatchExtensions

def isImgPath(check_path):
    """
    -- input --------------
    check_path :
        pathlib.path.
    -- output --------------
    void
    """
    return isMatchExtensions(check_path, [".jpg", ".png", ".JPG", ".PNG"])

#画像からPDFにする
def ImageToPdf(inputpath, outputpath): 
    """
    -- input --------------
    inputpath :
        pathlib.path.
    -- output --------------
    outputpath :
        pathlib.path.
    """

    lists = sorted(list(inputpath.glob("*")))#単フォルダ内を検索
    img_list = [str(i) for i in lists if isImgPath(i)]
    if (img_list == []):
        return 0

    #pdfを作成
    with open(outputpath, "wb") as f:
        #jpg,pngファイルだけpdfに結合
        #Pathlib.WindowsPath()をstring型に変換しないとエラー
        f.write(img2pdf.convert(img_list))
    print(outputpath.name + " :Done")
    size_mb = round(float(outputpath.stat().st_size) / (2**20), 1)
    print("file size: " + str(size_mb) + "MB")
    return 1

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

    # PL = [p for p in Path(imagepath).glob('*') if p.match("*./jpg/i") or p.match("*./png/i")]
    PL = [p for p in Path(imagepath).glob('*') if isImgPath(p)]

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
    #作業フォルダを入力させる
    print("put in your work folder path: ")
    base_path = Path(input())

    if (not base_path.exists()):
        print("not found img file")
        return

    while(1):
        print("is resize?:[y/n]")
        ans = input()
        if (ans == 'y' or ans == 'n'):
            is_resize = ans == 'y'
            break
    if (is_resize):
        imagepath = resizeImg(base_path)
    else:
        imagepath = base_path

    outputpath = Path(str(base_path) + '/' + base_path.name + ".pdf")
    result = ImageToPdf(imagepath, outputpath)

    if (result == 0):
        print("Not Found Image!")
        return
    
    if (is_resize):
        shutil.rmtree(imagepath)
        print("remove resize file")

if __name__ == "__main__":
    main()