import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/",methods=["GET"])
def home():
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method=="GET":
        #files=os.listdir("./upload/")
        #return render_template("list_maps.jinja",files=files)
        return redirect(url_for("home"))
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img' not in request.files:
            flash('No file part')
            return redirect(url_for("home"))
        file = request.files['img']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file.filename == '':
            flash('No selected file')
            return redirect(url_for("home"))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("index.html",img_url=f"/static/{filename}")



app.run(host="0.0.0.0", port=8080,debug=True)