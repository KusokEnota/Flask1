from flask import Flask, request, render_template, redirect, url_for, make_response


app = Flask(__name__)
app.secret_key= '12345fffff'


app.static_url_path = '/static'

@app.route('/', strict_slashes=False)
@app.route('/index.html', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/odegda/', strict_slashes=False)
@app.route('/odegda.html/', strict_slashes=False)
def odegda():  # put application's code here
    return render_template('odegda.html')

@app.route('/vhod/', strict_slashes=False)
def vhod():
    return render_template('vhod.html')

@app.route('/obuv/', strict_slashes=False)
@app.route('/obuv.html/', strict_slashes=False)
def obuv():
    return render_template('obuv.html')

@app.route('/kurtka/')
def kurtka():
    return  render_template('kurtka.html')

@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('user_name', user_name)
        response.set_cookie('user_email', user_email)

        return response

@app.route('/welcome')
def welcome():
    user_name = request.cookies.get('user_name')
    return render_template('welcome.html', user_name=user_name)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')

    return response

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