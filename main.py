'''
Name: Rayyan A
Date: May 14, 2022
Program: Linear Regression Calculator
'''

# Modules
import os
import matplotlib.pyplot as plt

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
    f.scatterPlot() 
  
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
  
# PROGRAM END
