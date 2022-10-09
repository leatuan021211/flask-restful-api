from flask import Blueprint
from .services import add_item_service, get_item_by_id_service, get_all_items_service, update_item_by_id_service, delete_item_by_id_service

items = Blueprint("items", __name__)

# create item
@items.route("/item", methods=["POST"])
def add_item():
    return add_item_service()

# get all items
@items.route("/items", methods=["GET"])
def get_all_items():    
    return get_all_items_service()

# get item by id
@items.route("/item/<int:id>", methods=['GET'])
def get_item_by_id(id):
    return get_item_by_id_service(id) 

# update item by id
@items.route("/item/<int:id>", methods=['PUT'])
def update_item_by_id(id):
    return update_item_by_id_service(id) 

# delete item by id
@items.route("/item/<int:id>", methods=['DELETE'])
def delete_item_by_id(id):
    return delete_item_by_id_service(id) 