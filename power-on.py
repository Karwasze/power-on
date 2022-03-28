from flask import Flask, render_template, request
import subprocess
import os
app = Flask(__name__)

MAC_ADDRESS = os.getenv('MAC_ADDRESS', "not_specified")
if MAC_ADDRESS == "not_specified":
    print("Please provide environment variable MAC_ADDRESS as described in the README.md")
    exit(1)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('power-on') == 'Power on!':
            subprocess.call(['sudo', 'etherwake', '-i', 'eth0', MAC_ADDRESS])
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")
