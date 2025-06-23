import unittest
import stock_manager

class TestStockManager(unittest.TestCase):
    def test_string(self):
        cart = {
            "1": {"name": "apple", "price": "two", "quantity": 100},
            "2": {"name": "orange", "price": 1.5, "quantity": 100}
        }
        stock_manager.save_cart(cart)
        loaded = stock_manager.load_cart()
        total = 0
        with self.assertRaises(Exception):
            for item in loaded.values():
                total += item["price"] * item["quantity"]

    def test_negative(self):
        cart = {
            "1": {"name": "apple", "price": "2", "quantity": 100},
            "2": {"name": "orange", "price": 1.5, "quantity": -50}
        }
        stock_manager.save_cart(cart)
        loaded = stock_manager.load_cart()
        total = 0
        with self.assertRaises(Exception):
            for item in loaded.values():
                total += item["price"] * item["quantity"]
if __name__ == '__main__':
    unittest.main()
