from flask import Flask, render_template , request, url_for
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=['GET', 'POST'])
def create():
    myid = str(uuid.uuid1()) 
    print(f'uuid= {myid}')
    
    if request.method == 'POST':
        print(request.files.keys())
        
        form_id = request.form.get('myid')
        print(form_id)
        
        desc = request.form.get('text')
        print(desc)
        
        for key, value in request.files.items():
            print(f'key = {key} , value = {value}')
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                folder_path = os.path.join(app.config['UPLOAD_FOLDER'], form_id)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                file.save(os.path.join(folder_path, filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], form_id, "desc.txt"), "w") as f:
                f.write(desc)
    
    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)