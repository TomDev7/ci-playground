import main.py as main

def testAddition():

    if (main.sumValues(1, 2) == 3):
        return True
    else:
        return False

def testMultiplication():

    if (main.multiplyValues(2, 3) == 6):
        return True
    else:
        return False


testAddition()
testMultiplication
