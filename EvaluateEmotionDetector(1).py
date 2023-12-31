# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-07-10 21:26:46
# @Last Modified by:   Your name
# @Last Modified time: 2023-07-12 09:48:08

import numpy as np
from keras.models import model_from_json
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report,ConfusionMatrixDisplay


emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
#json_file = open('C:\Users\DELL\Downloads\Emotion_detection_with_CNN\Emotion_detection_with_CNN-main\model\emotion_model(1).json', 'r')
json_file = open(r'C:\\Users\\DELL\\Downloads\\Emotion_detection_with_CNN\\Emotion_detection_with_CNN-main\\model\\emotion_model(1).json', 'r')

loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("C:\\Users\\DELL\\Downloads\\Emotion_detection_with_CNN\\Emotion_detection_with_CNN-main\\model\\emotion_model(1).h5")
print("Loaded model from disk")

# Initialize image data generator with rescaling
test_data_gen = ImageDataGenerator(rescale=1./255)

# Preprocess all test images
test_generator = test_data_gen.flow_from_directory(
        'C:\\Users\\DELL\\Downloads\\archive (4)\\test',
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

# do prediction on test data
predictions = emotion_model.predict_generator(test_generator)

# see predictions
# for result in predictions:
#     max_index = int(np.argmax(result))
#     print(emotion_dict[max_index])

print("-----------------------------------------------------------------")
# confusion matrix
c_matrix = confusion_matrix(test_generator.classes, predictions.argmax(axis=1))
print(c_matrix)
cm_display = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=emotion_dict)
cm_display.plot(cmap=plt.cm.Blues)
plt.show()

# Classification report
print("-----------------------------------------------------------------")
print(classification_report(test_generator.classes, predictions.argmax(axis=1)))




