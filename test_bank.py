import unittest
from bank import *

class TestBank(unittest.TestCase):
    def test_Deposit(self):

        client1 = BankAccount(12, "Miguel", "Estêvão", 6000)
        client2 = BankAccount(123, "Bruno", "Montenegro", 6000)
        client3 = BankAccount(1234, "Teresa", "Estêvão", 6000)


        self.assertEqual(client1.Deposit(1000), 7000)
        self.assertEqual(client2.Deposit(500),6500)
        self.assertEqual(client3.Deposit(20),6020)

    def test_email(self):

        client1 = BankAccount(12, "Miguel", "Estêvão", 6000)
        client2 = BankAccount(123, "Bruno", "Montenegro", 6000)
        client3 = BankAccount(1234, "Teresa", "Estêvão", 6000)

        self.assertEqual(client1.email(), "Miguel.Estêvão@gmail.com")

