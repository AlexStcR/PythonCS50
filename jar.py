class Jar:
    def __init__(self, capacity=12):
        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number
        # of cookies that can fit in the cookie jar. If capacity is not a non-negative int,
        # though, __init__ should instead raise a ValueError.

        if capacity < 0:
            raise ValueError ("Cannot deposit negative cookies")
        if capacity > 13:
            raise ValueError("Exceeds jar capacity")

        self._capacity = capacity
        # size should return the number of cookies actually in the cookie jar, initially 0.
        self._size = 0

    def __str__(self):

        # __str__ should return a str with🍪, where n
        # is the number of cookies in the cookie jar. For instance,
        # if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return "🍪" * self._size

    def deposit(self, n):
        # deposit should add n cookies to the cookie jar.
        # If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.

        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        # withdraw should remove n cookies from the cookie jar. Nom nom nom.
        # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.

        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        # capacity should return the cookie jar’s capacity.
        return self._capacity

    @property
    def size(self):
        # https://www.programiz.com/python-programming/property'''
        # size should return the number of cookies actually in the cookie jar, initially 0.

        return self._size


'''
jar1=Jar()
jar1.deposit(2)
print(jar1)
jar1.withdraw(1)
print(jar1)
'''
