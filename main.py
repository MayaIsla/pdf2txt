
from pdf2image import convert_from_path
from pytesseract import image_to_string
from pytesseract import Output, pytesseract
from PIL import Image

converted_scan = convert_from_path('scanned.pdf', 500, poppler_path=r'D:\filepath\to\poppler')

for i in converted_scan:
    i.save('scan_image.png', 'png')

pytesseract.tesseract_cmd = r'C:\filepath\to\tesseract.exe'
text = image_to_string(Image.open('scan_image.png'))
with open('scan_text_output.txt', 'w') as outfile:
    outfile.write(text.replace('\n\n', '\n'))


#prereqs are to install poppler via github, and import pytesseract packages directly
