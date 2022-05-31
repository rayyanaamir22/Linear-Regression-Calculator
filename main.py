'''
Name: Rayyan A
Date: May 31, 2022
Program: Linear Regression Calculator
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

    # Give an option to import points from a database or manually enter the coordinates
    f.createDataPoints()
    # Convert imported data sets to Python-readable lists
    f.translateData()

    if len(f.dataX) > 2: # There must be atleast 2 points for regression
      f.removeDataPoints()
    else:
      pass
    
    f.miscValues()
  
    # DATA ANALYSIS FUNCTIONS
    
    # Calculate the line of best fit equation (y=ax+b)
    e.linearRegressionAlgorithm() 

    # Determine Pearson Correlation Coefficient
    e.correlationCoefficientAlgorithm()

    # Return the results
    res.correlationResults()

    # Create a graph using matplotlib.pyplot
    try:
      f.scatterPlot() 
    except:
      print('\nGraph is meaningless due to correlation coefficient of 0.')

    # Option to use model for a prediction
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
