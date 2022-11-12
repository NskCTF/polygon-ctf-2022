from flask import Flask, render_template, render_template_string, request, redirect
import sqlite3 as sq
app = Flask(__name__)


@app.route("/", methods=['GET'])
def begin():
    return render_template("index.html")

@app.route("/admin", methods=['GET'])
def admin():
    return render_template("admin.html")

@app.route("/admin", methods=['POST'])
def login():
    login = request.form.get('login')
    passw = request.form.get('pass')
    con = sq.connect('db.db')
    db = con.cursor()
    feeds = db.execute(f"SELECT flag FROM users WHERE login = '{login}' AND password = '{passw}'")
    feed = feeds.fetchone()
    if feed:
        return render_template_string(f"<h1>{feed[0]}</h1>")
    else:
        return render_template_string(f"<h1>Неверный логин или пароль</h1>")
    con.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')


