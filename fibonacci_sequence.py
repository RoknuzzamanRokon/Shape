num_1 = 0
num_2 = 1
count = 0

while count < 10:
    print(num_1)
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    count += 1


# Here using only function.
def fibonacci(value):
    count_1 = 0
    num_f_1 = 0
    num_f_2 = 1
    while count_1 < value:
        print(num_f_1)
        num_f_3 = num_f_1 + num_f_2
        num_f_1 = num_f_2
        num_f_2 = num_f_3
        count_1 += 1

fibonacci(10)


# Genarte Fibonacci number using Class method.
class Fibonacci_sequence:
    def __init__(self, user_value):
        self.user_value = user_value
        self.n1 = 0
        self.n2 = 1
        self.count = 0


    def fibonacci_c_f(self):
        while self.count < self.user_value:
            print(self.n1)
            x = self.n1 + self.n2
            self.n1 = self.n2
            self.n2 = x
            self.count += 1


object_attribute = Fibonacci_sequence(10)

object_attribute.fibonacci_c_f()



