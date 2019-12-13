from flask import Flask,request,jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST'] = "remotemysql.com"
app.config['MYSQL_USER'] = "nQzk2musHT"
app.config['MYSQL_PASSWORD'] = "e1HaekGOP4"
app.config['MYSQL_DB'] = "nQzk2musHT"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql=MySQL(app)
def show(connect):
	connect.execute("SELECT *  FROM project")
	# header=[x[0]for x in connect.description]
	rv=connect.fetchall()
	connect.close()
	# output=[]
 #    for result in rv:
 #    	output.append(dict(zip(header,result)))
	return jsonify({"RESULT":rv})	
@app.route("/todo/api/v1.0/tasks",methods=["POST"])
def framework():
	connect=mysql.connection.cursor()
	id=int(request.json['id'])
	description=request.json['description']
	title=request.json['title']
	done=request.json['done']
	connect.execute(f"INSERT INTO project(id,description,title,done) VALUES ('{id}','{description}','{title}','{done}')")
	mysql.connection.commit()
	return show(connect)
@app.route("/todo/api/v1.0/tasks",methods=["GET"])
def GetFrameWork():
	connect=mysql.connection.cursor()
	connect.execute("SELECT * FROM project")
	a=connect.fetchall()
	connect.close()
	mysql.connect.commit()
	return jsonify({"RESULT":a})
@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["GET"])
def GetOneFrameWork(task_id):
	connect=mysql.connection.cursor()
	connect.execute("SELECT * FROM project WHERE id=%s",[task_id])
	a=connect.fetchall()
	connect.close()
	mysql.connect.commit()
	return jsonify({"RESULT":a})
@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["Delete"])
def DeleteFrameWork(task_id):
	connect=mysql.connection.cursor()
	connect.execute("DELETE From project WHERE id=%s",[task_id])
	mysql.connect.commit()
	
	return jsonify({"RESULT":"record is delete!"})
@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["PUT"])
def UpdateFrameWork(task_id):
	connect=mysql.connection.cursor()
	id=int(request.json['id'])
	description=request.json['description']
	title=request.json['title']
	done=request.json['done']
	connect.execute(f"UPDATE project SET id='{id}',description='{description}',title='{title}',done='{done}' WHERE id=%s",[task_id])
	mysql.connect.commit()
	return show(connect)
if __name__ == '__main__':
	app.run(debug=True)