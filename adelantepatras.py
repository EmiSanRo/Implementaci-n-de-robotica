import cv2
cap=cv2.VideoCapture(0) #Abre la camara
#tamaño de la imagen
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer=cv2.VideoWriter('videitonormalito.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20,(width,height)) #el 20 es a cuantos frames
while True:
    ret,frame=cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    writer.write(frame)
    cv2.imshow('frame',frame)
cap.release()
writer.release()cap2=cv2.VideoCapture(r"videitonormalito.mp4")
#obtener frames
check, vid = cap2.read()
frame_list=[]
while(check==True):
    check,vid=cap2.read()
    frame_list.append(vid)
frame_list.pop()
frame_list.reverse()
writer2=cv2.VideoWriter('videitoreverso.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20,(width,height)) #el 20 es a cuantos frames

for frame in frame_list:
    writer2.write(frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap2.release()
writer2.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()

capnat = cv2.VideoCapture("videitonormalito.mp4")
caprev = cv2.VideoCapture("videitoreverso.mp4")

width = int(capnat.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capnat.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('videocompleto.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height)) # el 20 es a cuantos frames

while True:
    ret, frame = capnat.read()
    if not ret:
        break
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

while True:
    ret, frame = caprev.read()
    if not ret:
        break
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capnat.release()
caprev.release()
writer.release()
cv2.destroyAllWindows()