class phone:
    manufacutured = 'chine'
    #constructor 
    def __init__(self, owner, brand, price, ):
      self.owner = owner
      self.brand = brand
      self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone = phone('kala chan', 'oppo', 10000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = phone('my janu', 'iphone' , 100000)
print(her_phone.owner, her_phone.brand, her_phone.price)

dad_phone = phone('abbu', 'nokia', 2400)
print(dad_phone.owner, dad_phone.brand , dad_phone.price)