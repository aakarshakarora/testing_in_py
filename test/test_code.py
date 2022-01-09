import unittest

from Customer import Customer
from User import User


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.userObject = User("sunny", "1234")
        self.customerObject = Customer(self.userObject.name, self.userObject.customerId)

    def test_check_bill_calculation(self):
        self.customerObject.addItems("Rice", 2, 25)
        self.customerObject.addItems("Milk", 2, 60)
        x = self.customerObject.check_calculateBill()
        self.assertEqual(x, 2 * 25 + 2 * 60)

    def test_check_user_details(self):
        x = self.userObject.check_ustomerDetails()
        self.assertEqual(x, ["sunny", "1234"])

    def test_check_in_lst_false(self):
        self.customerObject.addItems("Rice", 2, 36)
        self.assertFalse(self.customerObject.check_itemExist("Sugar"))

    def test_check_in_lst_true(self):
        self.customerObject.addItems("Rice", 2, 36)
        self.assertTrue(self.customerObject.check_itemExist("Rice"))

    def test_check_value_in_lst_wrt_key(self):
        self.customerObject.addItems("Rice", 2, 26)
        self.assertFalse(self.customerObject.check_value_in_item("Rice", [2, 26, 2 * 16]))
