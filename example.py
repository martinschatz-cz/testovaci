#example.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiplication(a, b):
    return a * b

# uncomment the following test in step 5
def test_subtract():
    assert subtract(2, 3) == -1
    
def test_multiplication():
    assert multiplication(2, 3) == 6
