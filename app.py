from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def to_do_home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

