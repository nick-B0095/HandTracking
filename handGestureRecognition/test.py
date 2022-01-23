import cv2
import HTM as htm
import numpy as np
import os
import pickle

actions = ['rock', 'scissors', 'paper']

print(os.getcwd())
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)


detector = htm.handDetector()
cap = cv2.VideoCapture(0)

seq = []
action_seq = []
last_action = False

def isReliable(action_seq_set):
    if len(action_seq_set) == 1:
        return True
    return False

while cap.isOpened():
    success, img = cap.read()

    img = detector.findHands(img)
    lmList, angleList, exist = detector.findPosition_Angle(img)
    if exist:
        input = [angleList.astype(np.float32)]
        y_pred = model.predict(input)
        i_pred = int(np.argmax(y_pred))
        conf = model.predict_proba(input)[i_pred][-1, -1]

        if conf < 0.95:
            action_seq = []
            continue

        action = actions[i_pred]
        action_seq.append(action)

        if len(action_seq) > 5:

            this_action = '?'
            if isReliable(set(action_seq)):
                this_action = action
                action_seq = []
            else:
                action_seq = []

            cv2.putText(img, f'{this_action.upper()}',(400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
            last_action = this_action

    if last_action:
        cv2.putText(img, f'{last_action.upper()}',(400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)

    cv2.imshow('img', img)
    cv2.waitKey(1)
