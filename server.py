from flask import Flask
import pymongo

app = Flask(__name__)


def openDatabase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    return mycol


def addUser(name):
    mydict = {"name": name, "address": "Highway 37"}
    x = mycol.insert_one(mydict)
    return


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/members")
def members():
    return "Members"


@app.route("/setmember/<string:name>/")
def addMember(name):
    addUser(name)
    return name


@app.route("/getmember")
def getMember():
    members = [];
    for member in mycol.find():
        print(member)
    return "hello"


if __name__ == "__main__":
    mycol = openDatabase()
    app.run(host='0.0.0.0', port=80)