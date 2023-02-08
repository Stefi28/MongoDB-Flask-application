from flask import Flask, render_template, request
from utils import write_to_mongodb, mongodb_to_html


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/update_sql', methods=['GET', 'POST'])
def read_update_sql():
    if request.method == 'POST':
        if request.form['sqldb'] == "Update the SQL database":
            update_db()
            flash("Finished cleaning data!", "success")
            return render_template('index.html')


@app.route('/write_to_mongodb', methods=['GET', 'POST'])
def write_to_mongodb():
    write_to_mongodb()
    flash('Data has been written to MongoDB!' "success")
    return render_template('index.html')


@app.route('/mongodb_to_html', methods=['GET', 'POST'])
def mongodb_to_html():
     mongodb_to_html()
     flash('Show list of first twenty companies!')
     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)







