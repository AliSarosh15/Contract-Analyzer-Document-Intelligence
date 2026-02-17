from flask import Blueprint,request,jsonify
from app.extensions import db
from User.models.user_model import User
from functools import wraps
# from User.utils import set_token


user_bp=Blueprint('user',__name__)


def token_required(f):
    wraps(f)
    def decorated(*args,**kwargs):
        token=request.headers.get("Authorization")
        if not token or not token.startswith("Bearer"):
            return jsonify({"message:invalid token"})
        token=token.split()[1]
        users=User.query.filter(User.token==token).first()
        if not users:
            return jsonify({"message":"invalid token"})
        return jsonify(*args,**kwargs,current_user=users)
    return decorated
    
@user_bp.route('/userlogin',methods=["POST"])
def user_login():
    data=request.get_json()
    users=User.query.filter(User.user_name==data["user_name"]).first()
    print(users)
    if users and users.password==data["password"]:
        User.set_token(users)
        db.session.commit()
        return jsonify({"message":"login successful"})
    return jsonify({"message":"invalid username or password"})


   
@user_bp.route('/getalluser',methods=["GET"])
def get_user():
    users=[{
        "id":value.id,
        "user_name":value.user_name,
        "password":value.password,
        "phone_no":value.phone_no,
        "email":value.phone_no
    }for value in(db.session.query(User.id,User.user_name,User.password,User.phone_no,User.email)).all()
    ]
    return jsonify(users)

@user_bp.route('/postuser',methods=["POST"])
def post_user():
    data=request.get_json()
    users=User(user_name=data["user_name"],password=data["password"],phone_no=data["phone_no"],email=data["phone_no"])
    db.session.add(users)
    db.session.commit()
    return jsonify({"message":"new user created"})






