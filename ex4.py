import argparse


def max_knapsack_weight(capacity, weights):
    n_bars = len(capacity)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n_bars + 1)]
    for i in range(n_bars):
        for j in range(capacity):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif int(weights[i - 1]) <= j:
                table[i][j] = max(
                    int(weights[i - 1]) + table[i - 1][j - int(weights[i - 1])],
                    table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]

    return table[n_bars][capacity]


parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, dest='capacity')
parser.add_argument('-w', type=int, dest='weights', nargs='+')
parser.add_argument('-n', type=int, dest='n_bars')
args = parser.parse_args()

# it's not clear what is -n for,
# because we can use len(weights),
# so let's just add a check if the value is valid
if args.n_bars != len(args.weights):
    raise ValueError('Wrong number of bars')

print(max_knapsack_weight(args.capacity,
                          args.weights))
