from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)


@app.route('/')
def home():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        ssql="select * from task"
        cus.execute(ssql)
        data=cus.fetchall()
        db.commit()
        print(data)
        return render_template('dashboard.html',d=data)
    except Exception:
        print("The error is",Exception)
    

@app.route('/form')
def fm():
    return render_template('form.html')
    
@app.route('/store',methods=['POST'])
def store():
    t=request.form['title']
    dt=request.form['detail']
    d=request.form['date']
    #return t+dt+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        insql="insert into task (name,detail,date) values('{}','{}','{}')".format(t,dt,d)
        cus.execute(insql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)

@app.route('/delete/<rid>')
def delete(rid):
    #return "Id is"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        dsql="delete from task where id={}".format(rid)
        cus.execute(dsql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)
@app.route('/edit/<rid>')
def edit(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cu=db.cursor()
        sql="select * from task where id= '{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
        
    except Exception as e:
        print("Error:",e)
 
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    #return "ID to be  update in db is:"+rid
    t=request.form['title']
    dt=request.form['detail']
    d=request.form['date']
    #return t+dt+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cu=db.cursor()
        sql="update task SET name='{}',detail='{}',date='{}' where id='{}'".format(t,dt,d,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

    


app.run(debug=True)
