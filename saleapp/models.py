from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from saleapp import db
from datetime import datetime
from flask_login import UserMixin
from enum import Enum as UserEnum

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipts = relationship("Receipt", backref="user", lazy=True)
    comments = relationship("Comment", backref="user", lazy=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    __tablename__ = "category"

    name = Column(String(20), nullable=False)
    products = relationship("Product", backref="category", lazy=False)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = "product"

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = relationship("ReceiptDetail", backref="product", lazy=True)
    comments = relationship("Comment", backref="product", lazy=True)

    def __str__(self):
        return self.name

class Comment(BaseModel):
    content = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    created_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.content


class Receipt(BaseModel):
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    details = relationship("ReceiptDetail", backref="receipt", lazy=True)

class ReceiptDetail(db.Model):
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False, primary_key=True)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)

if __name__ == "__main__":
    db.create_all()

    #c1 = Category(name='V??n h???c')
    #c2 = Category(name='Kinh t???')
    #c3 = Category(name='Thi???u Nhi')

    #db.session.add(c1)
    #db.session.add(c2)
    #db.session.add(c3)

    #db.session.commit()

    # products = [{
    #      "id": 1,
    #      "name": "Cho t??i xin m???t v?? ??i tu???i th??",
    #      "description": "Nguy???n Nh???t ??nh, B??a c???ng, T??i b???n 2018",
    #      "price": 140000,
    #      "image": "images/ctx1vdtt.jpg",
    #      "category_id": 1
    #     }, {
    #      "id": 2,
    #      "name": "T??i th???y hoa v??ng tr??n c??? xanh",
    #      "description": "Nguy???n Nh???t ??nh, B??a c???ng, B???n in m???i 2018",
    #      "price": 125000,
    #      "image": "images/tthvtcx.jpg",
    #      "category_id": 1
    #     }, {
    #      "id": 3,
    #      "name": "C?? g??i ?????n t??? h??m qua",
    #      "description": "Nguy???n Nh???t ??nh, B??a m???m",
    #      "price": 80000,
    #      "image": "images/cgdthq.jpg",
    #      "category_id": 1
    #     }, {
    #      "id": 4,
    #      "name": "S??? im l???ng c???a b???y c???u",
    #      "description": "Thomas Harris, B??a m???m, T??i b???n 2019",
    #      "price": 115000,
    #      "image": "images/silcbc.jpg",
    #      "category_id": 1
    #     }, {
    #      "id": 5,
    #      "name": "Ngh?? gi??u & l??m gi??u",
    #      "description": "Napoleon Hill, B??a m???m, T??i b???n 2020",
    #      "price": 110000,
    #      "image": "images/ngvlg.jpg",
    #      "category_id": 2
    #     }, {
    #      "id": 6,
    #      "name": "B?? t???p k??? chuy???n - Ch?? v???t x??m",
    #      "description": "Nhi???u t??c gi???, B??a m???m",
    #      "price": 10000,
    #      "image": "images/cvx.jpg",
    #      "category_id": 3
    #     }]
    # for p in products:
    #     pro = Product(name=p['name'], price=p['price'], image=p['image'], description=p['description'], category_id=p['category_id'])
    #
    #     db.session.add(pro)
    # db.session.commit()


