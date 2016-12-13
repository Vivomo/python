from PIL import Image
import pytesseract

image = Image.open('E:\git\pythonCode\src\img\qqjt1.png')
print(pytesseract.image_to_string(image))
