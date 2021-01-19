# def print_hi(name):
#     # 영상인식 표현 예제
#     import cv2
#
#     imageFile = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy'
#     img = cv2.imread(imageFile)  # 컬러표현
#     img2 = cv2.imread(imageFile, 0)  # GrayScale 표현
#     cv2.imshow('Lenna color', img)
#     cv2.imshow('Lenna grayscale'.img2)
#
#     cv2.waitKey()
#     cv2.destroyAllWIndows()
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


import cv2
from matplotlib import pyplot as plt
path = 'C:\\Users\\user\\Desktop\\python\\OpenCV\\OpenCVStudy\\'

imgBGR1 = cv2.imread(path + 'lena.jpg')
imgBGR2 = cv2.imread(path + 'apple.jpg')
imgBGR3 = cv2.imread(path + 'baboon.jpg')
imgBGR4 = cv2.imread(path + 'orange.jpg')

imgBGR1 = plt.figure(imgBGR1,figsize=(6,6))
imgBGR2 = plt.figure(imgBGR2,figsize=(6,6))
imgBGR3 = plt.figure(imgBGR3,figsize=(6,6))
imgBGR4 = plt.figure(imgBGR4,figsize=(6,6))

imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)


fig, ax=plt.subplots(2,2,figsize = (10,10),sharey = True)
fig.canvas.set_window_title('Sample Pictures')

ax[0][0].axis('off')
ax[0][0].imshow(imgRGB1, aspect = 'auto')

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'auto')

ax[1][0].axis('off')
ax[1][0].imshow(imgRGB3, aspect = 'auto')

ax[1][0].axis('off')
ax[1][1].imshow(imgRGB4, aspect = 'auto')

plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, wspace = 0.05, hspace = 0.05)
plt.savefig(path + "0206.png", bbox_inches = 'tight')
plt.show()
