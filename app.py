from flask import Flask, render_template

app = Flask(__name__)

app.static_url_path = '/static'

@app.route('/', strict_slashes=False)
@app.route('/index.html', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/odegda/', strict_slashes=False)
@app.route('/odegda.html/', strict_slashes=False)
def odegda():  # put application's code here
    return render_template('odegda.html')


@app.route('/obuv/', strict_slashes=False)
@app.route('/obuv.html/', strict_slashes=False)
def obuv():
    return render_template('obuv.html')

@app.route('/kurtka/')
def kurtka():
    return  render_template('kurtka.html')

@app.route('/news/')
def news():
    _news = [
        {
            "title": "John1",
            "descr": "Doe",
            "date": 201
        },
        {
            "title": "John2",
            "descr": "Doe",
            "date": 202
        },
        {
            "title": "John3",
            "descr": "Doe",
            "date": 203
        },
    ]
    context = {'news': _news}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()