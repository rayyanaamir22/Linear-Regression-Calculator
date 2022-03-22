# FUNCTIONS

# Modules
import numpy as np
import os

# User creates their custom 2D array of data points
def createDataPoints():
  
  global userArray
  userArray = []
  global arrayInput
  global arrayComplete
  arrayComplete = False
  while arrayComplete == False:
    try: # Try statement will force input to be an integer
      arrayInput = int(input('Enter data points as ordered pairs. (X, Y)'))
      if type(arrayInput) == int: # If input is valid
        userArray.append(arrayInput) # Add it to the list
        while True: # Program asks user if they are finished the array
          os.system('clear')
          print('Current array: ', userArray)
          print('\nIs array complete?')
          concludeArray = input()
          
          if concludeArray.lower().startswith('y'): # If yes
            arrayComplete = True # The outermost loop will stop running
            break
          elif concludeArray.lower().startswith('n'): # If no
            break
          else:
            print('(Answer yes or no)') # If invalid input
      else:
        os.system('clear')
        print('Please enter a whole number.')
    except (TypeError, ValueError): # If original input was not an integer
      os.system('clear')
      print('Please enter an integer.')

# Assign the data points under the lists used in the program
def translateDatabase():
  # Assign a variable for each component of the data being imported. They will be used for the impending statistics equations.

  # Use names of imported data
  global xAxis
  global yAxis
  xAxis = 'yAxis'
  yAxis = 'xAxis'
  
  # Let n represent the number of data points being imported
  global n
  
  # Let x represent the independent variable; the presumed cause of sea otter population decline
  global dataX
  global meanX
  global squareX
  global rCopyX
  dataX = [1,2,3] # Should these be converted to tuples?
  rCopyX = list(dataX) # Copy for recursion
  n = len(dataX)
  meanX = np.mean(dataX)
  squareX = []
  
  # Let y represent the dependent variable; the sea otter population itself
  global dataY
  global meanY
  global squareY
  global rCopyY
  dataY = [3,2,1]
  rCopyY = list(dataY) # Copy for recursion
  meanY = np.mean(dataY)
  squareY = []
  
  # Let xy represent the product of x and y in their respective ordered pairs
  global dataXY
  dataXY = []
  
  # Covariance and Standard Deviation
  global covariance
  global deviationX
  global deviationY
  # Covariance is a measure of how strongly two connected variables X adn Y affect eachother.
  
  covariance = np.cov(dataX, dataY) 
  # Standard Deviation is the frequency to deviate from the main stream
  
  deviationX = np.std(dataX)
  deviationY = np.std(dataY)

# The squaring recursion is not working

# Use recursion to create list of squared values
def squared(data, squareData):
  if len(squareData) == n: # BASE CASE: If list is complete...
    return squareData
  else:
    squareData.append(data[0]**2) # Append squared x value
    data.pop(0)
    return squared(data, squareData)

# Use recursion to create list of the products of dataX and dataY
def multiply(data1, data2):
  if len(dataXY) == n: # BASE CASE: If list is complete...
    return dataXY
  else:
    dataXY.append(data1[0] * data2[0]) # Append product of ordered pair
    data1.pop(0) 
    data2.pop(0)
    return multiply(data1, data2)

def comperehensionAlgorithm():
  # This algorithm will yield solutions to the problem
  print()
