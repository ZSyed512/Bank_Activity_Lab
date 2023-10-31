
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        Averages = []
        for row in self.data:
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            A = stats.mean(new_row)
            Averages.append(round(A,3))
        
        return Averages

    def median02(self):
        """pt2
        """
        Medians = []
        for row in self.data:
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            Medians.append(stats.median(new_row))
        return Medians
    
    def stddev03(self):
        """pt3
        """
        StDeviations = []
        for row in self.data:
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            S = stats.stdev(new_row)
            StDeviations.append(round(S,3))
        
        return StDeviations
