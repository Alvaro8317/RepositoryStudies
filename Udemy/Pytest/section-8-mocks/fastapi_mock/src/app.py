import random
import time
from fastapi import FastAPI

web_app = FastAPI()


class Foo:
    def retorna_string_foo(self):
        return "string"

    def retorna_is_a_number(self):
        return random.choice(["string", "123"])


def retorna_string():
    return "string"


@web_app.get("/")
async def index():
    return "Pytest"


@web_app.get("/timeout")
async def timeout():
    time.sleep(6)


@web_app.get("/api")
def api():
    return retorna_string()


@web_app.get("/api/v2")
def api_v2():
    return Foo().retorna_string_foo()


@web_app.get("/api/v3")
def api_v3():
    result = Foo().retorna_is_a_number()
    if result.isnumeric():
        return "is a number"
    return "is not a number"
