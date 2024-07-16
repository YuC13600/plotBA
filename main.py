# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 2022

@author: YuC13600

這個作品是第8次作業的升級版，先前是在C++程式中使用Opencv讀出相片的值再人工複製貼上到Python程式碼中。
這次則是把Opencv的部分整合進Python，並將輸入的檔案從圖片升級為影片，將每一張plot存檔成jpg之後再變回影片。
雖然這個程式在我的電腦順利跑完了，但放到colab上就沒辦法執行了，請見諒。
不建議在自己的電腦執行，因為我的電腦跑了10小時才完成。

原影片:https://www.youtube.com/watch?v=FtutLA63Cp8
"""
#%%

import cv2
import numpy as np
import matplotlib.pyplot as plt

#讀入影片檔並計算total frame和圖片的尺寸
cap = cv2.VideoCapture("orivid.webm")
total_frames = cap.get(7)
print(total_frames)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size:%d"%(width*height))

#將每一幀轉成灰階之後讀出值，再用pyplot畫出圖表並存檔
for j in range(0, int(total_frames)-3):
    print("Plot Processing... %f%s"%(j/total_frames*100,'%'))
    cap.set(1, j) # 1 = cv2.CAP_PROP_POS_FRAMES
    _, frame = cap.read()
    # cv2.imwrite("outimg.jpg", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # print(gray)

    x = range(0, int(width))
    y = range(int(height)-1, -1, -1)
    X, Y = np.meshgride(x, y)

    plt.contourf(X, Y, gray)
    img_name = str(j)+'out.jpg'
    plt.savefig(img_name)
    # print(x)
    # print(y)

#將每一張plot復原成影片
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
out.release()
# %%
