# FUNCTIONS

# Modules
import numpy as np # Math
import time # Misc
#from scipy import stats
import matplotlib.pyplot as plt # For graphing
import pylab # For naming graph
import os # Misc

# Other files
import equations as e
import results as res

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
            print(f'Current array: {dataPoints}')
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
  del dataComplete, yValid
    
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
def translateData():
  # Assign a variable for each component of the data being imported. They will be used for the impending statistics equations.
  
  # Let x represent the independent variable
  global dataX, meanX, squareX
  dataX = []
  dataX.append(dataPoints[::2]) # Every other value (from 0)
  dataX = [i for j in dataX for i in j] # Strip double brackets
  squareX = []
  
  # Let y represent the dependent variable
  global dataY, meanY, squareY
  dataY = []
  dataY.append(dataPoints[1::2]) # Every other value (from 1)
  dataY = [i for j in dataY for i in j] # Strip double brackets
  squareY = []
  
  # Let xy represent the product of x and y in their respective ordered pairs
  global dataXY
  dataXY = []

# Option to remove any data points from the list before or after calculation
def removeDataPoints():
  while True:
    # Display a list of the points as ordered pairs
    os.system('clear')
    print('Current array:\n')
    index = 1
    x = 0
    y = 0
    for point in dataX: # Print each data point as an ordered pair with an index
      print(f'{index}. ({dataX[x]}, {dataY[y]})')
      index += 1
      x += 1
      y += 1
    
    print('Do you want to remove any data points?')
    remove = input()

    # Verify input
    if remove.lower().startswith('n'): # pass
      break
    elif len(dataX) == 2:
      print('There must be atleast 2 data points for regression.')
      time.sleep(3) # Delay so user can read
      break
    elif remove.lower().startswith('y'): # Remove points
      while True:
        print('Enter the index denoting the point to be removed:')
        try:
          remove = int(input())
          if int(remove) > x: # Since x counts the index, it is equal to the number of data points available
            print('Index out of range.')
          else: # If valid, removal procedure
            dataX.pop(remove - 1) # Since index starts at 0, subtract 1 from the value of remove
            dataY.pop(remove - 1)

            break
        except (ValueError, TypeError):
          print('Invalid input.')
    else:
      os.system('clear')

  os.system('clear')
  del index, x, y

def miscValues():
  # Data is finalized, assign values derived from it like avg
  global copyX1, copyX2, copyX3
  global copyY1, copyY2, copyY3
  global n, meanX, meanY, stdX, stdY

  # Number of data points
  n = len(dataX)
  # Means
  meanX = np.mean(dataX)
  meanY = np.mean(dataY)
  # Standard Deviations
  stdX = np.std(dataX)
  stdY = np.std(dataY)
  
  # Create copies of data for recursion
  copyX1 = dataX[:]
  copyX2 = dataX[:] 
  copyX3 = dataX[:] # Is there a more convenient way to do this?
  copyY1 = dataY[:]
  copyY2 = dataY[:]
  copyY3 = dataY[:]

  # Recursion
  squared(copyX1, squareX) # Create list of squared X values
  squared(copyY1, squareY) # Create list of squared Y values
  dotProduct(copyX2, copyY2) # Create list of XY dot products

  del copyX1, copyX2, copyY1, copyY2
  
def scatterPlot():
  # Trying to resolve the cache warning but neither of these work :(
  #os.environ['MPLCONFIGDIR'] = '/opt/myapplication/.config/matplotlib'
  #os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
  
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
def predict():
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
    y = (e.a)*varGiven+(e.b)
    print(f'y = {e.a}({varGiven}) + {e.b}\n y = {y}')
    plt.plot(varGiven, y, 'ro') # Doesn't show on same graph
  else:
    x = (varGiven-(e.b))/(e.a)
    print(f'{varGiven} = {e.a}x + {e.b}\n x = {x}')
    plt.plot(x, varGiven, 'ro') # Same issue
    
