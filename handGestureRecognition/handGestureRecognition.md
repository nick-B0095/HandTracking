# HandGestureRecognition
with openCV, sklean, keras ...

I studied with this video and code.
>##### https://www.youtube.com/watch?v=eHxDWhtbRCk&t=1s -손 제스처 인식 딥러닝 인공지능 학습시키기
>##### https://github.com/kairess/gesture-recognition
\
This video is using LSTM for training model on sequential actions.
But I want to train on stopped motions. So, I make some changes.

1. I'm not using LSTM but other ML model(date::22-1-24::Decision Tree). <br/>
And I can get good model enough :: accuracy_score(y_test_arg, y_pred_arg) # 0.98


2. I'm not using 3D dataset but 2D dataset. <br/>
You know, I don't have to collect sequential actions. So, I save data just about fingers' angles (only 12 parameters).


3. -1)I use other codes on calculate angles. <br/>
   -2)I use HTM(HandTrackingModule) and add codes about calculating angles.
