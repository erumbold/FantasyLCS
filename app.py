from flask import Flask
from models import Schema
from service import ToDoService

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=["GET"])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/<name>')
def hello_name(name):
    return "hello " + name

@app.route('/todo', methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

if __name__ == '__main__':
    Schema()
    app.run()
