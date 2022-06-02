'''
Name: Rayyan A
Date: June 1, 2022
Program: Linear Regression Calculator 2.0
'''

'''
Goal:
- Remake the code but pass parameters through the functions to improve reusability
'''

# Modules
import os

# Other Files
import functions as f
import equations as e
import results as res
import goodbye as g

def main():
  while True:
    # Title
    print('LINEAR REGRESSION CALCULATOR\n')

    # Manually enter each data point
    data = f.createDataPoints()
    noOfPoints = len(data)
    
    if noOfPoints > 2: # There must be atleast 2 points for regression
      f.removeDataPoints(data)

    xCoords = []
    yCoords = []
    for xCoord in data:
      xCoords.append(xCoord)
      yCoords.append(data[xCoord])

    dataXY, meanX, meanY, squareX, squareY, stdX, stdY = f.miscValues(xCoords, yCoords)
  
    # DATA ANALYSIS FUNCTIONS
    
    # Calculate the line of best fit equation (y=ax+b)
    e.linearRegressionAlgorithm(noOfPoints, xCoords, squareX, yCoords, dataXY) 

    # Determine Pearson Correlation Coefficient
    e.correlationCoefficientAlgorithm(noOfPoints, xCoords, yCoords, squareX, squareY, dataXY)

    # Return the results
    res.correlationResults()

    # Create a graph using matplotlib.pyplot
    try:
      f.scatterPlot(xCoords, yCoords) 
    except:
      print('\nGraph is meaningless due to correlation coefficient of 0.')

    # Option to use model for a prediction
    if not res.dataUndefined:
      while True:
        print('\nDo you want to use the regression to predict a value?')
        pre = input()
        if pre.lower().startswith('y'):
          os.system('clear')
          f.predict()
          break
        elif pre.lower().startswith('n'):
          os.system('clear')
          break
        else:
          print('(Yes or no)')
  
    # Reuse program or exit
    if res.reuse():
      os.system('clear')
      continue
    else:
      os.system('clear')
      print(g.getFarewellStatement(g.farewellStatements),    end='.')
      break

# PROGRAM START
if __name__ == '__main__':
  main()

  '''
  Description:
  Linear regression is a mathematical technique to yield the most accurate line of best fit regarding ALL data points entered (including outliers). This program automates the entire calculation, and it only requires the user to enter the data points they want to find the linear regression of.

  How to use:
  When run, the program will ask the user to enter each data point manually as an ordered pair. First, the user must enter the X coordinate, followed by the corresponding Y coordinate. The program assumes that each pair entered in 1 round is an ordered pair. Also, linear regression is not possible with a single data point, so the program will not begin calculations until there is more than 1 (one) data point.

  Once finished, state that you are finished entering data points and the program will immediately calculate and return the linear regression, as well as several meaningful statistics constants like standard deviation and covariance.
  '''
  
# PROGRAM END
