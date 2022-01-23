import cv2
import HTM as htm
import numpy as np
import time, os

actions = ['rock', 'scissors', 'paper']
seq_len = 30
secs_for_action = 30

cap = cv2.VideoCapture(0)
detector = htm.handDetector()

created_time = int(time.time())
os.makedirs('dataset', exist_ok=True)


while cap.isOpened():
    for idx, action in enumerate(actions):
        data = []

        success, img = cap.read()

        cv2.putText(img, f'Waiting for collecting {action.upper()} action...', org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
        cv2.imshow('img', img)
        cv2.waitKey(3000) # 3 sec

        start_time = time.time()

        while time.time() - start_time < secs_for_action:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList, angleList, exist = detector.findPosition_Angle(img)

            if exist:
                angle_label = np.array([angleList], dtype=np.float32)
                angle_label = np.append(angle_label, idx)

                data.append(angle_label)
                # data.append(np.concatenate([lmList.flatten(), angle_label]))


            cv2.imshow('img', img)
            cv2.waitKey(1)

        data = np.array(data)
        print(action, data.shape)
        np.save(os.path.join('dataset', f'raw_{action}_{created_time}'), data)

        # seq_data = []
        # for seq in range(len(data) - seq_len):
        #     seq_data.append(data[seq:seq+seq_len])
        #
        # seq_data = np.array(seq_data)
        # print(action, seq_data.shape)
        # np.save(os.path.join('dataset', f'seq_{action}_{created_time}'), seq_data)

    break
