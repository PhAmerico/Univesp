from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/produto')
def produto():

    return render_template('produto.html')



@app.route('/adicionar')
def adicionar():

    return render_template('adicionar.html')




if __name__ == '__main__':
    app.run(debug=True)