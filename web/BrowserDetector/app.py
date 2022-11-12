from flask import Flask, render_template_string, request, redirect
import subprocess, os
app = Flask(__name__)

subprocess.Popen("echo 1", shell=True)

@app.route("/", methods=['GET'])
def begin():
    ua = request.headers.get('User-Agent')
    return render_template_string(f"<label>Your browser is: { ua } </label>")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


