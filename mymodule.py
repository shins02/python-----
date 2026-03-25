def my_add(a,b) :
    return a+b

def my_sub(a,b) :
    return a-b

print(f"mymodule 안에서의__name__: {__name__}")

if __name__ == "__main__":
    print(my_add(11, 22))
    print(my_sub(11, 22))