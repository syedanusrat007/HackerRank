def compareTriplets(a, b):
    # Write your code here
    return [sum(x > y for x, y in zip(a, b)), sum(x < y for x, y in zip(a, b))]
