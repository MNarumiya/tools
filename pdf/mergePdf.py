import PyPDF2
from pathlib import Path
import subprocess
from minimizePdf import minimizePdf
from util import isMatchExtensions

def mergePdf(pdf_path_strs, dst_path_str):
    """
    -- input --------------
    pdf_path_strs :
        str[](配列). 結合したいpdfのpath(複数)
    dst_path_str :
        str. 出力したいpdfのpath.
    -- output --------------
    void
    """
    
    merger = PyPDF2.PdfFileMerger()
    for pdf_path_str in sorted(pdf_path_strs):
        merger.append(pdf_path_str)
    merger.write(dst_path_str)
    merger.close()
 
def solvePassword(src_path, dst_path, src_password):
    try:
        command=f"qpdf --password='{src_password}' --decrypt {src_path} {dst_path};"
        subprocess.run([command], shell=True)
        with open(dst_path, mode='rb') as fp:
            reader = PyPDF2.PdfFileReader(fp)
            print(f"Number of page: {reader.getNumPages()}")
        return 1
    except FileNotFoundError:
        return 0

def changePassword(src_path, dst_path, src_password=None, dst_password=None):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    if (src_password):
        src_pdf.decrypt(src_password)

    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)

    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)

    if(dst_password):
        dst_pdf.encrypt(dst_password)

    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)
        print("set password : Done")

def setPassword(src_path, dst_path, password):
    changePassword(src_path, dst_path, None, password)

def inputFiles():
    """
    -- input --------------
    void.
    -- output --------------
    file_path_strs : 
        list<str>.
    """
    while (1):
        print("put in pdf file or dir or put [q] key: ")
        file_path_strs = input().split()

        # 入力されたのがdirの場合
        dir_path = Path(file_path_strs[0])
        file_path_strs = [] # 初期化
        if (dir_path.suffix == ""):
            files = dir_path.glob("*")
            for file in files:
                if(isMatchExtensions(file, [".pdf"])):
                    file_path_strs.append(str(file))

        while (1):
            print("Is it OK, yo want to merge file? [y/n]:")
            for file_path_str in file_path_strs:
                print(file_path_str)
            key = input()
            if (key == "y" or key == "n"):
                break
        if (key=="y"):
            break
    new_file_path_strs = []
    while (1):
        print("Do you wont to sort list? [y/n]")
        key = input()
        if (key == "y"):
            new_file_path_strs = sorted(file_path_strs)
            print("Is it Ok? [y/n]:")
            for new_file_path_str in new_file_path_strs:
                print(new_file_path_str)
            new_key = input()
            if (new_key == "y"):
                break
            elif (new_key == "n"):
                print("back list")
                break
        elif (key == "n"):
            break
    return file_path_strs

def main():
    file_path_strs = inputFiles()
    root_dir = Path(file_path_strs[0]).parent
    merger_paths = []

    for file_path_str in file_path_strs:
        reader = PyPDF2.PdfFileReader(file_path_str)
        if (reader.isEncrypted):
            result = 0
            nonpass_path_str = str(root_dir) + "/" + str(Path(file_path_str).stem) + "_nopass.pdf"
            while(1):
                if (result != 0):
                    break
                print("input password, for {}: ".format(file_path_str))
                password = input()
                result = solvePassword(file_path_str, nonpass_path_str, password)
                while(result == 0):
                    print("faild. One more try?[y/n]")
                    y_n_key = input()
                    if (y_n_key == "n"):
                        result = -1
                        print("no merge")
                        return 0
                    elif (y_n_key == "y"):
                        break
            merger_paths.append(nonpass_path_str)
        else:
            merger_paths.append(file_path_str)

    print("input pdf title (ex. hoge.pdf) : ")
    title = input()
    output_path = str(root_dir) + "/" + title
    mergePdf(merger_paths, output_path)

    y_n_key = ""
    while(1):
        print("minimize? [y/n]:")
        y_n_key = input()
        if (y_n_key == "y"):
            minimizePdf(output_path)
            break
        elif (y_n_key == "n"):
            break

if __name__ == '__main__':
    main()


    