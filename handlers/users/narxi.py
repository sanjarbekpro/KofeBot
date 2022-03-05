price = {
    'Sazan(300g)' : 45000,
    'Sudak(300g)' : 48000,
    'Sous(300ml)' : 7000,
    'Coca-cola(0,5 l)' : 5000,
    'Fanta(0,5 l)' : 5000,
    'Coca-cola(1,5 l)' : 12000,
    'Fanta(1,5 l)' : 12000,
    'Мишель' : 30000,
    'Мясо по-французски' : 28000,
    'Fri 🍟' : 10000
    }


def get_price(name, amaunt):
    narx = price[name]
    return narx  * amaunt