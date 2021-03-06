import cv2
from trackEvent import event_detection

cap = cv2.VideoCapture('kyle.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

writeVideo = False
count = 1
videos = []

out = cv2.VideoWriter('Answers\\laura\\Answer' + str(count) + '.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while True:

    _, frame = cap.read()
    #frame = cv2.resize(frame, (0,0), fx=1.1, fy=1.1)
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    #frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

    if cap.isOpened():
        fps = cap.get(cv2.CAP_PROP_FPS)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    cropped = event_detection(frame)

    if cropped:
        videos.append(frame)
        writeVideo = True
    else:
        if writeVideo and len(videos) > 20:
            out = cv2.VideoWriter('Answers\\laura\\Answer' + str(count) + '.mp4', fourcc, 20.0,
                                  (int(cap.get(3)), int(cap.get(4))))

            for images in videos:
               # images = cv2.rotate(images, cv2.ROTATE_180)
               # images = cv2.resize(images, (0, 0), fx=2.5, fy=2.5)
                out.write(images)
            print('Successfully created video for Answer ', count)
            videos = []
            count = count + 1
            writeVideo = False

    cv2.imshow('frame', frame)
    cv2.waitKey(10)

    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
