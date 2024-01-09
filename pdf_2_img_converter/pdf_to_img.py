from pdf2image import convert_from_path
from pathlib import Path
import os

pdf_path = Path("Drop PDF")
img_path = Path("IMG final")

while True:
    try:
        pdf_list = os.listdir(pdf_path)

        for files in pdf_list:
            count = 0
            new_path = Path(pdf_path.__str__() + "/" + files)
            print(new_path)
            File = convert_from_path(new_path)
            file_name = files.replace(".pdf", "")
            file_folder = Path(f"{img_path}/{file_name}/")
            print(file_folder)
            os.mkdir(file_folder)

            for page in File:
                fileName = (f"{file_folder}/{count}- {files}")
                fileName = fileName.replace(".pdf", ".jpg")
                print(fileName)

                fileName = Path(fileName)
                page.save(fileName, format="JPEG")
                count +=1

            print(f"{files} is done converting\n")
            os.remove(new_path)

    except Exception as e:
        print(e)

