# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

numlist = [2, 3, 4, 5]
def odd_average(numlist):
    return sum(numlist) / len(numlist)

print(odd_average(numlist))
