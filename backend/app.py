from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client["mydb"]
collection = db["messages"]

@app.route("/api")
def get_message():
    collection.insert_one({"msg": "Hello from Backend!"})
    return jsonify({"message": "Hello from Flask Backend with MongoDB!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
