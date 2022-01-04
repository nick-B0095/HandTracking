# HandTracking
with openCV

I studied with two youtube video.
##### https://youtu.be/NZde8Xt78Iw 
##### https://youtu.be/p5Z_GGRCI5s

This is definitely informative! but there were some problems.
(It's not the video is wrong, just time has passed. so some module is changed.)


**Please check it.**
1. What is your version of python? mediapipe does not work in python 3.10 (at 21.11.18) so you use a lower version in python.

2. Hands function in mediapipe has more arguments so now we have to write this. working.
```python
self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)
```
