from flask import Flask, render_template, request
import cv2
import numpy as np
import os

from keras.backend.tensorflow_backend import set_session
from keras.models import load_model
import tensorflow as tf

config = tf.ConfigProto(
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    # device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)


GTSR_model = load_model("GTSR_model_keras")
GTSR_model.predict(np.zeros((1, 48, 48, 3)))

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
	
@app.route('/predict', methods = ['GET', 'POST'])
def predict_image():
    if request.method == 'POST':
        print("info: ", request.files)
        f = request.files['file']
        f.save(f.filename)
        result = int(predict(f.filename))
        return render_template('./predict.html', result=result)

if __name__ == '__main__':
   app.run(debug = True)