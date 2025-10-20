from squared import square_number
def test_positive_number(self):
    self.assertEqual(square_number(2), 4)

def test_negative_number(self):
    self.assertEqual(square_number(-3), 9)

def test_zero(self):
    self.assertEqual(square_number(0), 0)
