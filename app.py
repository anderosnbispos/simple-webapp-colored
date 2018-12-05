import os
from flask import Flask

app = Flask(__name__)

from flask import render_template

color = os.environ.get('APP_COLOR')

@app.route("/")
def main():
    print(color)
    return render_template('hello.html', color=color)

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', color=new_color)

if __name__ == "__main__":
    app.run()
