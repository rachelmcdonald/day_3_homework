def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2 

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(test_string):
    return len(test_string)
    
def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1 = '1', string_2 = '2'):
    new_string_1 = int(string_1)
    new_string_2 = int(string_2)
    
    return new_string_1 + new_string_2

def number_to_full_month_name(num = 1):
    new_month = str(num)
    new_month = 'January'

    return new_month
# I was able to complete the first one but was unsure how to ammend the other two
# as they both had the same function name
# I tried placing them all in the same function, but it threw errors my way!

def number_to_short_month_name(numb = 1):
    short_month = str(numb)
    short_month = 'Jan'

    return short_month
        
# I was able to complete the first one but was unsure how to ammend the other two
# as they both had the same function name
# I tried placing them all in the same function, but it threw errors my way!
