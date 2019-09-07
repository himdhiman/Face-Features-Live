import cv2
from mtcnn.mtcnn import MTCNN

camera = cv2.VideoCapture(0)
detector = MTCNN()

while True:

    ret, image = camera.read()

    if ret == False:
        continue

    result  = detector.detect_faces(image)

    try:

        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']

        image = cv2.rectangle(image, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]), (0,155,255), 2)

        image = cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        image = cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        image = cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        image= cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        image = cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

    except:
        pass


    cv2.imshow("Features",image)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
    
