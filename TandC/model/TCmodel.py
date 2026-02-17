from app.extensions import db
import secrets
from User.models import user_model
from sqlalchemy.sql.schema import ForeignKey

class TermsCondition(db.Model):
    __tablename__="termscondition"
    id=db.Column(db.Integer,primary_key=True)
    tc_content=db.Column(db.Text,nullable=True)
    tc_summary=db.Column(db.Text,nullable=True)
    req_user=db.Column(db.Integer,ForeignKey('user.id'),nullable=False)
    products_company=db.Column(db.String(255),nullable=False)
    product_name=db.Column(db.String(255),nullable=False)

    def set_token(self):
        self.token=secrets.token_hex(32)
        print(self.token)





