from flask import Flask
from flask.helpers import url_for
from flask_restplus import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0.0 09-09-2021',
            title='API Programação WEB',
            description='Api como Requisito da disciplina de Programação WEB  - Prof. Aléssio - Cefet/MG - Timóteo',
            contact='Egmon',
            contact_email='egmon@ufmg.br',
            contact_url='http://www.egmon.com.br',
            authorizations='123456',
            doc='/docs'
        );
        
    def run(self, ):
        self.app.run(
            debug = True
        )
             
server = Server()          