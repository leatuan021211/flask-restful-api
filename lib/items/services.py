from lib.extension import db
from lib.item_marshmallow import ItemSchema
from lib.model import Items
from flask import request, jsonify

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

def add_item_service():
    data = request.json
    if data and ('name' in data) and ('amount' in data) and ('cost' in data):
        name = data['name']
        amount = data['amount']
        cost = data['cost']
        try:
            new_item = Items(name, amount, cost)
            db.session.add(new_item)
            db.session.commit()
            return jsonify({"message": "Add Successfully!"}), 200 
        except IndentationError: 
            db.session.rollback()
            return "Can not add item!", 400
    else:
        return jsonify({"message": "Request error!"}), 400
    
    
def get_item_by_id_service(id):
    item = Items.query.get(id)
    if item:
        return item_schema.jsonify(item), 200
    else:
        return jsonify({"message": "Not found!"}), 404
    

def get_all_items_service():
    items = Items.query.all()
    if items:
        return items_schema.jsonify(items), 200
    else:
        return jsonify({"message": "Not found!"}), 404
    

def update_item_by_id_service(id):
    item = Items.query.get(id)
    data = request.json
    if item:
        try:
            if 'amount' in data:
                item.amount = data['amount']
            if 'cost' in data:
                item.cost = data['cost']
            return item_schema.jsonify(item), 200
        except IndentationError: 
            db.session.rollback()
            return jsonify({"message": "Can not update item!"}), 400
    else:
        return jsonify({"message": "Not found!"}), 404
    

def delete_item_by_id_service(id):
    item = Items.query.get(id)
    if item:
        try:
            db.session.delete(item)
            db.session.commit()
            return "Deleted Item!", 200
        except IndentationError: 
            db.session.rollback()
            return jsonify({"message": "Can not delete item!"}), 400
    else:
        return jsonify({"message": "Not found!"}), 404