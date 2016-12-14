from PIL import Image
import pytesseract

image2 = Image.open('E:\git\pythonCode\src\img\captcha.jpg')
print(pytesseract.image_to_string(image2))
