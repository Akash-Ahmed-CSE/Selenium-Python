ItemsInCart = 0

if ItemsInCart !=2:
    pass
assert(ItemsInCart ==0)

#tyr, catch

try:
    with open('akahs.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("this code will run even my code fails.")