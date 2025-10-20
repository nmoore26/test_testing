from squared import square_number
def test_positive_number(self):
    assert(square_number(2), 4)

def test_negative_number(self):
    assert(square_number(-3), 9)

def test_zero(self):
    assert(square_number(0), 0)
