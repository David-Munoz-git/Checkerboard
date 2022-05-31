from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', width = 8, length = 8)

@app.route('/4')
def eightbyfour():
    return render_template('index.html', width = 8, length = 4)

@app.route('/<int:width>/<int:length>')
def custom_checkerboard(width, length):
    return render_template('index.html', width = width, length = length)


if __name__=="__main__":
  app.run(debug=True) 