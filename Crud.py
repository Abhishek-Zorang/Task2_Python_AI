from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/myData_flask"
mongo = PyMongo(app)

@app.route('/')
def home():
    return "Hello"

@app.route('/add', methods=['POST'])
def add_document():
    data = request.get_json()
    result = mongo.db.collection.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/documents', methods=['GET'])
def get_documents():
    documents = mongo.db.collection.find()
    result = []
    for document in documents:
        document['_id'] = str(document['_id'])
        result.append(document)
    return jsonify(result), 200

@app.route('/update/<id>', methods=['PUT'])
def update_document(id):
    data = request.get_json()
    mongo.db.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Updation Complete"}), 200

@app.route('/delete/<id>', methods=['DELETE'])
def delete_document(id):
    mongo.db.collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Deletion complete"}), 200

if __name__ == '__main__':
    app.run(debug=True)
