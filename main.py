class App:
    def __init__(self):
        self.routes = {}
        return

    def get(self, path):
        def decorator(func):
            # 注册：把函数和路径绑定
            self.routes[path] = func
            return func

        return decorator

    def call(self, path, *args, **kwargs):
        if path in self.routes:
            return self.routes[path](*args, **kwargs)
        else:
            return f"404 Not Found: {path}"
        return


app = App()


@app.get("/hello")
def hello(name="World"):
    return f"Hello, {name}!"


@app.get("/bye")
def bye():
    return


print(app.call("/hello", "Luna"))
print(app.call("/bye"))
print(app.call("/unkown"))

