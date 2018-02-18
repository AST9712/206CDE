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
    hey = 'hey'
    cc_names    = sorted(a.names())
    ccurrencies = a.rates()
    items = {
        'cc_names' : cc_names,
        'ccurrencies' : ccurrencies
    }
    print (type(ccurrencies))
    return render_template('index.html',items= items)

@app.route('/')
def graph():

    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    # output to static HTML file
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    # show the results
    k = show(p)
    return render_template('index.html',k = k)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



if __name__ == '__main__':
    app.run(debug=True)


