# ✨LIBRARY FOR IOKA API✨

This library is designed to simplify interaction with the API of the IOKA payment system. It provides a simple and intuitive interface for performing various payment system operations, such as creating transactions, processing payments and managing accounts.


## 📎Functionality
💫Creating and managing payments

💫Integration with various payment methods

💫IOKA Resource Management, for example  Order, Payment, Customer, Card, Webhook

💫User friendly interface

💫Validation of parameters

💫Transforming server responses into developer-friendly formats


## 📎Run Locally

🖇Clone the project

```bash
  git clone https://github.com/llunareine/ioka_library.git
```

🖇Go to the project directory

```bash
  cd /path/to/project
```

🖇Install dependencies

```bash
  poetry install
```

🖇You need to build it locally

```bash
  python setup.py bdist_wheel
```

🖇Your wheel file is stored in the “dist” folder that is now created. You can install your library by using:

```bash
  pip install /path/to/wheelfile.whl
```


## 📎Installation


```bash
    pip install ioka-lib
```


## 📎Usage/Examples

```python
import ioka_lib
ioka = ioka_lib.IokaLib("YOUR_API_KEY")
orders = ioka.Orders
payments  = ioka.Payments

# ORDERS
# print a list of all orders.
print(orders.get_orders().data) 

# print the details of a specific order by its ID.
print(orders.get_order("order_id")) 

# the ID of the first order in the list.
print(orders.get_orders().data[0].id) 

# print that order's amount
print(orders.get_order("order_id").amount) 

# PAYMENTS
# Create a card payment
print(payments.create_card_payment("order_id", "pan", "exp", "holder", "cvc", "save"))

# Get a specific payment by its ID
print(payments.get_payment_by_id('order_id','payment_id'))
```

## 📎To do
Handle all requests asynchronously