import cv2
import pytesseract
from gtts import gTTS
import os
from playsound import playsound
from main import objDet
from distance import getDis
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def imgToText():
    img=cv2.imread('C:\\Users\\Shankaranaarayanan\\Desktop\\Shankar\\KCT\\3rdYear\\SamsungPrism\\images\\image.png', cv2.IMREAD_GRAYSCALE)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,21, 20)
    # t = pytesseract.image_to_string(thresh)
    # print(t)
    # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('im',thresh)
    if cv2.waitKey(0) == ord('q'):
        # ok_flag = False
        cv2.destroyAllWindows() 
    text = (pytesseract.image_to_string(thresh))
    return text

def textToSpeech(t):
    audio = gTTS(text=t, lang="en", slow=False)
    audio.save("test01.mp3")
    # os.system("start example.mp3")
    playsound('test01.mp3')
    # print('playing sound using  playsound')
t = imgToText()
textToSpeech(t)
objDet()
getDis()