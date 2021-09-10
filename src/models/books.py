from flask_restplus import fields
from src.server.instance import server

book = server.api.model('Book', {
    'id': fields.String(description='O id do registro'),
    'title': fields.String(required=True, min_Lenght=1, max_Lenght=200, description='O titulo do livro')
})