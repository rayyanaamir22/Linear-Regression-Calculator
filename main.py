'''
Name: Rayyan A
Date: March 22, 2022
Program: Linear Regression Calculator
'''

# Modules
import os

# Other Files
import functions as f
import equations as e
import results as res

# PROGRAM START

while True:
  
  # Title
  print('LINEAR REGRESSION CALCULATOR\n')

  # How to use 
  
    
  #f.createDataPoints()

  # DATA ANALYSIS FUNCTIONS

  # Convert imported data sets to Python-readable lists
  f.translateDatabase()
  print('X squared list: ', f.squared(f.dataX, f.squareX))
  print('Y squared list: ', f.squared(f.dataY, f.squareY))
  print('XY list: ', f.multiply(f.rCopyX, f.rCopyY))

  # Calculate the line of best fit equation (y=ax+b)
  e.linearRegressionAlgorithm() 

  # Determine data correlation values
  e.correlationCoefficientAlgorithm()

  # Return the results
  res.correlationResults()

  if res.reuse():
    continue
  else:
    os.system('clear')
    print('Thanks for using this program.')
    break

# PROGRAM END