
import cv2

imageFile = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lenna.png'
img = cv2.imread(imageFile)  # 컬러표현
img2 = cv2.imread(imageFile, 0)  # GrayScale 표현(폴더경로, image size에 적합한 채널(크기별로 구분되어있음)
cv2.imshow('Lenna color', img)
cv2.imshow('Lenna grayscale', img2)

cv2.waitKey()
cv2.destroyAllWIndows()
