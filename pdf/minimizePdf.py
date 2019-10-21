from pathlib import Path
import subprocess

def minimizePdf(input_pdf_path_str):
    """
    -- input --------------
    input_pdf_path_str :
        str.
    -- output --------------
    void
    """
    input_pdf_path = Path(input_pdf_path_str)
    output_pdf_path_str = str(input_pdf_path.parent) + "/" + input_pdf_path.stem + "_min.pdf"
    command = "gs -sDEVICE=pdfwrite\
         -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH\
              -sOutputFile={0} {1}".format(output_pdf_path_str, str(input_pdf_path))
    subprocess.run([command], shell=True)
    print("minimize : Done")
    print("output file : {}".format(output_pdf_path_str))

def main():
    print("put in minimize pdf files or put [q] key: ")
    file_path_strs = input().split()
    for file_path_str in file_path_strs:
        minimizePdf(file_path_str)

if __name__ == "__main__":
    main()