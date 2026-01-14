from hello_world import say_hello

if __name__ == "__main__":
    if say_hello() == "hello world":
        print("Test passed")
    else:
        print("Test failed")