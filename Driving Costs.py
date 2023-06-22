gas_mileage = float(input())
gas_cost = float(input())

cost_per_mi = gas_cost / gas_mileage

print(f'{(20 * cost_per_mi):.2f} {(75 * cost_per_mi):.2f} {500 * cost_per_mi:.2f}')
