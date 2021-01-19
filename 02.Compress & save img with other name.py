
import cv2

imageFile = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lenna.png'
img = cv2.imread(imageFile)  # 컬러표현
cv2.imwrite('C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena.bmp',img)
cv2.imwrite('C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena.png',img)
cv2.imwrite('C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena2.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])
#압축률 0~9, 디폴트 = 3
cv2.imwrite('C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena2.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,90])
#품질 지정 : 0%~100%, 디폴트는 95%
