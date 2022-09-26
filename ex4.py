import argparse


def knapsack(capacity: int, bars: list):
    sum_bars = sum(bars)
    # If knapsack is bigger than sum of bars, it can store all of them.
    if capacity >= sum_bars:
        return sum_bars

    # Let`s solve this task with dynamic programming.
    # This task is subset sum problem,
    # a variation of knapsack problems.
    bars = sorted(bars)
    row = [0] * (capacity + 1)  # plus zero item

    # Iterate over sorted list of bars
    for i in range(len(bars)):
        # We need to count cells from current bar value
        # to sum of bar values from first to current.
        # This regularity is got empirically.
        for j in range(min(sum(bars[0:i+1]), capacity), bars[i] - 1, -1):
            row[j] = max(row[j], row[j - bars[i]] + bars[i])

    return row[-1]


parser = argparse.ArgumentParser()
parser.add_argument('-W', '--capacity', type=int)
parser.add_argument('-w', '--weights', type=int, nargs='+')

# I don't know what is it for,
# so let's check if it is correct
parser.add_argument('-n', '--bars_number', type=int)
args = parser.parse_args()

if args.bars_number != len(args.weights):
    raise ValueError('Wrong bars number')

print(knapsack(args.capacity, args.weights))
