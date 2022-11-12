from flask import Flask, render_template, request, redirect, render_template_string
import subprocess
app = Flask(__name__)

ban = ["sh ", "bash", "python", "socat"]

@app.route("/", methods=['GET'])
def begin():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def execute():
    cmd = request.form.get('cmd')
    if not any(x in cmd for x in ban):
        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return render_template("index.html")
    else:
        return render_template_string("sh/bash/python/socat are restricted")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


