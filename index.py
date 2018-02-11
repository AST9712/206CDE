from flask import Flask , render_template

app = Flask(__name__)

# this is the home
@app.route('/')
def index():
    return 'route'

@app.route('/kwlos')
def something():
    if method == 'POST'
        return 'something'
    else:
        return 'else'

    return render_template('templates/index.html')


@app.route('/kwlos/moyni')

def something2():




if __name__ == '__main__':
    app.run()


