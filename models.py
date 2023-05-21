from peewee import *


db = SqliteDatabase('besty.db') 

# :memory:, use this to test and only use testdata once. Nothing will be saved.

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    adress = CharField()

class Tag(BaseModel):
    name = CharField()

class Product(BaseModel):
    name = CharField()
    description = CharField()
    price = DecimalField(decimal_places=2, auto_round=True)
    stock = IntegerField()
    owner = ForeignKeyField(User, backref="own")
    tags = ManyToManyField(Tag, backref='tag')

ProductTag = Product.tags.get_through_model()

class Tracker(BaseModel):
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    buyer = ForeignKeyField(User)