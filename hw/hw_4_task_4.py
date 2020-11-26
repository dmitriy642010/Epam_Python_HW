from typing import List


def fizzbuzz(n: int) -> List[str]:

    """
    - Install Python 3.8 (https://www.python.org/downloads/)
     - Install pytest `pip install pytest`
     - Clone the repository https://github.com/dmitriy642010/Epam_Python_HW
     - Checkout branch HW4T4
     - Open terminal
     -Run python hw_4_task_4.py -v

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    >>> fizzbuzz(0.2)
    Traceback (most recent call last):
        ...
    TypeError: Wrong number!
    """

    try:
        res = []
        for i in range(1, n + 1):
            div_3 = i % 3
            div_5 = i % 5
            if div_3 == 0 and div_5 == 0:
                res.append("Fizz Buzz")
            elif div_3 == 0:
                res.append("Fizz")
            elif div_5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    except TypeError:
        raise TypeError("Wrong number!")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
