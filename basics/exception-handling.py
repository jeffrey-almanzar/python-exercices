

class MyException(Exception):
    pass

def sample_func():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Error:", e)
        raise MyException("This is a custom exception!")
    except FloatingPointError as e:
        print("Error:", e)
    except MyException as e:
        print("Custom error:", e)
    finally:
        print("Always run")

try:
    sample_func()
except Exception as e:
    print(e)

    