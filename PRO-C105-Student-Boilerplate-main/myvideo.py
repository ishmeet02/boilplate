import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")


if (vid.isOpened() == False):
    print("Unable to read the feed")


height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)



#cv2.VideoWriter(filename, fourcc, fps,frameSize, isColor)

output = cv2.VideoWriter('name.mp4',cv2.VideoWriter_fourcc(*'DIVX'),60,(width,height))


while True:
    ret, frame = vid.read()
    cv2.imshow("Web Cam", frame)

    output.write()

    if cv2.waitKey(25) == 32:
        break

vid.release()
output.release()

cv2.destroyAllWindows()