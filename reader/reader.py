from PIL import Image
import pytesseract
filename = 'tmp38qq9oqq\zadanie-004.png'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename), lang="pol")

print(text)