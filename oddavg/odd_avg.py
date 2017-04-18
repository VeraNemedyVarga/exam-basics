# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases


class CountAverage(object):

    def odd_average(self, numlist):
        self.list_of_odd_numbers = []
        self.numlist = numlist
        if len(self.numlist) == 1 and self.numlist[0] % 2 == 0:
            return "ZeroDivisionError, element is even in list"

        elif len(self.numlist) != 0:
            for self.number in self.numlist:
                if self.number % 2 == 1:
                    self.list_of_odd_numbers.append(self.number)
            return sum(self.list_of_odd_numbers)/ len(self.list_of_odd_numbers)

        else:
            return "ZeroDivisionError, please do not enter empty list"
