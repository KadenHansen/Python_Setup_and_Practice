def hello():
    print("Hello!")
hello()

def pack(item1, item2, item3):
    list = [item1, item2, item3]
    return list
print(pack("sandwich", "apple", "pudding"))

def eat_lunch(*items):
    if items:
        for i in items:
            if i == items[0]:
                print(f"First I eat my {i}")
            else:
                print(f"Next I eat my {i}")
    else:
        print("My lunchbox is empty!")
eat_lunch('sandwich', "apple", "pudding")