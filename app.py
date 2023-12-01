from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/curtca/')
def curtca():
    return render_template('curtca.html')

@app.route('/obuv/')
def obuv():
    return render_template('obuv.html')

if __name__ == '__main__':
    app.run(debug=True)
