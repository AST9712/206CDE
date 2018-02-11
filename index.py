from flask import Flask

app = Flask(__name__)

# this is the home
@app.route('/')
def index():
    return 'route'



if __name__ == '__main__':
    app.run()
