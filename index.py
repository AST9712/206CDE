from flask import Flask , render_template , request

app = Flask(__name__)

# this is the home
@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'route'

@app.route('/log_in')
def log_in():
    ''' log in user '''
    error = None
    user_name = request.form['username']
    user_pass = request.form['password']
    if request.method == 'POST':
        if valid_login(user_name,user_pass):
            return log_the_user_in(['username'])

    else:
        error = 'The Passwrd or Username is invalid'



    return render_template('templates/index.html',error = error)


@app.route('/upload', methods=['POST','GET'])
def upload_file():
    
    if request.method == 'POST': 
        f = request.files['the files']
        f.save['/var/upload/file/uploaded_files.txt']

    return render_template('upload_file.html')





if __name__ == '__main__':
    app.run()


