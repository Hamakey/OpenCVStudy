
import cv2
from matplotlib import pyplot as plt
imageFile = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\Lena.png'
imgBGR = cv2.imread(imageFile)
plt.axis('off')
#plt.imshow(imgBGR)
#plt.show()

imgRGB=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB) # opencv는 채널 순서를 BGR 로 하지만, matlotlib은 RGB로 처리하기떄문에 변환해줌
plt.imshow(imgRGB)
plt.show()
