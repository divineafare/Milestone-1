from Policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder('John Cena', '001')
policyholder2 = Policyholder('Mucheal Joy', '002')

# Create a product
product1 = Product('P001', 'Health Insurance', 1000)

# Process payments
payment1 = Payment(policyholder1, 1000)
payment1.process_payment()

# Display policyholder details
print(f'Policyholder: {policyholder1.name}, Active: {policyholder1.active}')
