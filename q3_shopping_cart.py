# Part A

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Part B

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


# Part C

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print("\nTuple Error:", e)
        print("Tuples are immutable and cannot be modified.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    total -= discount_amount

    return total


cart1 = create_cart("Rahul", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

cart2 = create_cart("Priya", 5)

add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1000, 1)

print("\nCustomer 1 Cart:")
print(cart1)
print("Total:", calculate_total(cart1))

print("\nCustomer 2 Cart:")
print(cart2)
print("Total:", calculate_total(cart2))

prices = (100, 200, 300)
update_price(prices, 500)

# Discussion Answers

# 1. discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared.

# 2. Rebinding means assigning a new object.
# Mutating means changing the existing object.

# 3. Mutable: list, dict, set
# Immutable: tuple, str, int

# 4. When a list is passed to a function and modified,
# changes are reflected outside because both references
# point to the same list object.h