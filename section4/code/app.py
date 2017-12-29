from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'diego'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# Normally we use a database
items = []

class Item(Resource):
    """
    Inherits from Resource class
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = filter(lambda x: x['name'] == name, items)
        return {'item': item[0]}, 200 if item else 404

    def post(self, name):
        if filter(lambda x: x['name'] == name, items):
            return {'message': "An item with name '%s' already exists." % name}, 400

        # If content type is not json this will give an error
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = filter(lambda x: x['name'] != name, items)
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = filter(lambda x: x['name'] == name, items)
        if not item:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item[0].update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
