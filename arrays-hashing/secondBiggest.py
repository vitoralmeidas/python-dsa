# get the second greatest number

def secondBiggest(arr):
    # get the first biggest number
    # get the second biggest number
    # if the first biggest number is bigger than the second biggest number, return the first biggest number
    # else return the second biggest number
    first = 0
    second = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[first]:
            second = first
            first = i
        elif arr[i] > arr[second]:
            second = i
    return arr[first] if arr[first] > arr[second] else arr[second]
