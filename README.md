# Emotion_detection_with_CNN

![image](https://github.com/Charmie1234/Group-Face-Emotion-Detection-using-Deep-Learning-/assets/136858550/78e57905-3d49-49a4-b8c3-f4de10a221a1)
![Screenshot (462)](https://github.com/Charmie1234/Group-Face-Emotion-Detection-using-Deep-Learning-/assets/136858550/55b782d5-ccbc-4a72-bac8-6b838fbf292d)


### Packages need to be installed
- pip install numpy
- pip install opencv-python
- pip install keras
- pip3 install --upgrade tensorflow
- pip install pillow

### download FER2013 dataset
- from below link and put in data folder under your project directory
- https://www.kaggle.com/msambare/fer2013

### Train Emotion detector
- with all face expression images in the FER2013 Dataset
- command --> python TranEmotionDetector.py

It will take several hours depends on your processor. (On i7 processor with 16 GB RAM it took me around 4 hours)
after Training , you will find the trained model structure and weights are stored in your project directory.
emotion_model.json
emotion_model.h5

copy these two files create model folder in your project directory and paste it.

### run your emotion detection test file
python TestEmotionDetector.py
