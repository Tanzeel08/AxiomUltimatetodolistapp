from flask import Flask,redirect,request,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME']='tanzo'
app.config['MONGO_URI']="mongodb+srv://Imran_riaz_chohan:Audionic123@cluster0-k8jot.mongodb.net/tanzo"
mongo = PyMongo(app)
@app.route("/todo/api/v1.0/tasks",methods=["POST"])
def PostFramework():
	framework=mongo.db.framework
	id=int(request.json['id'])
	description=request.json['description']
	title=request.json['title']
	done=bool(request.json['done'])
	framework_id=framework.insert({'id' :id, 'description' : description, 'title' : title, 'done': done })
	find_id=framework.find_one({"_id":framework_id})
	output={'id':find_id['id'],'description':find_id['description'],'title':find_id['title'],"done":find_id['done']}
	

	return jsonify({'result':output})
@app.route("/todo/api/v1.0/tasks",methods=["GET"])
def GetFramework():
	framework=mongo.db.framework
	results = []
	for a in framework.find():
		results.append({"id":a["id"],"description":a["description"],"title":a["title"],"Done":a["done"]})
	return jsonify({"RESULT":results})
@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["GET"])
def GetSpecificFramework(task_id):
	framework=mongo.db.framework
	find=framework.find_one({"id":task_id})
	if find:
		data={"id":find['id'],"description":find['description'],"title":find["title"],"Done":find["done"]}
	else:
		data="No record found"
	return jsonify({"result":data}) 
@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["delete"])
def deleteItem(task_id):

	framework=mongo.db.framework
	dat_find_one=framework.find_one({"id":task_id})
	if not dat_find_one:
		return jsonify({"result":"NOT FOUND"})
	else:
		framework.remove(dat_find_one,True)		
	
	return jsonify({"Result":"Item successfully removed! "})
@app.route("/todo/api/v1.0/tasks/<int:tasks_id>",methods=['PUT'])
def UPDATE(tasks_id):
    framework=mongo.db.framework
    item=framework.find_one({"id":tasks_id})
    if not item:
        return jsonify({"result":"not found"})
    else:
        item['id']=tasks_id 
        item['description']=request.json['description']
        item['title']=request.json['title']
        item['done']=bool(request.json['done'])
        item.save(data)    
    return jsonify({"Result":'updated'})  
if __name__ == '__main__':
	app.run(debug=True)


