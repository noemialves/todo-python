from flask import Flask, request
from tasks import tasks

app = Flask(__name__)

@app.route('/list',methods=['GET'])
def get_tasks():
    return tasks

@app.route('/create', methods=['POST'])
def create_task():
    task = request.json
    return task


app.run(debug=True)