import os
import cv2
import numpy as np
import tensorflow as tf

from keras.models import load_model
from flask import Flask, render_template, request
from get_sign import get_sign


GTSR_model = load_model("GTSR_model_keras")
GTSR_model.predict(np.zeros((1, 48, 48, 3)))
info = get_sign()


def predict(image):
    src = cv2.imread(image)
    src = cv2.resize(src, (48, 48))
    src = np.reshape(src, (1, 48, 48, 3))

    y = GTSR_model.predict(src, steps=1)
    result = np.argmax(y)

    return result


app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('./upload.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_image():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        result = int(predict(f.filename))
        return render_template('./predict.html', result=info[result])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
