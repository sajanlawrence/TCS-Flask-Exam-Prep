from flask import Flask, jsonify, request, make_response
from functools import wraps
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = "44bt5375ngdnhbsfskjdu9885jd"

def token_required(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return make_response({'Error' : 'token is missing'}, 403)
        try:
            payload = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return make_response({'Error' : 'Invalid Token'}, 403)
        return func(*args,**kwargs)
    return decorated


@app.route('/')
def home():
    return jsonify({'Content' : 'You are now viewing home page'})

@app.route('/public')
def public():
    return jsonify({'Content' : 'This page can be viewed by anyone'})

@app.route('/private')
@token_required
def private():
    return jsonify({'Content' : 'This page is private'})

@app.route('/login')
def login():
    auth = request.authorization
    if not auth:
        return make_response({'Error' : 'auth error'}, 403)
    if auth.username and auth.password == "qwerty":
        token = jwt.encode({'username' : auth.username, 
                            'exp' : datetime.utcnow() + timedelta(minutes=1)
                            },app.config['SECRET_KEY'],algorithm='HS256')
        return jsonify({'token' : token})
    else:
        return make_response({'error' : 'could not verify user. Please login'}, 405,{'WWW-Authenticate' : 'Basic realm="login required"'})

if __name__ == "__main__":
    app.run(debug=True)
















'''
from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my secret key"


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        print("token is : {}".format)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return jsonify({'error':'Invalid token','token' : token}),403
        return f(*args,**kwargs)
    return decorated




@app.route('/unprotected')
def unprotected():
    return jsonify({'Content' : 'This is an unprotected view'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'Content' : 'This is a protected view'})

@app.route('/loginn')
def login():
    auth = request.authorization
    if auth and auth.password == "qwerty":
        token = jwt.encode({'User' : auth.username, 'exp' : datetime.utcnow() + timedelta(minutes=1)},app.config['SECRET_KEY'], algorithm='HS256')
        print(token)
        return jsonify({'token' : token})
    return make_response('could not verify user',401,{'WWW-Authenticate' : 'Basic realm="login required"'})



if __name__ == "__main__":
    app.run(debug=True)

'''