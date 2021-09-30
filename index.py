from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("registro.html", titulo = "titulo h1")

if __name__ == "__main__":
    app.run(debug=True)