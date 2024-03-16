class Product:
    def __init__(self, name = 'codetree', code = 50):
        self.name = name
        self.code = code


name , code = map(str, input().split())

product = Product()
print("product {} is {}".format(product.code, product.name))

product.name = name
product.code = int(code)


print("product {} is {}".format(product.code, product.name))