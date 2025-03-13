from tinydb import TinyDB, Query


class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        self.table = self.db.table('Products')
    
    def all_products(self):
        """Returns all products in the database"""
        return self.table.all()
    
    def get_product_id(self, id):
        """Returns all products by id"""
        return self.table.search(self.query.id == id)
    
    def get_all_product_names(self):
        """Returns all product names"""
        name = []
        for product in self.table.all():
            name.append(product['name'])
        return name

    def get_names(self, name: str):
        """Returns all products by name"""
        return self.table.search(self.query.name == name)

    def get_all_catagories(self):
        """Returns all catagories name"""
        return [item['category'] for item in self.table.all()]

    
    def get_small_from_price(self, price):
        return  self.table.search(self.query.price < price)

    def expensive_products(self):
        """Returns a top three expensive products"""
        from operator import itemgetter
        sort = sorted(self.table.all(), key = itemgetter('price'),reverse=True)
        return sort[:3]
    
    def get_between_price(self,max_price , min_price):
        """Returns a products between max_price and min_price"""
        return self.table.search((self.query.price >= min_price) & (self.query.price <= max_price))

    def add_product(self, product):
        """Adds a product to the database"""
        return self.db.insert(product)

    def delete_product(self, doc_id):
        """Deletes a product from the database"""
        return self.table.remove(self.query.id == doc_id)

#db = ProductsDB('products_db.json')
#print(db.get_product_id(1))