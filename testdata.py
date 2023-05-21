from peewee import *
from models import *

"""
CAUTION!
Caution for user_data. In the user data you find the user, tag, product and tracker data.
Whenever you want to change the teststa, be sure that you fill in tracker data with data which already excists
in the database or be sure that the user and product already have been looped.
Otherwise python can not handle the function te create the database! This has to do with the fact that
the function dont know what id numbers belongs to a product and user. 
"""

user_data = [
 (  # User
    ("Hans", "Amsterdam"),
        
        [
        #Products                       #tags
        ("bottle", "round", 10.22, 18, ("rommel", "handig")),
        ("boot", "round", 10.22, 18, ("rommel", "handig")),
        ],
        # 
        [
        ("bottle", 10)
        ],
 
      
 ),
(
    ("Grietje", "Eindhoven"),
       [
         ("fles", "rond", 10.22, 20, ("rommel", "leuk")),
       ],
       [
        ("bottle", 10)
        ],
 
),
(   
    ("Roodkapje", "Rotterdam"),
       [
         ("onderzetter", "round", 10.22, 30, ("handig", "leuk")),
        ],
        [
        ("bottle", 10)
        ],
 
),        
(
    ("Harry", "Londen"),
       [
         ("muis", "ergonomisch", 10.22, 40, ("rommel",)),
    ],
    [
    ("muis", 10)

]
 
)
]

 
def create_user_tag_tracker_data():
    # Tag.select() #only need when database already excists
    tagslist = []
    # tagslist.append(Tag.name) #only need when database already excists
    for user, product, tracker in user_data:
        user = User.create(
            name=user[0], 
            adress=user[1])
        for item in product:
            product = Product.create(
                name = item[0],
                description = item[1],
                price = item[2],
                stock = item[3],
                owner = user
            )
            for x in item[4]:
                if x not in tagslist:
                    tagslist.append(x)
                    Tag.create(name=x)
            for x in item[4]:
                id = Tag.get(Tag.name==x)
                product.tags.add(id)
        for purchase in tracker:
            tracker = Tracker.create(
                product = Product.get(Product.name==purchase[0]),
                quantity = purchase[1],
                buyer = user
            )  
         