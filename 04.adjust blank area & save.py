import cv2
from matplotlib import pyplot as plt
imageFile = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena.png'
imgGray = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)

plt.figure(figsize = (6,6)) # 6inch 6inch 사이즈로 띄움
plt.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1) # 좌<우, 하<상 으로 세팅해서 영상출력범위 설정
plt.imshow(imgGray,cmap='gray')
##plt.axis('tight')
plt.axis('off')
plt.savefig('C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\0205.png')
plt.show()
