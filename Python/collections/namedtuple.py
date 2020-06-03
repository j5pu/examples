
from collections import namedtuple

customers_data = [
    ['John Carl', 32, 13, 0],
    ['Mary Carl', 25, 27, 159],
    ['Mary Melody', 28, 13, 32],
    ['Susie Perl', 33, 17, 12],
    ['Andy Wharton', 66, 24, 1],
    ['Jorge Mar', 44, 18, 24],
    ['Mary Jorge', 37, 24, 36]
]

# verbose = True
# customers = [Customer(customer_data[0], customer_data[1], customer_data[2], customer_data[3])
#              for customer_data in customers_data]

class Customer:
    def __init__(self, name: str = str(), age: int = int(), experience: int = int(), accidents: int = int()):
        self.name = name
        self.age = age
        self.experience = experience
        self.accidents = accidents

print('---------------------------------------------------------------')
Client = namedtuple('Clients', 'name age experience accidents')
client = Client('Maria', 32, 2, 1)
print(f'type(Clients): {type(Client)}')
print(f'Clients: {Client}')
print(f'type(client): {type(client)}')
print(f'client1: {client}')
print(f'client1.name: {client.name}')

print('---------------------------------------------------------------')
class Ana:
    name='Ana'
ana = Ana()
print(f'type(Ana): {type(Ana)}')
print(f'Ana: {Ana}')
print(f'type(ana): {type(ana)}')
print(f'ana: {ana}')
print(f'ana.name: {ana.name}')
