class Computation:
    def __init__(self):
        pass

    def factorial(self,n):
        j = 1
        for number in range(1, n+1):
            j = j * number
        return j

    def sum(self, n):
        j = 0
        for number in range(1, n+1):
            j = j + number
        return j

