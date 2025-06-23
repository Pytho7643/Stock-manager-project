import unittest
import stock_manager

class TestStockManager(unittest.TestCase):
    def setUp(self):
        stock_manager.save_products({
            "1": {"name": "apple", "price": 1.5, "quantity": 200},
            "2": {"name": "orange", "price": 2.0, "quantity": 170},
            "3": {"name": "peach", "price": 3.0, "quantity": 150}
        })
        stock_manager.create_cart()

    def test_update_product(self):
        products = stock_manager.load_products()
        products["1"]["price"] = 2.5
        stock_manager.save_products(products)
        updated = stock_manager.load_products()
        self.assertEqual(updated["1"]["price"], 2.5)

    def test_remove_product(self):
        products = stock_manager.load_products()
        del products["1"]
        stock_manager.save_products(products)
        updated = stock_manager.load_products()
        self.assertNotIn("1", updated)

    def test_view_product(self):
        products = stock_manager.load_products()
        self.assertIn("1", products)
        self.assertEqual(products["1"]["name"], "apple")

    def test_create_cart(self):
        stock_manager.create_cart()
        cart = stock_manager.load_cart()
        self.assertEqual(cart, {})

    def test_add_item_to_cart(self):
        cart = stock_manager.load_cart()
        cart["1"] = {
            "name": "apple",
            "price": 1.5,
            "quantity": 2
        }
        stock_manager.save_cart(cart)
        updated_cart = stock_manager.load_cart()
        self.assertIn("1", updated_cart)
        self.assertEqual(updated_cart["1"]["quantity"], 2)

    def test_remove_item_from_cart(self):
        cart = stock_manager.load_cart()
        cart["1"] = {
            "name": "apple",
            "price": 1.5,
            "quantity": 2
        }
        stock_manager.save_cart(cart)
        cart = stock_manager.load_cart()
        del cart["1"]
        stock_manager.save_cart(cart)
        updated = stock_manager.load_cart()
        self.assertNotIn("1", updated)

    def test_view_cart(self):
        cart = {
            "1": {"name": "apple", "price": 1.5, "quantity": 2},
            "2": {"name": "orange", "price": 2.0, "quantity": 3}
        }
        stock_manager.save_cart(cart)
        loaded_cart = stock_manager.load_cart()
        self.assertEqual(len(loaded_cart), 2)
        self.assertEqual(loaded_cart["2"]["quantity"], 3)

    def test_checkout(self):
        cart = {
            "1": {"name": "apple", "price": 1.5, "quantity": 2},
            "2": {"name": "orange", "price": 2.0, "quantity": 3}
        }
        stock_manager.save_cart(cart)

        products = stock_manager.load_products()
        products["1"]["quantity"] -= 2
        products["2"]["quantity"] -= 3
        stock_manager.save_products(products)
        stock_manager.save_cart({

        })

        updated = stock_manager.load_products()
        self.assertEqual(updated["1"]["quantity"], 198)
        self.assertEqual(updated["2"]["quantity"], 167)

    def test_print_stock(self):
        products = stock_manager.load_products()
        self.assertIn("3", products)
        self.assertEqual(products["3"]["name"], "peach")

if __name__ == '__main__':
    unittest.main()