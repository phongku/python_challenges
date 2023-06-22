def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost = dollars_per_gallon / miles_per_gallon * miles_driven
    return cost

if __name__ == '__main__':
    mpg = float(input())
    price_per_gallon = float(input())
    cost_10_miles = driving_cost(mpg, price_per_gallon, 10)
    cost_50_miles = driving_cost(mpg, price_per_gallon, 50)
    cost_400_miles = driving_cost(mpg, price_per_gallon, 400)
    print(f'{cost_10_miles:.2f}\n{cost_50_miles:.2f}\n{cost_400_miles:.2f}')


