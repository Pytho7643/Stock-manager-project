import argparse
import json
import os

#loading and saving products (json file)
def load_products():
    if not os.path.exists("products.json"):        
        return {}
    with open("products.json", "r", encoding = "utf8") as file:
        return json.load(file)
def save_products(products):
    with open("products.json", "w", encoding = "utf8") as file:
        json.dump(products, file, indent=2)

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
if args.add_product:
    print("add product selected")
if args.update_product:
    print("update product selected")
if args.remove_product:
    print("remove product selected")
if args.view_product:
    print("view product selected")

#cart management
if args.create_cart:
    print("create cart selected")
if args.add_item:
    print("add item selected")  
if args.remove_item:
    print("remove item selected")
if args.view_cart:
    print("view cart selected")
if args.checkout:
    print("checkout selected")

#view stock
if args.print_stock:
    print("print stock selected")