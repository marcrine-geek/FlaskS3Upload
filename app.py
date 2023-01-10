import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import list_files, upload_file, show_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
# UPLOAD_FOLDER = "uploads"
import boto3

s3 = boto3.client('s3',
                    aws_access_key_id='AKIARKSJ3WF3JY6MCM6Q',
                    aws_secret_access_key= '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'
                     )
BUCKET = "washwashbucket"

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
                # img.save(filename)
                s3.upload_file(
                    filename,
                    BUCKET,
                    Key = filename
                )
                
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    