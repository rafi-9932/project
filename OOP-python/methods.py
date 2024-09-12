def call():
    print('calling someone i dont know')
    return 'call done'
class phone:
    price = 12000
    colour = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']


    def call(self):
        print('calling one person')

    def send_sms(self,phone, sms):
            text = f'sending sms to :{phone} and massage: {sms}'
            return text 

my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(42456,'i forget to miss you')
print(result)
