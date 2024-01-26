# ✨LIBRARY FOR IOKA API✨

This library is designed to simplify interaction with the API of the IOKA payment system. It provides a simple and intuitive interface for performing various payment system operations, such as creating transactions, processing payments and managing accounts.


## 📎Functionality
💫Creating and managing payments

💫Integration with various payment methods


## 📎Run Locally

Clone the project

```bash
  git clone https://github.com/llunareine/ioka_library.git
```

Go to the project directory

```bash
  cd /path/to/project
```

Install dependencies

```bash
  poetry install
```

You need to build it locally

```bash
  python setup.py bdist_wheel
```

Install it in the project where you will use the library

```bash
  pip install /path/to/wheelfile.whl
```

## 📎Usage/Examples

```python
import ioka_lib
ioka = ioka_lib.IokaLib("YOUR_API_KEY")
orders = ioka.Orders

print(orders.get_orders().data) 
# print a list of all orders.
print(orders.get_order("order_id")) 
# print the details of a specific order by its ID.
print(orders.get_orders().data[0].id) 
# the ID of the first order in the list.
print(orders.get_order("order_id").amount) 
# print that order's amount

```