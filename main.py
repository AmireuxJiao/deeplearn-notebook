def hello(func):
    def wapper():
        print("begin function call")
        func()
        print("end function call")
    return wapper

@hello
def say_hello_world():
    print("hello world")
    
say_hello_world()