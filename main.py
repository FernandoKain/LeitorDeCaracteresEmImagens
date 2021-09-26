# links uteis:
# corrigir instalação windows do tesseract: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata - fazer download do por.traineddata e colocar justamente no caminho da instalação do tesseract.exe - no meu caso: C:\Program Files\Tesseract-OCR\tessdata (Colocar dentro da pasta "tessdata"

# pegar linguas: print(pytesseract.get_languages())

# pip install opencv-python
# pip install pytesseract

import pytesseract
import cv2

# Passo 1: ler a imagem

imagem = cv2.imread("email.png")

caminho = r"C:\Program Files\Tesseract-OCR"

# Passo 2: perdir para o tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)

