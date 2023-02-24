from application.database import db
from application.models import registration,tweet_message
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import current_app as application

create_registration_parser = reqparse.RequestParser()
create_registration_parser = add_argument('registration_UserId')
create_registration_parser = add_argument('registration_firstname')
create_registration_parser = add_argument('registration_middlename')
create_registration_parser = add_argument('registration_lastname')
create_registration_parser = add_argument('registration_email')
create_registration_parser = add_argument('registration_password')
create_registration_parser = add_argument('registration_age')
create_registration_parser = add_argument('registration_gender')
create_registration_parser = add_argument('registration_phonenumber')

registration_output_fields={
    "registration_userId" : fields.Integer,
    "registration_firstname" : fields.String,
    "registration_middlename" : fields.String,
    "registration_lastname" : fields.String,
    "registration_email" : fields.String,
    "registration_password" : fields.String,
    "registration_age" : fields.Integer,
    "registration_gender" : fields.String,
    "registration_phonenumber" : fields.Integer,
}

class registrationApi(Resource):
    def post(self):
        args = create_registration_parser.parser_args()
        registration_userId=args.get('registration_userId', None)
        registration_firstname=args.get('registration_firstname', None)
        registration_middlename=args.get('registration_middlename', None)
        registration_lastname=args.get('registration_lastname', None)
        registration_email=args.get('registration_email', None)
        registration_password=args.get('registration_password', None)
        registration_age=args.get('registration_age', None)
        registration_gender=args.get('registration_gender', None)
        registration_phonenumber=args.get('registration_phonenumber', None)

        if registration_firstname id None:
            raise BusinessValidationError(status_code=400, error_code="R001", error_message="Validation error")
        if registration_email id None:
            raise BusinessValidationError(status_code=400, error_code="R002", error_message="Validation error")
        if registration_password id None:
            raise BusinessValidationError(status_code=400, error_code="R003", error_message="Validation error")
        if registration_age id None:
            raise BusinessValidationError(status_code=400, error_code="R004", error_message="Validation error")
        if registration_password is None:
            raise BusinessValidationError(status_code=400, error_code="R005", error_message="Validation error")
        if registration_gender is None:
            raise BusinessValidationError(status_code=400, error_code="R006", error_message="Validation error")
        if registration_phonenumber is None:
            raise BusinessValidationError(status_code=400, error_code="R007", error_message="Validation error")

        exists = registration.query.get(userId)
        if exists:
            raise ExistsError(status_code=409)
        
        registration = registration(uid=userId, fname=firstname, mname=middlename, lname=lastname, email1=email, password1=password, phn=phonenumber, gender1=gender, age1=age)