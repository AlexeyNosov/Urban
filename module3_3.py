from main import print_hi


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=11)
print_params(c=[1, 2, 3])
values_list = [ "one", 1, False]
values_dict = { "a" : "100", "b" : "200", "c" : "300"}
print_params(values_list)
print_params(values_dict)
print_params(*values_list)
print_params(**values_dict)
value_list_2 = ["ski", 1000]
print_params(*value_list_2, 7)
