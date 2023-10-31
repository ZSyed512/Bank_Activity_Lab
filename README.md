# README


## Project Intro/Objective
The purpose of this project is to engineer a pipeline to analyze stock data in python. We will achieve this by implementing classes and use Object Oriented programming and documentation reading skills to complete the pipeline. The piepline will compute the Average, Median and Standard Deviation of 9 weeks of sample stock data


### Methods Used
* Inferential Statistics
* Machine Learning
* Object Oriented Programming 
* Classes

### Technologies
* Python
* VSCode

## Project Description
I was given a repository that represents an incomplete data engineering project with a goal to satisfy the purpose described above. The sample dataset that was provided contains 9 weeks of data. Utilizing object oriented programming, I first completed the Average function to compute the average of stock prices from the given list of lists data. Since the data was in string format and also contained missing values, I first iterated over each row of self.data within the average01 function of the stockmetrics class. I converted the string values to float values and also skipped over any missing values. After computing the average for each row, I appended the Averages list with the value of the average for each row and finally returned the Averages list. I followed the same procedure for the median and standard deviation functions as well. At the end, I used the validate file to check that my code was working correctly.
