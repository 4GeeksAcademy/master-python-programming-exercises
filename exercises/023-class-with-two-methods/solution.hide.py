class input_out_string(object):
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = raw_input()

    def print_String(self):
        print self.s.upper()

str_obj = input_out_string()
str_obj.get_string()
str_obj.print_String()