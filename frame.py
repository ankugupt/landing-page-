import cv2

cap = cv2.VideoCapture("capture.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

print (duration)
print (frame_count)

i=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%20==0 : 
       cv2.imwrite('frames/'+'kang'+str(i)+'.jpg',frame)
    i+=1
print (i)
 
cap.release()
cv2.destroyAllWindows()