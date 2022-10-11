from distutils.log import error
from platform import java_ver
from urllib import request
from flask import Flask,jsonify,request

app=Flask(__name__)

#creatin an array of task with each as a different ogj in it

tasks=[
    {
        'id':1,
        'title':'buy groceries',
        'description':'milk,cheese,rice',
        'done': False
    },
    {
        'id':2,
        'title':'learn python',
        'description':'need to find a good python tutorial on web',
        'done': False 
    }
]
@app.route('/add_data',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            'status':"error",
            'msg':'pls provide the data'

        },400)

    task= {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done': False
    },

    tasks.append(task)
    return jsonify({
       'status':'success',
       'msg':'data added successfully' 
    })


@app.route('/get_data')
def get_task():
    return jsonify({
        'data':tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)