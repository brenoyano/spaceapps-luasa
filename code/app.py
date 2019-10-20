from flask import Flask, render_template, redirect, make_response, url_for, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from user import User 


from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

jwt = JWT(app, authenticate, identity)


class Login(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('/login.html'),200,headers)

    def post(self):
        headers = {'Content-Type': 'text/html'}
        email = request.form['email']
        password = request.form['pass']
        user = User()
        auth = user.log_in_user(email,password)
        if auth:
            return make_response(render_template('/index.html'),200,headers)
        else:
            pass

class Registration(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('/profile.html'),200,headers)

    def post(self):
        headers = {'Content-Type': 'text/html'}
        username = request.form['email']
        password = request.form['pass']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birthday = request.form['birthday']
        gender = request.form['gender']
        phone = request.form['phone']
        user = User()
        email_validation = user.email_exist(username)
        if email_validation:
            return "O e-mail já existe", 401
        else:
            insert = user.create_user(username,password,first_name,last_name,birthday,phone,gender)
            return make_response(render_template('/login.html'),200,headers)
        
class Index(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('/index.html'),200,headers)

class Moon(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('/ar.html'),200,headers)


api.add_resource(Login, '/login')
api.add_resource(Registration, '/registration')
api.add_resource(Index, '/')
api.add_resource(Moon, '/ar')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)