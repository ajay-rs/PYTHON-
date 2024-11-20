def generator_demo():
    yield "One"
    yield "Two"
    yield "Three"

gd = generator_demo()
print(type(gd))

print(next(gd))
print(next(gd))
print(next(gd))
