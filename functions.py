# FUNCTIONS

# Modules
import numpy as np # Math
import time # Misc
import os # Misc
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import matplotlib.pyplot as plt # For graphing
import pylab # For naming graph

# Other files
import equations as e
import results as res

# Take the dataPoints dictionary and display it as coordinates
def displayCurrentArray(dataPoints):
  print('Current Array:\n')
  for index, xCoord in enumerate(dataPoints):
    print(f'{index+1}. ({xCoord}, {dataPoints[xCoord]})')

    if index == len(dataPoints):
      print('\n')
      break

def createDataPoints():
  global dataPoints
  dataPoints = {} # Save each coordinate as a key-value pair
  
  dataComplete = False
  
  while dataComplete == False:
    # X COORDINATES
    while True:
      try: # Try statement will force input to be a number
        dataInput = float(input('Enter X value: '))
        if type(dataInput) == float or type(dataInput) == int: # If input is a number
          newCoordX = dataInput
          break
        else:
          os.system('clear')
          print('Please enter a number.')
      except (TypeError, ValueError): # If original input was not a number
        os.system('clear')
        print('Please enter a number.')

    # Y COORDINATES (mostly same as X)
    yIsValid = False # Variable to account for the nested loop
    while yIsValid == False:
      try: # Try statement will force input to be a number
        dataInput = float(input('Enter Y value: '))
        if type(dataInput) == float or type(dataInput) == int: # If input is a number
          newCoordY = dataInput
          yIsValid = True
          # When adding Y coordinate, the user can state that the list is finished and exit this process.

          dataPoints[newCoordX] = newCoordY # Add the data point as a new key-value pair in format: { x : y }
    
          while True: 
            os.system('clear')
            displayCurrentArray(dataPoints)
            print('\nDo you want to add more points?')
            concludeData = input()
            if concludeData.lower().startswith('n'): # If yes
              if len(dataPoints) < 2: # Not enough points
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
    
  del dataComplete, yIsValid

  return dataPoints
  
# CONVERT DATA TO LISTS for equations
# Recursively create list of squared values
def squared(data, squareData):
  if len(squareData) == n: # BASE CASE: If list is complete...
    return squareData
  else:
    squareData.append(data[0]**2) # Append squared value
    data.pop(0)
    return squared(data, squareData)

# Recursively create list of XY dot products
def dotProduct(data1, data2):
  if len(dataXY) == n: # BASE CASE: If list is complete...
    return dataXY
  else:
    dataXY.append(data1[0] * data2[0]) # Append product of ordered pair
    data1.pop(0) 
    data2.pop(0)
    return dotProduct(data1, data2)

# CONVERT DATA TO LISTS for equations

# Option to remove any data points from the list before or after calculation
def removeDataPoints(dataPoints):
  while True:
    # Display a list of the points as ordered pairs
    os.system('clear')
    displayCurrentArray(dataPoints)
    
    print('\nDo you want to remove any data points?')
    remove = input()

    # Verify input
    if remove.lower().startswith('n'): # Exit
      break
    elif len(dataPoints) <= 2 and remove.lower().startswith('y'):
      print('There must be atleast 2 data points for regression.')
      time.sleep(3) # Delay so user can read
      break
    elif remove.lower().startswith('y'): # Can remove points
      while True:
        print('Enter the index denoting the point to be removed:')
        try:
          remove = int(input())
          if remove > len(dataPoints) or remove < 1: # Since x counts the index, it is equal to the number of data points available
            print('Index out of range.')
          else: # If valid, remove coordinate at that index
            dataPoints.pop(remove-1)

            break
        except (ValueError, TypeError):
          print('Invalid input.')
    else:
      os.system('clear')

  os.system('clear')
  del remove

def miscValues(dataX, dataY):
  # Data is finalized, now prepare for equation
  global copyX1, copyX2, copyX3
  global copyY1, copyY2, copyY3
  global n, meanX, meanY, squareX, squareY, stdX, stdY
  squareX = []
  squareY = []  
  
  # XY is the product of an x coordinate and its corresponding y coordinate
  global dataXY
  dataXY = []

  n = len(dataX) # Used in recursion

  # Means
  meanX = np.mean(dataX)
  meanY = np.mean(dataY)
  # Standard Deviations
  stdX = np.std(dataX)
  stdY = np.std(dataY)
  
  # Create copies of data for recursion
  copyX1 = dataX[:]
  copyX2 = dataX[:] 
  copyX3 = dataX[:]
  copyY1 = dataY[:] # Need a more efficient way for this
  copyY2 = dataY[:]
  copyY3 = dataY[:]

  # Recursion
  squared(copyX1, squareX) # Create list of squared X values
  squared(copyY1, squareY) # Create list of squared Y values
  dotProduct(copyX2, copyY2) # Create list of XY dot products

  del copyX1, copyX2, copyY1, copyY2
  return dataXY, meanX, meanY, squareX, squareY, stdX, stdY
  
  
def scatterPlot(dataX, dataY):
  # Convert data to numpy array
  x = np.array(dataX)
  y = np.array(dataY)

  # Put data points on the plane
  plt.scatter(x, y, color="red")

  # Plot linear regression as infinite line
  plt.axline((1, e.a+e.b), slope=e.a, color="blue", label="y = " + res.roundedEquation)
  
  # Set axis
  plt.xlim(dataX[0] - 3*np.mean(dataX), dataX[-1] + 3*np.mean(dataX))
  plt.ylim(dataY[0] - 3*np.mean(dataY), dataY[-1] + 3*np.mean(dataY))

  # GRAPH
  plt.axhline(y=0, color="black") # X-axis
  plt.xlabel("X-axis")
  plt.axvline(x=0, color="black") # Y-axis
  plt.ylabel("Y-axis")
  plt.title("Correlation Model")
  plt.legend(loc='best')

  # Window title
  fig = pylab.gcf()
  fig.canvas.manager.set_window_title('Linear Regression')

  # Display 
  plt.show(block=False) # Let code continue running
  del x, y

# Predictive function
def predict(a, b):
  while True:
    print('Do you want to predict the function at a given X or Y value?')
    varToGive = input()
    if varToGive.lower().startswith('x'):
      varToGive = 'X'
      break
    elif varToGive.lower().startswith('y'):
      varToGive = 'Y'
      break
    print('(X or Y)')

  while True:
    print(f'Enter {varToGive} value:')
    try:
      varGiven = float(input())
      break
    except TypeError:
      print('Please enter a number.')

  # Calculate and show varToGive on same graph as regression
  if varToGive == 'X':
    y = (a)*varGiven+(b)
    print(f'y = {a}({varGiven}) + {b}\n y = {y}')
    plt.plot(varGiven, y, 'ro')
  else:
    x = (varGiven-(b))/(a)
    print(f'{varGiven} = {a}x + {b}\n x = {x}')
    plt.plot(x, varGiven, 'ro') 
    
