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




