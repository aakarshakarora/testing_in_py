class User:

    def __init__(self, name, customerID):
        self.name = name
        self.customerId = customerID

    def customerDetails(self):
        return [self.name, self.customerId]
