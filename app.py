from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = (os.urandom(16))


@app.route("/")
def index_page():
    return render_template("main_page.html")


@app.route("/en_main_page")
def en_main_page():
    return render_template("en_main_page.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/exhibitions")
def exhibitions():
    return render_template("exhibitions.html")


@app.route("/breeding_bitches")
def breeding_bitches():
    return render_template("breeding_bitches.html")


@app.route("/litters")
def litters():
    return render_template("litters.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/pl_main_page")
def pl_main_page():
    return render_template("pl_main_page.html")


@app.route("/pl_news")
def pl_news():
    return render_template("pl_news.html")


@app.route("/pl_exhibitions")
def pl_exhibitions():
    return render_template("pl_exhibitions.html")


@app.route("/pl_breeding_bitches")
def pl_breeding_bitches():
    return render_template("pl_breeding_bitches.html")


@app.route("/pl_litters")
def pl_litters():
    return render_template("pl_litters.html")


@app.route("/pl_contact")
def pl_contact():
    return render_template("pl_contact.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(
        host='localhost',
        port=5000,
        debug=True,
    )
