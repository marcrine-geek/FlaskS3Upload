import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import list_files, upload_file, show_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
# UPLOAD_FOLDER = "uploads"
BUCKET = "anothertrialbucketdamn"

@app.route("/")
def home():
    contents = list_files(BUCKET)
    return render_template('index.html')

@app.route("/pics")
def list():
    contents = show_image(BUCKET)
    return render_template('collection.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                upload_file(
                    filename,
                    BUCKET
                )
                
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    