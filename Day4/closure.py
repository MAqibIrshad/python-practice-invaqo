def outer():
    name = "MAqib"
    def inner():
        print(f"Name: {name}")

    return inner


out = outer()
out()
