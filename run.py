from flask import Flask, render_template, request
import cv2
import numpy as np

from keras.models import load_model

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

@app.route('/upload')
def upload_file():
    return render_template('./upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def predict_image():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        result = int(predict(f.filename))
        return str(result)

if __name__ == '__main__':
   app.run(debug = True)