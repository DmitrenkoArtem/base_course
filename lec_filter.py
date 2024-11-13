names=['vova','vlad']
ages=[72,1]
def checker(user):
    name,age=user
    return age>21
users=list(zip(names,ages))
canDrinkAlcohol=list(filter(checker,users))
print(canDrinkAlcohol)