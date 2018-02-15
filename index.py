from flask import Flask , render_template
# from flask_mysqldb import MySQL
from data import Currencies


app = Flask(__name__)
# mysqsdl = MySQL(app) 



@app.route('/') #home page
def index():
    # cur = mysql.connection.cursor() 
    # cur.execute('''SELECT user, host FROM mysql.user''')
    # all_users = cur.fetchall()
    a = Currencies()
    s = a.names()
    return render_template('index.html', s = s)



if __name__ == '__main__':
    app.run()


