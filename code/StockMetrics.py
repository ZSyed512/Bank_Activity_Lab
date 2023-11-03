
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    #Function to compute the averages and add them to a list
    def average01(self):
        """pt1
        """
        #Creating empty list to store averages
        Averages = []
        #for loop to iterate through all rows in self.data
        for row in self.data:
            #List comprehension. Since all values are originally in string format, float(val) is 
            # used to convert them to floating point.
            # for val in row [1:] iterates through all values in the list and if val !="" checks if any 
            # of the values are an empty string, if they are it does not include them, it only includes values that 
            # are not empty.
            # val != " " checks if any value contains a space in the string, if so it is not included
            new_row = [float(val) for val in row[1:] if val !="" and val !=" "]
            # Computing the mean and assigning it to variable A
            A = stats.mean(new_row)
            #Appending the Averages list with A(the mean value) and rounding it to 3 decimal places
            Averages.append(round(A,3))
        #Returning Averages list
        return Averages

    #Function to compute the medians and add them to a list
    def median02(self):
        """pt2
        """
         #Creating empty list to store Medians
        Medians = []
        #for loop to iterate through all rows in self.data
        for row in self.data:
             #List comprehension. Since all values are originally in string format, float(val) is 
            # used to convert them to floating point.
            # for val in row [1:] iterates through all values in the list and if val !="" checks if any 
            # of the values are an empty string, if they are it does not include them, it only includes values that 
            # are not empty.
            # val != " " checks if any value contains a space in the string, if so it is not included
            new_row = [float(val) for val in row[1:] if val !="" and val !=" "]
             # Computing the median and appending it to list Medians
            Medians.append(stats.median(new_row))
        #Returning Medians list
        return Medians
    
    #Function to compute the standard deviations and add them to a list
    def stddev03(self):
        """pt3
        """
        #Creating empty list to store Standard Deviations
        StDeviations = []
        #for loop to iterate through all rows in self.data
        for row in self.data:
            #List comprehension. Since all values are originally in string format, float(val) is 
            # used to convert them to floating point.
            # for val in row [1:] iterates through all values in the list and if val !="" checks if any 
            # of the values are an empty string, if they are it does not include them, it only includes values that 
            # are not empty.
            # val != " " checks if any value contains a space in the string, if so it is not included
            new_row = [float(val) for val in row[1:] if val !="" and val !=" "]
              # Computing the Standard Deviation and assigning it to variable S
            S = stats.stdev(new_row)
             #Appending the StDeviations list with S(the Standard Deviation value) and rounding it to 3 decimal places
            StDeviations.append(round(S,3))
        #Returning StDeviations list
        return StDeviations
