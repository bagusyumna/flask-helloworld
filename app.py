from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'title':'Hello Page',
        'content':'HELLO WORLD!!'
    }
    return render_template('hello.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    