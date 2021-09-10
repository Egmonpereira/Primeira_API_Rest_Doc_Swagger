from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': "Guerra e Paz"},
    {'id': 1, 'title': "Código limpo"}
]

@api.route('/livros', methods = ['GET','POST','UPDATE','PATCH','PUT','DELETE'])
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self, ):
        return books_db

    @api.expect(book, valitade=True)
    @api.marshal_with(book)
    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200

    def update(self, ):
        pass
    
    def patch(self, ):
        pass    
    
    def put(self, ):
        pass    
    
    def delete(self, ):
        pass