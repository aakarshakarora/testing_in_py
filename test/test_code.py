import unittest

from Customer import Customer
from User import User


class SimpleTest(unittest.TestCase):

    def test_check_bill_calculation(self):
        userObject = User("sunny", "1234")
        customerObject = Customer(userObject.name, userObject.customerId)
        customerObject.addItems("Rice", 2, 25)
        customerObject.addItems("Milk", 2, 60)
        x = customerObject.calculateBill()
        self.assertEqual(x, 2 * 25 + 2 * 60)

    def test_check_user_details(self):
        userObject = User("sunny", "1234")
        x = userObject.customerDetails()
        self.assertEqual(x, ["sunny", "1234"])
