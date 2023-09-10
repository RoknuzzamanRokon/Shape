

for x in range(10,300):
    z = str(x)
    y = z[::-1]
    if z == y:
        print(f"its palindrome {x}")

    else:
        pass
        # print(f"its not palindrome {x}")


# using only function
def check_palindrome(value):
    revers = str(value)[::-1]
    return revers

for x in range(10,100):
    if check_palindrome(x) == str(x):
        print(f"palindrome {x}")
    else:
        pass

# using class base function


class Perindromes:
    def __init__(self, string_value):
        self.value = string_value

    def function(self):
        return self.value[::-1]


user = str(input("input a number: "))

revarce_str = Perindromes(user)

revarce_str_result = revarce_str.function()
print(revarce_str_result)

if user == revarce_str_result:
    print("This is palindrome : ")
else:
    print("No it is not palindrome: ")


