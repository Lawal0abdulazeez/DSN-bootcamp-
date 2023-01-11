'''This is a Telecom Based TBI python project(no deployment or hosting service it has to be run in a python terminal),
It is aimed to mimic the Telecom service in Nigeria (e.g MTN)
The features available are:
    *Ability for new customer to register and login with their pin
    *500 airtime registration bonus
    *Customer should be able to buy airtime and data
    *Customer should be able to check airtime and data balance
The project is aimed to improve my understanding of OOP
So i will be working mostly with OOP
'''
CustomerLists = {
#name: [password, number, airtimeBalance, DataBalance],
'lawal': ['oluwa', '080123', 1000, 1024]
}

list =['lawal', 'oluwa', '080123', 1000, 1024]

class Customer():
    """docstring for Customer."""
    def __init__(self, name, password, number, airtimeBalance, DataBalance):
        self.name = 'lawal'
        self.password = 'oluwa'
        self.number = 1234
        self.airtimeBalance = 1000
        self.DataBalance = 1000
        print('Customer instanciated')

    def login(self):
        self.name = input('Enter your name')
        if self.name in CustomerLists:
            print('Welcome {}'.format(self.name))
        self.password = input('Enter your password')
        count = 0
        if self.password == CustomerLists[self.name][0]:
            print('correct password')
            print(CustomerLists[self.name])
        while self.password != CustomerLists[self.name][0]:
            print('Wrong Password')
            self.password = input('Enter your password')
            count +=1
            if count == 3:
                print('timeout')
                break
    def register(self):
        self.name = input('Enter your name: ')
        self.password = input('Enter your password')
        self.number = int(input('Enter your number'))
        self.airtimeBalance = 500
        self.DataBalance = 0
        customer = {self.name: [self.password, self.number, self.airtimeBalance, self.DataBalance]}
        return self.name, self.airtimeBalance, self.DataBalance, self.password, self.number
        CustomerLists.update(customer)

    def rechargeAirtime(self, name):
        customer = CustomerLists[name]
        airtimeBalance = customer[2]
        print('Enter the amount you want to buy')
        amount = int(input(''))
        airtimeBalance += amount
        customer[2] = airtimeBalance
        print('Airtime recharge successful')


C = Customer('lawal', 'oluwa', '080123', 1000, 1024)
C.rechargeAirtime('lawal')
print(CustomerLists)
