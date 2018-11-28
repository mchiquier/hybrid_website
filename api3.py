from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request, render_template, flash, redirect, url_for
from flask import send_from_directory, send_file
from werkzeug.utils import secure_filename
from scipy import misc
from scipy.misc import imsave
import numpy
from scipy import ndimage
import cv2
import time
import os
import random
import numpy as np
import string
from calculations import hybridImage
import random
from random import randint

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder='templates')
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'my unobvious secret key'
img1 = ''
img2 = ''
string = '' 

@app.route('/', methods=['GET'])
def home():
    images = os.listdir('static/images')
    first_r = randint(0,len(images)-1)
    second_r = randint(0,len(images)-1)
    while first_r == second_r: 
        second_r = randint(0,len(images)-1)
    global img1
    global img2
    img1= images[first_r]
    img2 = images[second_r]
    highFreqImg = ndimage.imread("static/images/" + img1, flatten=True)
    lowFreqImg = ndimage.imread("static/images/" + img2, flatten=True)
    imsave("static/images/" +  img1 , highFreqImg)
    imsave("static/images/" +  img2  , lowFreqImg)
    hybrid = hybridImage('static/images/' + img1, 'static/images/' + img2, 10, 10)
    timestamp = time.time()
    imsave("static/temp/" + str(timestamp) + ".png",numpy.real(hybrid)) 
    return render_template("webpage3.html",file1=img1,file2=img2,file3="static/temp/" + str(timestamp) + ".png", file4 = str(random))
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/process', methods = ['GET', 'POST'])
def process():
    high_pass_threshold = request.form.get('highpassthresh')
    low_pass_threshold = request.form.get('lowpassthresh')
    print("?")
    print(high_pass_threshold)
    print(low_pass_threshold)
    images = os.listdir('static/images')
    highFreqPath = ''
    lowFreqPath = ''
  #  print(img1)
  #  global img1 
  #  global img2
    print("now")
    print(img2)
    print("now2")
    if request.method == 'POST':
        hybrid = hybridImage('static/images/' + img1, 'static/images/' + img2, int(high_pass_threshold), int(low_pass_threshold))
        sec = str(round(time.time() * 1000))+ ".png"
        misc.imsave("static/results/" + sec, numpy.real(hybrid))
    

        return "static/results/" + sec
    #return on the desk and then put it back out 

    return 'images/marilyn-einstein.png'
    #send_file('images/einstein.png')

@app.route('/final_submission', methods = ['GET', 'POST'])
def final_submission():
    print(request.args.get("a"))
    data = request.args.get("a").split(";")
    count = len(data)
    print(count, "Count")
    if len(data) > 2:
        with open("out.txt", 'a') as out:
            for elem in data:
                out.write(elem)
                out.write("\n")          
    if (count%5 == 0) and count > 0: 
        count = 0
        random = np.random.randint(0,99)
        count2 = 0
        randomstring = ''
        with open("randomtext.txt", 'r') as rand:
            for elem in rand:
                if count2 == random:
                    randomstring = elem 
                count2 += 1
        with open("out.txt", 'a') as out:
            out.write(str(randomstring) + "\n")
        return "Congratulations! You're done. Your code is:" + randomstring.rstrip().rstrip("\n")
    elif count < 0:
        count = 0
        return "You still have 5 pairs left"
    else:
        return "You still have " + str(5-count%5) + " pairs left"

app.run()
