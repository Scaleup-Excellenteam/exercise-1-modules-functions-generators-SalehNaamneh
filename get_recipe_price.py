
def get_recipe_price(prices:dict,optional=None,**kwargs )->int:
    finalPrice = 0
    if optional is None:
        optional = []
    for key,value in kwargs.items():
        if key not in optional:
            finalPrice += prices[key]*(value//100)
    return finalPrice



    return
if __name__ == '__main__':
    print(get_recipe_price({'ch':18,'milk':8},ch=200,milk=100))
