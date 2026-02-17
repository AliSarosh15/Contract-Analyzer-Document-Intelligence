from flask import Flask
from app.extensions import db
from User.routes.user_routes import user_bp
from TandC.routes.TCroutes import tc_bp



def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:ali123@localhost:5432/terms_and_condition'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


    app.register_blueprint(user_bp,url_prefix='/api/user')
    app.register_blueprint(tc_bp,url_prefix='/api/tandc')
    db.init_app(app)
    for rule in app.url_map.iter_rules():
        print(f'{rule.endpoint}:{rule.methods}-->{rule.rule}')
    with app.app_context():
        db.create_all()
    return(app)
