import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response
from functools import wraps, update_wrapper
from werkzeug.utils import secure_filename
from werkzeug.http import http_date
from datetime import datetime

import stega
import algo

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/decode")
def decode():
    return render_template("decode.html")

@app.route("/encode")
def encode():
    return render_template("encode.html")

@app.route("/updateEncode", methods = ['POST'])
def updateEncode():
    UPLOAD_FOLDER = "static/images"

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        file = request.files['input']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename("Cristi2.png")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("success.html")
    else:
        return render_template("error.html")

@app.route("/updateDecode", methods = ['POST'])
def updateDecode():
    UPLOAD_FOLDER = "static/images"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        file = request.files['input']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename("Cristi2.png")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_address = UPLOAD_FOLDER + "/" + "Cristi2.png"
            text = stega.decode(image_address)
            opt = text.split(" -")
            if opt[0] == "-c":
                delay = opt[1]
                text = opt[2]
                text = algo.caesarDecode(text, int(delay))
                return render_template("finalDecode.html", text = text)
            if opt[0] == "-v":
                delay = opt[1]
                text = opt[2]
                text = algo.vigenereDecode(text, delay)
                return render_template("finalDecode.html", text = text)
            else:
                return render_template("finalDecode.html", text = text)
    else:
        return render_template("error.html")

@app.route("/final", methods = ['POST'])
def finalEncode():
    address = "static/images/Cristi2.png"
    UPLOAD_FOLDER = "static/images"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        text = request.form['text']
        cipher = request.form['crypto']

        if(cipher == 'vigenere'):
            delay = request.form['delay']
            text = "-v " + "-" + delay + " -" + text
            text = algo.vigenereEncode(text,delay)
        if(cipher == 'caesar'):
            delay = request.form['delay']
            text = "-c " + "-" + delay + " -" + text
            text = algo.caesarEncode(text,int(delay))
        newimg = stega.encode(address, text)
        new_img_name = "encoded.png"
        newimg.save(os.path.join(app.config['UPLOAD_FOLDER'], new_img_name))
        os.remove(address)
        return render_template("finalEncode.html")
    else:
        return render_template("error.html")

@app.route("/walkThrough")
def walkThrough():
    return render_template("walkThrough.html")

if __name__ == "__main__":
    app.run(debug=True)
