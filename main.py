__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import testdata
import os

path_database = os.path.join(os.getcwd(),'besty.db')

def main():
    if os.path.exists(path_database):
        pass
    else:
        db.create_tables([User, Product, Tag, ProductTag, Tracker]) # creates needed tables
        testdata.create_user_tag_tracker_data()                     # fills the database with testdata
    print("------------------------------------------------------")
    search("boot")                                                  # funtion 1
    print("------------------------------------------------------")
    list_user_products("Roodkapje")                                 # funtion 2
    print("------------------------------------------------------")
    list_products_per_tag("rommel")                                 # funtion 3    
    print("------------------------------------------------------")
    add_product_to_catalog("Gitaa", "6 snaren", 1, 1300, "Hans", "muziek") #funtion 4
    print("------------------------------------------------------")
    update_stock("bottle", 20)                                      # funtion 5
    print("------------------------------------------------------")
    purchase_product("boot", "Roodkapje")                           # function 6
    print("------------------------------------------------------")
    remove_product("onderzetter")                                   # funtion 7
    print("------------------------------------------------------")

def search(term):
    query = Product.select().where(Product.name.contains(term))
    print(f"You are looking for {term}, this is what i have found:")
    for item in query:
        print(item.name)
    
def list_user_products(name):
    query = User.get(User.name == name)
    print(f"You are looking for products from {name}, this is what i have found:")
    for x in query.own:
        print(x.name)

def list_products_per_tag(tag_id):
    products = Tag.get(Tag.name == tag_id)
    print(f"This are all the products with #{tag_id}:")
    for x in products.tag:
        print(x.name)

def add_product_to_catalog(name, description, price, stock, owner, tag):
    # Check if tag already exists, otherwise, make a new tag in Tag.
    tagslist = []
    for item in Tag.select():
        tagslist.append(item.name)
    if tag not in tagslist:
            Tag.create(name=tag)
            tagslist.append(tag)
            print(f"{tag} is added to table Tag")

    # Creates the product
    product = Product.create(
        name=name,
        description=description,
        price=price,
        stock=stock,
        owner=User.get(User.name==owner)
    )
    
    # Makes the connection between tag and product
    new_tag = Tag.get(Tag.name==tag)
    product.tags.add(new_tag)

    print(f"{name} is added to table Products")

def update_stock(product_id, new_quantity):
    row=Product.get(Product.name==product_id)
    print ("name: {} old_stock: {}".format(row.name, row.stock))
    row.stock=new_quantity
    row.save()
    print ("name: {} new_stock: {}".format(row.name, row.stock))

def purchase_product(product_id, buyer_id):
    # Updates owner for a product
    row=Product.get(Product.name==product_id)
    buyer = User.get(User.name==buyer_id)
    row.owner_id=buyer.id
    row.save()
 
    Tracker.create(
        product=row,
        quantity=row.stock,
        buyer=buyer
    )

    print(f"{buyer_id} is the new owner of {product_id}")

def remove_product(product_id):
    dq = Product.delete().where(Product.name==product_id)
    dq.execute()
    product=product_id.capitalize()
    print(f"{product} is deleted form list")

if __name__ == "__main__":
    main()
   





