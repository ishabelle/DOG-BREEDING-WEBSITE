from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = (os.urandom(16))

# INDEX PAGE


@app.route("/")
def index_page():
    return render_template("index_page.html")


# EN MAIN PAGE


@app.route("/en_main_page")
def en_main_page():
    return render_template("en_main_page.html")


@app.route("/en_news")
def en_news():
    return render_template("en_news.html")


@app.route("/en_exhibitions")
def en_exhibitions():
    return render_template("en_exhibitions.html")


@app.route("/en_breeding_bitches")
def en_breeding_bitches():
    return render_template("en_breeding_bitches.html")


@app.route("/en_litters")
def en_litters():
    return render_template("en_litters.html")


@app.route("/en_contact")
def en_contact():
    return render_template("en_contact.html")


@app.route("/en_about_us")
def en_about_us():
    return render_template("en_about_us.html")


@app.route("/en_about_breed")
def en_about_breed():
    return render_template("en_about_breed.html")


# PL MAIN PAGE


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


@app.route("/pl_about_us")
def pl_about_us():
    return render_template("pl_about_us.html")


@app.route("/pl_about_breed")
def pl_about_breed():
    return render_template("pl_about_breed.html")

# EN LITTERS


@app.route("/en_litter_b")
def en_litter_b():
    return render_template("en_litter_b.html")


@app.route("/en_litter_a")
def en_litter_a():
    return render_template("en_litter_a.html")


@app.route("/en_litter_m")
def en_litter_m():
    return render_template("en_litter_m.html")


@app.route("/en_litter_n")
def en_litter_n():
    return render_template("en_litter_n.html")


@app.route("/en_litter_j")
def en_litter_j():
    return render_template("en_litter_j.html")


# EN BREEDING BITCHES

@app.route("/en_salma")
def en_salma():
    return render_template("en_salma.html")


@app.route("/en_zoja")
def en_zoja():
    return render_template("en_zoja.html")


@app.route("/en_jaga")
def en_jaga():
    return render_template("en_jaga.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(
        host='localhost',
        port=5000,
        debug=True,
    )
