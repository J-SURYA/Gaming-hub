from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(id varchar(20) PRIMARY KEY NOT NULL,name varchar(50) NOT NULL,email varchar(50) NOT NULL,dob date NOT NULL,password varchar(50) NOT NULL)')

    if request.method == 'POST':
        
        inc1 = request.form.get('id')
        inc2 = request.form.get('name')
        inc3 = request.form.get('email')
        inc4 = request.form.get('dob')
        inc5 = request.form.get('password')
        c.execute("SELECT * FROM users WHERE id=?",(inc1,))
        data=c.fetchone()
        if data:
            err="User id already exists..."
            return render_template('signup.html',error=err)
        else:
            sql_query = "INSERT INTO users (id,name,email,dob,password) VALUES (?,?,?,?,?)"
            c.execute(sql_query, (inc1,inc2,inc3,inc4,inc5))
            conn.commit()
            c.close()
            return redirect('/home')
    return render_template("signup.html")

@app.route('/history')
def accounts():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()
    c.execute("SELECT * FROM users")
    rows=c.fetchall()
    c.close()
    return render_template("accounts.html",accounts=rows)

@app.route('/')
def startup():
    return render_template("startup.html")
 
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/signin',methods=['GET','POST'])
def signin():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()
    if request.method == 'POST':
        name = request.form.get('id')
        passw = request.form.get('password')
        c.execute("SELECT * FROM users WHERE id=? AND password=?",(name,passw))
        data=c.fetchone()
        c.close()
        if data:
            return redirect('/home')
        else:
            err="Invalid user access..."
            return render_template('signin.html',error=err)
    return render_template("signin.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/mainfile')
def mainfile():
    
    return render_template("mainfile.html")

@app.route('/change')
def change():
    return render_template("change.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/memorygame')
def memorygame():
    return render_template("mem.html")

@app.route('/tictactoe')
def tictactoe():
    return render_template("tic.html")

@app.route('/snakegame')
def snakegame():
    return render_template("snake.html")

@app.route('/memjs')
def memjs():
    return render_template("mem.js")

@app.route('/memcss')
def memcss():
    return render_template("mem.css")

@app.route('/ticjs')
def ticjs():
    return render_template("tic.js")

@app.route('/ticcss')
def ticcss():
    return render_template("tic.css")

@app.route('/snakejs')
def snakejs():
    return render_template("snake.js")

if __name__ == '__main__':
    app.run(debug=True)
