# FUNCTIONS

# Modules
import numpy as np
import os

# User creates their custom array of data points
def createDataPoints():
  
  global dataPoints
  dataPoints = []
  global dataInput
  global dataComplete
  dataComplete = False
  while dataComplete == False:

    # X COORDINATES
    while True:
      try: # Try statement will force input to be a number
        dataInput = float(input('Enter X value: '))
        if type(dataInput) == float or type(dataInput) == int: # If input is a number
          dataPoints.append(dataInput) # Add it to the list
          break
        else:
          os.system('clear')
          print('Please enter a number.')
      except (TypeError, ValueError): # If original input was not a number
        os.system('clear')
        print('Please enter a number.')

    # Y COORDINATES (mostly same as X)
    yValid = False # Variable to account for the nested loop
    while yValid == False:
      try: # Try statement will force input to be a number
        dataInput = float(input('Enter Y value: '))
        if type(dataInput) == float or type(dataInput) == int: # If input is a number
          dataPoints.append(dataInput) # Add it to the list
          yValid = True
          # When adding Y coordinate, the user can state that the list is finished and exit this process.
          while True: 
            os.system('clear')
            print('Current array: ', dataPoints)
            print('\nDo you want to add more points?')
            concludeData = input()
            if concludeData.lower().startswith('n'): # If yes
              if len(dataPoints)/2 == 1: # Not enough points
                print('There must be atleast 2 data points.\n')
                dataComplete = False
                break
              else:
                dataComplete = True # The outermost loop will stop running
                os.system('clear')
                break 
            elif concludeData.lower().startswith('y'): #If no
              break
            else:
              print('(Answer yes or no)') # If invalid input
        else:
          os.system('clear')
          print('Please enter a number.')
      except (TypeError, ValueError): # If original input was not a number
        os.system('clear')
        print('Please enter a number.')

# CONVERT DATA TO LISTS for equations
def translateDatabase():
  # Assign a variable for each component of the data being imported. They will be used for the impending statistics equations.

  # Use names of imported data
  global xAxis
  global yAxis
  xAxis = 'xAxis'
  yAxis = 'yAxis'
  
  # Let n represent the number of data points being imported
  global n
  #n = len(dataPoints)/2 
    
  
  # Let x represent the independent variable; the presumed cause of sea otter population decline
  global dataX
  global tDataX
  global meanX
  global squareX
  global rCopyX
  dataX = []
  dataX.append(dataPoints[::2]) # Every other value (from 0)
  dataX = [i for j in dataX for i in j] # Strip double brackets
  tDataX = tuple(dataX) # Create a tuple of dataX
  rCopyX = list(dataX) # Copy for recursion
  n = len(dataX)
  meanX = np.mean(dataX)
  squareX = []
  
  # Let y represent the dependent variable; the sea otter population itself
  global dataY
  global tDataY
  global meanY
  global squareY
  global rCopyY
  dataY = []
  dataY.append(dataPoints[1::2]) # Every other value (from 1)
  dataY = [i for j in dataY for i in j] # Strip double brackets
  tDataY = tuple(dataY) # Create a tuple of dataY
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
