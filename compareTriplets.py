def compareTriplets(a, b):
    # Write your code here
    alicePoints = 0
    bobPoints = 0

    for i in range(0, len(a)):
        if (a[i] < b[i]):
            bobPoints = bobPoints + 1
        elif (a[i] > b[i]):
            alicePoints = alicePoints + 1
    return [alicePoints,bobPoints]