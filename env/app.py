
from flask import Flask, flash, get_flashed_messages, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)
app.secret_key='1234'

##### cretion de la base de donnée ########
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTERGER,
    bat1 INTERGER,
    bat2 INTERGER,
    bat3 INTERGER,
    bat4 INTERGER,
    hall INTERGER )""")
conn.commit()



@app.route('/')
def index():
    return render_template("accueil.html")

@app.route('/connexion',methods = ['POST','GET'])
def connexion():
    return render_template("connexion.html")


@app.route('/connect',methods = ['POST'])
def connect():
    
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    #recuperation des informations du form
    global p
    global a
    
    """if int(request.form['age']) :
        flash("L'âge ou le nombre n'est pas valide",'error')
        return redirect(url_for('.connexion'))"""
    p = request.form['nom']
    a = int(request.form['age'])

    #connexion à la session du joueur si elle existe deja
    cursor.execute("""SELECT id, name, age, bat1, bat2, bat3, bat4, hall FROM user""")
    rows = cursor.fetchall()
    for row in rows:
        if row[1]==p and row[2]==a:
            return render_template("carte.html", pseudo=p,age=row[2],bat1=row[3],bat2=row[4],bat3=row[5],bat4=row[6],hall=row[7])

    cursor.execute(""" INSERT INTO user(name,age,bat1,bat2,bat3,bat4,hall) VALUES(?,?,0,0,0,0,0) """,(p,a))
    conn.commit()
    
    conn.close()
    return render_template("carte.html", pseudo=p)


        ####################
        #### Batiment 1 ####
        ####################
@app.route('/bat1', methods=['POST','GET'])
def bat1():
    global p
    global a
    image_file=url_for('static', filename='images/test_pnj.PNG')
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user SET bat1=100 WHERE name=? and age=? """,(p,a))
    conn.commit()
    
    return render_template("bat1.html",image_file=image_file)


        ####################
        #### Batiment 2 ####
        ####################
@app.route('/bat2', methods=['POST','GET'])
def bat2():
    global p
    global a
    image_file=url_for('static', filename='images/test_pnj.PNG')
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user SET bat2=100 WHERE name=? and age=? """,(p,a))
    conn.commit()
    
    return render_template("bat2.html",image_file=image_file)


        ####################
        #### Batiment 3 ####
        ####################
@app.route('/bat3', methods=['POST','GET'])
def bat3():
    global p
    global a
    image_file=url_for('static', filename='images/test_pnj.PNG')
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user SET bat3=100 WHERE name=? and age=? """,(p,a))
    conn.commit()
    
    return render_template("bat3.html",image_file=image_file)


        ####################
        #### Batiment 4 ####
        ####################
@app.route('/bat4', methods=['POST','GET'])
def bat4():
    global p
    global a
    image_file=url_for('static', filename='images/test_pnj.PNG')
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user SET bat4=100 WHERE name=? and age=? """,(p,a))
    conn.commit()
    
    return render_template("bat4.html",image_file=image_file)


        ####################
        ####### Hall #######
        ####################
@app.route('/hall', methods=['POST','GET'])
def hall():
    global p
    global a
    image_file=url_for('static', filename='images/test_pnj.PNG')
    #connexion à la base de donnée
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user SET hall=100 WHERE name=? and age=? """,(p,a))
    conn.commit()
    
    return render_template("hall.html",image_file=image_file)


"""if __name__=="__main__":
    website_url = 'ModesteTour.fr:5000'
    app.config['SERVER_NAME'] = website_url 
app.run(debug="True",host="0.0.0.0")"""
    