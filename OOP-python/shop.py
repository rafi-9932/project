class Shop:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer


    def add_to_cart(self,item):
        self.cart.append(item)


sanjana = Shop(' sanjana')
sanjana.add_to_cart('shoes')
sanjana.add_to_cart('phone')
print(sanjana.cart)


nishu = Shop('nishu')
nishu.add_to_cart('cap')
nishu.add_to_cart('watch')
print(nishu.cart)
