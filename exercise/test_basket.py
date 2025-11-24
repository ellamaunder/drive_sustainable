import unittest
from basket import Basket

class TestBasket(unittest.TestCase):
    def setUp (self):
        self.basket = Basket()
    
    def test_add_single_item(self):
        self.assertEqual(len(self.basket.items), 0)
        result = self.basket.add_item("apple", 3)
        self.assertTrue(result)
        self.assertEqual(self.basket.items["apple"], 3)

    def test_calc_price_when_empty_is_zero(self):
        self.assertEqual(self.basket.calculate_price(), 0.0)

    def test_remove_single_item(self):
        self.assertEqual(len(self.basket.items), 0)
        result = self.basket.add_item("apple", 1)
        self.assertEqual(self.basket.items['apple'], 1)
        result = self.basket.remove_item('apple', 1)
        self.assertTrue(result)
        with self.assertRaises(KeyError):
            self.assertEqual(self.basket.items['apple'], 0)

    def test_removing_item_that_doesnt_exist_does_nothing(self):
        self.assertEqual(len(self.basket.items), 0)
        result = self.basket.remove_item('apple', 1)
        self.assertFalse(result)
        self.assertEqual(len(self.basket.items), 0)

    def test_remove_single_item_to_not_zero(self):
        self.assertEqual(len(self.basket.items), 0)
        result = self.basket.add_item("apple", 2)
        self.assertEqual(self.basket.items['apple'], 2)
        result = self.basket.remove_item('apple', 1)
        self.assertTrue(result)
        self.assertEqual(self.basket.items['apple'], 1)

    def test_add_item_thats_not_allowed(self):
        self.assertEqual(len(self.basket.items), 0)
        result = self.basket.add_item("orange", 1)
        self.assertFalse(result)
        self.assertEqual(len(self.basket.items), 0)

    def test_add_multiple_items_with_one_incorrect(self):
        self.assertEqual(len(self.basket.items), 0)
        self.basket.add_item("apple", 2)
        self.basket.add_item("banana", 2)
        result = self.basket.add_item("orange", 1)
        self.assertFalse(result)
        self.assertEqual(len(self.basket.items), 2)


    def test_calculate_price_for_multiple_items(self):
        self.basket.add_item("apple", 2)
        self.basket.add_item("banana", 4)
        total_price = self.basket.calculate_price()
        expected_price = (Basket.item_prices["apple"] * 2) + (Basket.item_prices["banana"] * 4)
        self.assertEqual(total_price, expected_price)

if __name__ == '__main__':
    unittest.main()