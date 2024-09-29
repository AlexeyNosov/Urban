def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string_lenth = len(string)
    string_up = string.upper()
    string_down = string.lower()
    return string_lenth, string_up, string_down
def in_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    for j in range(len(list_to_search)):
        if string in list_to_search[j]:
            mark = True
            break
        else:
            mark = False
    return mark
calls = 0
print(string_info("LasPalmas"))
print(string_info("FRRRReeeee"))
print(in_contains("One", ["Barebone", "CollOne", "pantOne1"]))
print(in_contains("ball", ["footBall", "Baloon", "bai"]))
print(in_contains("sport", ["spot", "spartak", "spirt"]))
print("Calls=",calls)


