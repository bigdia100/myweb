from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>안녕! 내가 만든 첫 번째 웹사이트야!</h1>"

if __name__ == "__main__":
    app.run(debug=True)