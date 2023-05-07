import cv2
import cv2.gapi
import matplotlib.pyplot as plt
import numpy as np

model = cv2.dnn.readNetFromONNX("yolov7-tiny.onnx")
cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    image = cv2.resize(image, (640, 640))
    data = cv2.dnn.blobFromImage(image, 1, (640, 640))
    data = data / 255
    model.setInput(data)
    output = model.forward('output')
    output.resize(25200, 7)
    output = output[output[:, 4] > 0.6]
    ind = np.argmax(output[:, 5:], axis=1)
    m = output[np.arange(output.shape[0]), ind + 5]
    output[:, 5] = ind
    output[:, 4] *= m
    output[:, 0] -= output[:, 2]
    output[:, 1] -= output[:, 3]
    i = cv2.dnn.NMSBoxes(output[:, :4], output[:, 4], 0.6, 0.8)
    for j in i:
        cv2.rectangle(image, output[j, :4].astype(np.uint8), (0, 0, 0), 3)
    cv2.imshow("camera", image)
    print(1)