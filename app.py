from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="dist", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.errorhandler(404)
def not_found(_):
    return send_from_directory(app.static_folder, "index.html")
