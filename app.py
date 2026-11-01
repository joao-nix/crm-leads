from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "CRM de leads funcionando!"

@app.route("/sobre")
def sobre():
    return "Sobre funcionando"


if __name__ == "__main__":
    app.run(debug=True)



