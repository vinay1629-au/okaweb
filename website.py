from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ye ra labbey</h1>
    <p>Python and Flask.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)