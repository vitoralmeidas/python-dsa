def generatePascalTriangle(numRows):
    res = [[1]]  # the inner array is the first row
    for i in range(numRows - 1):  # -1 because we already have the first one
        temp = [0] + res[-1] + [0]  # first loop -> [0, 1, 0]  ... [0,1,1,0]...
        print("temp", temp)
        newRow = []
        # the range is the last row's length + 1, because in every row the length increses by 1
        for j in range(len(res[-1]) + 1):
            newRow.append(temp[j] + temp[j+1])
        res.append(newRow)
    return res

# time complexity - O(N²)


print(generatePascalTriangle(5))
