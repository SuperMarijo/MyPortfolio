from flask import Flask, render_template

app = Flask  (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Fakebook")
def fakebook():
    return render_template("Fakebook_index.html")

@app.route("/Boogle")
def boogle():
    return render_template("Boogle_index.html")

@app.route("/WebPage")
def webpage():
    return render_template("WebPage_index.html")

if __name__ == '__main__':
    app.run(use_reloader=True)
