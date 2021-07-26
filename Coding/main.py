# Program that enhances the quality of given photo
import numpy as np
import cv2

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result



imgsize = [617, 692]
photo = cv2.resize(cv2.imread('dude.png'), imgsize)

# CLAHE LAB section
lab = cv2.cvtColor(photo, cv2.COLOR_BGR2LAB)
lab_planes = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
lab_planes[0] = clahe.apply(lab_planes[0])
lab = cv2.merge(lab_planes)
bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


# FSRCNN Super resolution
sr = cv2.dnn_superres.DnnSuperResImpl_create()
path = "FSRCNN_x4.pb"
sr.readModel(path)
sr.setModel("lapsrn", 4)
superres = sr.upsample(bgr)
superres = cv2.resize(superres, imgsize)


# Increases saturation
hsvImg = cv2.cvtColor(superres,cv2.COLOR_BGR2HSV)
hsvImg[...,1] = hsvImg[...,1]*1.15
hsvImg[...,2] = hsvImg[...,2]*1.0
imgsat =cv2.cvtColor(hsvImg,cv2.COLOR_HSV2BGR)


# Gamma correction
gamma = 1.1
invgamma = 1.0/gamma
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, invgamma) * 255.0, 0, 255)
imggam = cv2.LUT(imgsat, lookUpTable)

# cartoon


total_color =3
img = color_quantization(imggam, total_color)
cv2.imshow('Stock and Modded', np.hstack([photo, img]))
cv2.waitKey(0)
cv2.destroyAllWindows()

