from flask import Flask , render_template
# from flask_mysqldb import MySQL
from data import Currencies


app = Flask(__name__,static_folder="static")
# mysqsdl = MySQL(app)



@app.route('/') #home page
def index():
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT user, host FROM mysql.user''')
    # all_users = cur.fetchall()
    a = Currencies()
    cc_names    = sorted(a.names())
    ccurrencies = a.rates()
    items = {
        'cc_names' : cc_names,
        'ccurrencies' : ccurrencies
    }
    return render_template('index.html',items= items)

@app.route('/currencies/<int:name>')
def currencies():
    coinlist = CryptocompareMOD()
    coinlist = coinlist.coinlist()
    return coinlist


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404



if __name__ == '__main__':
    app.run(debug=True)





def test(*args):
    for i in args:
        print (i)


test(1,2,4,'test', 'goodmorning')