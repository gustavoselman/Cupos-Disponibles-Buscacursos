from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World! 😛</p>"

@app.route("/store")
def store():
    return redirect(url_for('index'))

@app.route("/consulta", methods=['GET', 'POST'])
def consulta():
    return 'Consulta tipo GET'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    return 'El id del post es: ' + post_id

@app.route('/lele', methods=['GET'])
def lele():
    print(request.form)
    return 'lele'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)  