from flask import Flask, request
import os
app = Flask(__name__)
@app.route("/ping")
def ping():
    hote = request.args.get("hote")
    os.system("ping -c 1 " + hote)
    return "ok"