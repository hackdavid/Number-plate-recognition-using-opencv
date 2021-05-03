# C:\Program Files\Tesseract-OCR\tesseract.exe
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
img=cv2.imread("car2.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
flter=cv2.bilateralFilter(gray,11,15,15)
edge=cv2.Canny(flter,170,200)
contor,herf=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
ctn=sorted(contor,key=cv2.contourArea,reverse=True)
for c in ctn:
    peri=cv2.arcLength(c,True)
    epsilon=0.018*peri
    apporx=cv2.approxPolyDP(c,epsilon,True)
    if len(apporx)==4:
        x,y,w,h=cv2.boundingRect(apporx)
        img2=img[y:y+h,x:x+w]
        configr = ('-l eng --oem 1 --psm 3')

        text=pytesseract.image_to_string(img2,config=configr)
        print(text)
        final=cv2.drawContours(img,[apporx],-1,(255,0,0),3)
        break
cv2.imshow("plate detected",img)
cv2.waitKey(0)
