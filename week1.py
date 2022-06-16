def simpleArraySum(ar):
    # Write your code here
    # To determine the size of array ar
    n = len(ar)
    # To initialize the sum of the elements of array ar
    sum = 0
    # To iterate through the elements of the array ar
    # while summing the elements from first index to last
    for i in range(0, len(ar)):
        sum = sum + ar[i]
    # To return the total sum
    return sum