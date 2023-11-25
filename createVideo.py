import os
import cv2

path = "C:/Users/rajen/Downloads/PRO-C105-Project-Images-main/PRO-C105-Project-Images-main/Images"

images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+'./'+file

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)

out = cv2.VideoWriter('friends.mp4',cv2.VideoWriter_fourcc(*'DIVX'),2,size)

for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("done")