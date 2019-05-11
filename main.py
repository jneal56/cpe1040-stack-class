from stack import Stack
class arrList():

def test_integers():
    s = Stack(3)
    s.push(5)
    t = s.pop()
    print(t)


def test_floats():
    s = Stack()
    s.push(2,3)
    t = s.pop()
    print(t)


def test_strings():
    s = Stack("")
    s.push("Ahh")
    t = s.pop()
    print(t)


def test_exceptions():
    s = Stack(5)
    s.push("ahh")
    t = s.pop()
    print(t)

def safe_test_int_excption():
    s = InStack()
    s.push(1.0)

if __name__ == '__main__':
    test_integers()
    try:
        test_exceptions()

    except ValueError:
        print("test value error")


    try:
        test_strings()

    except ValueError:
        print("string error")

    try:
        test_integers()

    except ValueError:
        print("Int error")

    try:
        test_floats()

    except ValueError:
        print("float error")

    try:
        safe_test_int_excption()

    except ValueError:
        print("Value error")

    
