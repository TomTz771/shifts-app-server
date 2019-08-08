from flask import Flask
import pymongo
from werkzeug.wrappers import json

app = Flask(__name__)


def openDatabase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["users"]
    mycol = mydb["schedule"]
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


@app.route("/getScheduling")
def getScheduling():
    members_map = {}
    result = {}
    result = get_optimal_scheduling(list(mycol.find()), 0, members_map)
    return str(result)


def get_optimal_scheduling(members, index, members_map):
    if index >= len(members):
        return members_map
    max_len = -1
    max_map = {}
    for i in range(1, 4):
        # if member can be scheduled in this day
        if i.__str__() in members[index]['days'].split(','):
            print(members[index]['name'])
            print("is in day number:")
            print(i)
            members_map[members[index]['name']] = i

            result1 = get_optimal_scheduling(members, index + 1, members_map)
            print(str(result1))
            if map_values_length(result1) > max_len:
                max_len = map_values_length(result1)
                max_map = result1.copy()
            del members_map[members[index]['name']]
    return max_map

def map_values_length(members_map):
    items = members_map.items()
    list_of_values = list()
    for item in items:
        list_of_values.append(item[1])
    return len(set(list_of_values))


if __name__ == "__main__":
    mycol = openDatabase()
    app.run(host='0.0.0.0', port=80)