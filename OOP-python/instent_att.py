class Shop:
    shopping_mall = 'jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is an abrittute instence


    def add_to_cart(self, item):
            self.cart.append(item)

        
mahjaben = Shop('mahjabeen')
mahjaben.add_to_cart('shoe')
mahjaben.add_to_cart('phone')
print(mahjaben.cart)

nisho = Shop('nishu')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)