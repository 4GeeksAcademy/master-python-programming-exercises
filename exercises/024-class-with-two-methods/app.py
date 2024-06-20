# Your code here
class InputOutString:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print(self.input_string.upper())

string_object = InputOutString()
string_object.get_string()
string_object.print_string()
