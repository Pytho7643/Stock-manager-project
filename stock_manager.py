import argparse
import json
import os

#loading and saving products (json file)
def load_products():
    if not os.path.exists("products.json"):        
        return {}
    with open("products.json", "r", encoding = "utf8") as f:
        return json.load(f)
def save_products(products):
    with open("products.json", "w", encoding = "utf8") as f:
        json.dump(products, f, indent=2)

#creating-loading-saving cart (json file)
def create_cart():
    with open("cart.json", "w", encoding="utf-8") as f:
        json.dump({}, f)
def load_cart():
    if not os.path.exists("cart.json"):
        return {}
    with open("cart.json", "r", encoding="utf-8") as f:
        return json.load(f)
def save_cart(cart):
    with open("cart.json", "w", encoding="utf-8") as f:
        json.dump(cart, f, indent=2)

parser = argparse.ArgumentParser()

#products
parser.add_argument("--add-product", action="store_true")
parser.add_argument("--update-product", action="store_true")
parser.add_argument("--remove-product", action="store_true")
parser.add_argument("--view-product", action="store_true")

#cart
parser.add_argument("--create-cart", action="store_true")
parser.add_argument("--add-item", action="store_true")
parser.add_argument("--remove-item", action="store_true")
parser.add_argument("--view-cart", action="store_true")
parser.add_argument("--checkout", action="store_true")

#stock
parser.add_argument("--print-stock", action="store_true")

#product info
parser.add_argument("--id", type=str)
parser.add_argument("--name", type=str)
parser.add_argument("--price", type=float)
parser.add_argument("--quantity", type=int)

#parsing arguments
args = parser.parse_args()

#product management

#add product
if args.add_product:
    print("add product selected")
    if args.id is None or args.name is None or args.price is None or args.quantity is None:
        print("error: ID, name, price, and quantity are required for adding products")
    else:
        products = load_products()
        if args.id in products:
            print(f"error: product with this ID {args.id} already exists.")
        else:
            products[args.id] = {
                "name": args.name,
                "price": args.price,
                "quantity": args.quantity
            }
            save_products(products)
            print(f"product {args.name} added, ID {args.id}, price: {args.price}KWD, and quantity {args.quantity}")

#update product
if args.update_product:
    print("update product selected")
    if args.id is None:
        print("error : ID is required for updating product")
    else:
        products = load_products()
        if args.id not in products:
            print(f"error : no product with ID {args.id}")
        else:
            if args.name is not None:
                products[args.id]["name"] = args.name
            if args.price is not None:
                products[args.id]["price"] = args.price
            if args.quantity is not None:
                products[args.id]["quantity"] = args.quantity

            save_products(products)
            print(f"Product ID {args.id} updated.")

#remove product
if args.remove_product:
    print("remove product selected")
    if args.id is None:
        print(f"error: ID is required for removing products")
    else:
        products = load_products()
        if args.id not in products:
            print(f"eror: no product with ID {args.id}")
        else:
            del products[args.id]
            save_products(products)
            print(f"product with ID {args.id} removed")

#view product
if args.view_product:
    print("view product selected")
    products = load_products()
    if not products:
        print(f"error: no products found")
    else:
        print("products:")
        for product_id, details in products.items():
            print(f"ID : {product_id}, name: {details['name']}, price: {details['price']} KWD, quantity: {details['quantity']}")

#cart management

#create cart
if args.create_cart:
    print("create cart selected")
    create_cart()
    print("cart created")

#add item to cart
if args.add_item:
    print("add item selected")
    if args.id is None or args.quantity is None:
        print("error: product-ID and quantity are required for adding to cart")
    else:
        products = load_products()
        if args.id not in products:
            print(f"error: no item with ID {args.id}")
        elif args.quantity > products[args.id]["quantity"]:
            print(f"error: product {args.id} is out of stock/not enough stock. available: {products[args.id]['quantity']}")
        else:
            cart = load_cart()
            if args.id in cart:
                cart[args.id]["quantity"] += args.quantity
            else:
                cart[args.id] = {
                    "name": products[args.id]["name"],
                    "price": products[args.id]["price"],
                    "quantity": args.quantity
                }
            save_cart(cart)
            print(f"added {args.quantity} of {products[args.id]['name']} to cart.")  

#remove item from cart    
if args.remove_item:
    print("remove item selected")
    if args.id is None:
        print("error: ID is required to remove item from cart")
    else:
        cart = load_cart()
        if args.id not in cart:
            print(f"error: no item with ID {args.id} in cart")
        else:
            removed_name = cart[args.id]["name"]
            del cart[args.id]
            save_cart(cart)
            print(f"removed {removed_name} from the cart")

#view cart
if args.view_cart:
    print("view cart selected")
    cart = load_cart()
    if not cart:
        print("your cart is empty")
    else:
        print("your cart:")
        total = 0
        for item in cart.values():
            item_total = item["price"] * item["quantity"]
            total += item_total
            print(f"{item['quantity']} x {item['name']} for {item['price']} KWD (1x)")
        print(f"Total: {total:.2f} KWD")

#checkout
if args.checkout:
    print("checkout selected")
    cart = load_cart()
    if not cart:
        print("your cart is empty.")
    else:
        products = load_products()
        total = 0
        print("receipt:")
        for product_id, item in cart.items():
            name = item["name"]
            price = item["price"]
            qty = item["quantity"]
            checkout_total = price * qty
            total += checkout_total
            print(f"{qty} x {name} @ {price} each = {checkout_total:.2f} KWD")
            products[product_id]["quantity"] -= qty
        print(f"Total: {total:.2f} KWD")
        save_products(products)
        save_cart({})
        print("checkout complete, thank you for your purchase!")

#view stock
if args.print_stock:
    print("print stock selected")
    products = load_products()
    if not products:
        print("error: no products found.")
    else:
        print("Stock List:")
    for product_id, details in products.items():
        print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']} KWD, Quantity: {details['quantity']}")
