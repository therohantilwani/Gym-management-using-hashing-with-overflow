# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

from flask import Flask, render_template, request
from flask_session import Session


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

filename="gym.txt"
traversalfilename="gymtraversal.txt"
idfilename="gymid.txt"

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html")


@app.route('/newgymplan')
def newgymplan():
    return render_template("newgymplan.html")

@app.route('/adminviewgympage')
def adminviewgympage():
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    return render_template("adminviewgympage.html", rows=lines)

@app.route('/admingymdeletepage')
def admingymdeletepage():
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    return render_template("admingymdeletepage.html", rows=lines)

@app.route('/admindeletegympage1', methods=['GET'])
def admindeletegympage1():
    args = request.args
    id = args.get("id")
    print("Id : ", id)
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close();

    newlines=[]
    idlines=[]
    for line in lines:
        s=line.split(",")
        print(id,":", len(id), ":",  s[0],":", len(s[0]), ":", line)
        if(id!=s[0]):
            print("Not Equals")
            newlines.append(line)
            idlines.append(s[0]+"\n")

    print("New Lines : ")
    print(newlines)
    print("Id Lines : ")
    print(idlines)

    with open(filename,'w') as f:
        for line in newlines:
            f.writelines(line)
    f.close();

    with open(idfilename, 'w') as f:
        for line in idlines:
            f.writelines(line)
    f.close();

    return render_template("admingymdeletepage.html", rows=newlines)

@app.route('/admingymsearchpage')
def adminvotersearchpage():
    return render_template("admingymsearchpage.html", rows=[])

@app.route('/admingymsearchpage1', methods=['POST'])
def adminvotersearchpage1():
    if request.method == 'POST':
        id = request.form['id']
    print("Id : ", id)
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close();

    newlines=[]
    for line in lines:
        s=line.split(",")
        print(id,":", len(id), ":",  s[0],":", len(s[0]), ":", line)
        if(id==s[0]):
            print("Not Equals")
            newlines.append(s[0])
            newlines.append(s[1])
            newlines.append(s[2])
            newlines.append(s[3])
            newlines.append(s[4])
            newlines.append(s[5])
            newlines.append(s[6])

    print(newlines)
    return render_template("admingymsearchpage.html", rows=newlines)

@app.route('/adminupdategympage1', methods=['GET'])
def adminvoterupdatepage():
    args = request.args
    id = args.get("id")
    print("Id : ", id)
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    f.close();

    voterline=""
    for line in lines:
        s=line.split(",")
        print(id,":", len(id), ":",  s[0],":", len(s[0]), ":", line)
        if(id==s[0]):
            voterline = line

    f.close();
    s=voterline.split(",")
    return render_template("adminupdategympage1.html", id=s[0], gname=s[1], fname=s[2], lname=s[3], date=s[4], time=s[5], gender=s[6])

@app.route('/admingymupdatepage')
def gymupdatepage():
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    return render_template("admingymupdatepage.html", rows=lines)

@app.route('/opennotepad', methods=['POST'])
def opennotepad():
    if request.method == 'POST':
        choice = request.form['choice']

    if(choice=="Gym"):
        os.system(filename)
    elif (choice == "Id"):
        os.system(idfilename)
    else:
        os.system(traversalfilename)

    print("Choice : ", choice)
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    return render_template("adminviewgympage.html", rows=lines)

@app.route('/adminlogincheck', methods=['POST'])
def adminlogincheck():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
    print("Uname : ", uname, " Pwd : ", pwd);
    if uname == "admin" and pwd == "admin":
        return render_template("adminmainpage.html")
    else:
        return render_template("adminlogin.html", msg="UserName/Password is Invalid")


@app.route('/adminupdatevoterpage2', methods=['POST'])
def adminupdatevoterpage2():
    print("Update Gym Function")
    if request.method == 'POST':
        id = request.form['id']
        gname = request.form['gname']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        date = request.form['date']
        time = request.form['time']


        s = str(id) + "," + gname +  "," + firstname + "," + lastname + "," + date + "," + time + "," + gender;
        lines = []
        with open(filename) as f:
            lines = f.readlines()

        newlines = []
        for line in lines:
            print(f'line : {line}')
            x = line.split(",")
            if(x[0]==id):
                newlines.append(s+"\n")
            else:
                newlines.append(line)
        f.close();

        print("NewLines : ", newlines)

        with open(filename, 'w') as f:
            for line in newlines:
                f.writelines(line)

        f.close();
        return render_template("adminviewgympage.html", rows=newlines);


@app.route('/addnewgym', methods=['POST'])
def addnewgym():
    print("Add New Gym Function")
    if request.method == 'POST':
        planname = request.form['SI Number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        date = request.form['date']
        time = request.form['time']

        file_exists = os.path.exists(filename)

        print("File Exists : ", file_exists)

        if (file_exists == False):
            file = open(filename, "w")
            file.close();

        lines = []
        with open(filename) as f:
            lines = f.readlines()

        cnt = 0
        flag=True
        for line in lines:
            x = line.split(",")
            print(x[5] , " : ", date, " " , x[6] , " ", len(x[6]),  " : ", time, " ", len(time))
            if(x[4]==date and  x[5]==time):
                cnt=cnt+1
            if(cnt>=4):
                flag = False
                break
        if(flag):
            id = 0
            for line in lines:
                print(f'line : {line}')
                x = line.split(",")
                id = x[0]

            f.close();

            id=int(id)+1

            s = str(id) + "," + planname + "," + firstname + "," + lastname + "," + date + "," + time +","+ gender;
            print(s)
            with open(filename, 'a') as f:
                f.writelines(s+"\n")

            f.close();

            return render_template("newgymplan.html", msg="Gym Details Inserted Success");
        else:
            return render_template("newgymplan.html", msg="Batch is Full Not Inserted Success");

@app.route('/adminviewtraversalpage')
def adminviewtraversalpage():
    lines = []
    with open(traversalfilename) as f:
        lines = f.readlines()

    return render_template("adminviewtraversalpage.html", rows=lines)

@app.route('/adminmainpage')
def adminmainpage():
    return render_template("adminmainpage.html")

if __name__ == "__main__":
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
