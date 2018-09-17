from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request, render_template, flash, redirect, url_for
from flask import send_from_directory, send_file
from werkzeug.utils import secure_filename
from scipy import misc
import numpy
import os
from calculations import hybridImage

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder='templates')
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'my unobvious secret key'


@app.route('/', methods=['GET'])
def home():
        return render_template("webpage.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/process', methods = ['GET', 'POST'])
def process():

    highFreqPath = ''
    lowFreqPath = ''
    if request.method == 'POST':
        highpassimg = request.files['highpassimg']
        print(highpassimg)
        highpassimg.save(secure_filename("static/images/" + highpassimg.filename))
        print("Saved1")
        lowpassimg = request.files['lowpassimg']
        print("Saved2 _ ")
        lowpassimg.save(secure_filename("static/images/" + lowpassimg.filename))
        print(lowpassimg)
        print(highpassimg)
        # Return output path here
        high_pass_threshold = request.form.get('highpassthresh')
        low_pass_threshold = request.form.get('lowpassthresh')
        print(high_pass_threshold)
        print(low_pass_threshold)
        hybrid = hybridImage(highpassimg, lowpassimg, int(high_pass_threshold), int(low_pass_threshold))
        print("cool")
        #hybrid.save(secure_filename("/static/results/output.png"))
        return '/static/results/ok.png'

    misc.imsave("images/marilyn-einstein.png", numpy.real(hybrid))
    #return on the desk and then put it back out 
    hybrid = hybridImage(file1, file2, int(high_pass_threshold), int(low_pass_threshold))

    return 'images/marilyn-einstein.png'
    #send_file('images/einstein.png')
if __name__ == '__main__':
    app.run(debug=False)