"""
input: array containing sub arrays
output: sum of lesser numbers in all sub arrays

loop over the given array
loop over each inner element
add the smallest number to the output variable
return output variable
"""
arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def inner_adition(arr):
    output = 0
    for item in arr:
        output += min(item)
    return output


print(inner_adition(arr))
