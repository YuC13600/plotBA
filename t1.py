import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("orivid.webm")
total_frames = cap.get(7)
print(f"frames: {total_frames}")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"size: {width}x{height}")
fps = cap.get(5)
print(f"{fps} fps")

print(f"cv2.CAP_PROP_POS_FRAMES: {cv2.CAP_PROP_POS_FRAMES}")

for current_frame in range(0, 300):
    print(f"current frame:{current_frame}")

    cap.set(1, current_frame)
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # print(gray)

    x = range(0, int(width))
    y = range(int(height)-1, -1, -1)
    X, Y = np.meshgrid(x, y)
    # print(X)
    # print(Y)

    plt.contourf(X, Y, gray)
    img_name = str(current_frame) + "testing.jpg"
    plt.savefig(img_name)

frame_list = []
first_img = cv2.imread("0testing.jpg")
height, width, _ = first_img.shape
size = (width, height)
for current_frame in range(0, 300):
    filename = str(current_frame) + 'testing.jpg'
    img = cv2.imread(filename)
    frame_list.append(img)

out = cv2.VideoWriter('testing.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for frame in frame_list:
    out.write(frame)
out.release()
