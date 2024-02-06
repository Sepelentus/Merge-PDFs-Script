from PyPDF2 import PdfMerger
from pathlib import Path

import os

BASE_DIR = Path(__name__).resolve().parent

folder_path = BASE_DIR

file_urls=[]

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
                file_path = os.path.join(root, file_name)
                if file_name.endswith(".pdf"):
                        file_urls.append(file_path)

print("LOADING...")

merger = PdfMerger()

for pdf in file_urls:
        merger.append(pdf)
output_path = "merged.pdf"

merger.write(output_path)
merger.close()

print("DONE")