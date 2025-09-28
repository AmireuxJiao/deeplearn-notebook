class app:
    def __init__(self):
        self.routes = {}
        return

    def route(self, path, method="GET"):
        def decorator(func):
            key = (method.upper(), path)
            self.routes[key] = func
            return func

        return decorator

    def get(self, path):
        return self.route(path, method="GET")

    def post(self, path):
        return self.route(path, method="POST")

    def call(self, path, method="GET", *args, **kwargs):
        key = (method.upper(), path)
        if key in self.routes:
            return self.routes[key](*args, **kwargs)
        else:
            return f"404 Not Found: {path}"


app = app()


# 使用装饰器注册路由
@app.get("/hello")
def hello(name="World"):
    return f"Hello, {name}!"


@app.post("/echo")
def echo(data):
    return f"Echo: {data}"


# 模拟请求
print(app.call("/hello", method="GET", name="Luna"))
print(app.call("/echo", method="POST", data="Some message"))
print(app.call("/echo", method="GET"))  # 错误方法
print(app.call("/notfound", method="GET"))
