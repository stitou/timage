import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tif'])

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def median():
    print "Median filter runing"
    os.system("python scriptFilters/median.py static/uploads/girlface.png")

fofo = ''
@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global fofo
            fofo = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    else:
        print fofo
        median()
    return render_template('index.html')



'''
@app.route('/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    if request.method == 'POST':
        if 'MedianOK' in request.form:
            os.system("python scriptFilters/median.py uploads/"+filename+"")
        if 'ConvolutionOK' in request.form:
            print "Convolution"
    return render_template('index.html', filename=filename)
'''

'''
@app.route('/uploadajax/<filename>')
def send_file(filename):
    print 'send_file filename ==> ',filename
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/<filename>', methods=['GET', 'POST'])
def upload_ajax(filename):
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
    if request.method == 'GET':
        return render_template('index.html', filename=filename)
'''

if __name__ == '__main__':
    app.run(debug=True)
