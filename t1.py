import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("orivid.webm")
total_frames = cap.get(7)
print(total_frames)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Video encoding...")
img_arr = []
size = 0
for i in range(40, int(total_frames)-53):
    filename = str(i)+'out.jpg'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_arr.append(img)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_arr)):
    out.write(img_arr[i])
out.release
