user_request = str(input("write a word: "))

class Reverce:

    def __init__(self, string_value):
        self.x = string_value

    def revers_function(self):
        return self.x[::-1]

reversed = Reverce(user_request)
result = reversed.revers_function()
print(result)