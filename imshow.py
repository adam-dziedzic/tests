import cv2
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cwd = os.getcwd()
picture_path = "picture.jpg"
print("cwd: ", cwd)
path = os.path.join(cwd, '\picture.jpg')
# path = cwd + '\picture.jpg'
print("path: ", path)
print("last path: ", os.path.join(__location__, picture_path))
# img = cv2.imread(os.path.join(__location__, picture_path))

img = cv2.imread("picture.jpg", 0)
cv2.imshow('ImageWindow', img)
cv2.waitKey()