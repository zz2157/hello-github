"""最小示例：打印问候并演示一个函数的版本演进。"""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("GitHub"))
