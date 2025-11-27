'''
Implementing Static Methods
Create a class called MathOperations to group together some basic arithmetic functionality. Inside this class, define two static methods:

add, which accepts two numeric parameters and returns their sum.

multiply, which also takes two numeric parameters and returns their product.

Finally, write a small driver program to test the functionality of the add and multiply methods. This should involve calling both methods with sample inputs and printing the results to verify that they work correctly.
'''


class MathOperations:

    @staticmethod
    def sum(n1: float, n2: float) -> float:
        return n1 + n2
    
    @staticmethod
    def multiply(n1: float, n2: float) -> float:
        return n1 * n2
    


if __name__ == "__main__":

    print(MathOperations.sum(2, 4))
    print(MathOperations.multiply(2, 4))