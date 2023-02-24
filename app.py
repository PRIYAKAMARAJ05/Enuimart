import os
from flask import Flask
from flask_restful import Resource, apllication
from application.config import LocalDevelopmentConfig
from application.database import db

app, api = None, None
def create_app():
    app= Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development")== "production":
        raise Exception('PRODUCTION SETUP NOT YET READY')
    else:
        print('Starting Local Development environment')
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app, api

app, api = create_app()
from application.api import registrationApi
api.add_resource(registrationApi, "/api/user")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)