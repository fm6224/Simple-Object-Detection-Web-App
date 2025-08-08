# test_yolov8.py
import os
from flask import (
    Flask, 
    request,
    render_template,
    url_for, 
    redirect
)

from werkzeug.utils import secure_filename
from ultralytics import YOLO

import cv2


# Configuration
UPLOAD_FOLDER = 'static/uploads/'
RESULTS_FOLDER = 'static/results/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB max upload size

# ensure the upload and results directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

# load a pre-trained YOLOv8 model
# we load the model once when the application starts for efficiency
model = YOLO('yolov8n.pt') # 'n' for nano model

def allowed_file(filename):
    """Check if the file's extension is in allowed set."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_detect():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        # if the used deos not select a file, the browser submits an empty file
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # sanitize the file name to prevent security issues
            filename = secure_filename(file.filename)
            original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result_filepath = os.path.join(app.config['RESULTS_FOLDER'], filename)

            # save the uploaded file
            file.save(original_filepath)
            # perfrom detection
            # the model returns a list of results object
            results = model(original_filepath)
            # the plot() method returns a BGR numpy array with detections drawn on it
            res_plotted = results[0].plot()
            # save the resulting image using opencv
            cv2.imwrite(result_filepath, res_plotted)

            # pass the filename to the template to display the images
            return render_template('index.html', filename=filename)
    
    # for a get request, just display the upload form
    return render_template('index.html', filename=None)



if __name__ == '__main__':
    # the 'debug=True' option reloads the server automatically on code changes
    # and provides helpful error messages. Turn it off for production
    app.run(debug=True)