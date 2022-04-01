'''
Name: Rayyan A
Date: April 1, 2022
Program: Linear Regression Calculator
'''

# Modules
import os

# Other Files
import functions as f
import equations as e
import results as res
import goodbye as g

# PROGRAM START

while True:
  # Title
  print('LINEAR REGRESSION CALCULATOR\n')

  # How to use

  f.createDataPoints()

  # DATA ANALYSIS FUNCTIONS

  # Convert imported data sets to Python-readable lists
  f.translateDatabase()

  # For equations
  f.squared(f.dataX, f.squareX) # Produce squareX
  f.squared(f.dataY, f.squareY) # Produce squareY
  f.multiply(f.rCopyX, f.rCopyY) # Produce dataXY

  # Calculate the line of best fit equation (y=ax+b)
  e.linearRegressionAlgorithm() 

  # Determine data correlation values
  e.correlationCoefficientAlgorithm()

  # Return the results
  res.correlationResults()
  
  if res.reuse():
    os.system('clear')
    continue
  else:
    os.system('clear')
    print(g.getFarewellStatement(g.farewellStatements), end='.')
    break
  
# PROGRAM END
