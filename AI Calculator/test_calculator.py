import unittest
from chatterbot import ChatBot

def evaluate_expression(expression, bot):
    try:
        response = bot.get_response(expression)
        return str(response)
    except:
        return "Please enter valid input."

class TestCalculatorBot(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.bot = ChatBot(name='Calculator',
                          read_only=True,
                          logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
                          storage_adapter="chatterbot.storage.SQLStorageAdapter")
    
    def test_addition(self):
        result = evaluate_expression('3 + 4', self.bot)
        self.assertEqual(result, '3 + 4 = 7')
        
    def test_subtraction(self):
        result = evaluate_expression('10 - 5', self.bot)
        self.assertEqual(result, '10 - 5 = 5')
        
    def test_multiplication(self):
        result = evaluate_expression('6 * 7', self.bot)
        self.assertEqual(result, '6 * 7 = 42')

    def test_division(self):
        result = evaluate_expression('15 / 3', self.bot)
        self.assertEqual(result, '15 / 3 = 5')

    def test_power(self):
        result = evaluate_expression('4 ^ 2', self.bot)
        self.assertEqual(result, '4 ^ 2 = 16')

    def test_invalid_input(self):
        result = evaluate_expression('three plus four', self.bot)
        self.assertEqual(result, 'Please enter valid input.')
        
    def test_empty_input(self):
        result = evaluate_expression('', self.bot)
        self.assertEqual(result, 'Please enter valid input.')


if __name__ == '__main__':
    unittest.main()
