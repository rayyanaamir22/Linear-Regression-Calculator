'''
Name: Rayyan A
Date: June 6, 2022
Program: Linear Regression Calculator 2.0
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
    data = f.createDataPoints() # data is a dictionary which stores each coordinate as an x:y pair
    noOfPoints = len(data)
    
    if noOfPoints > 2: # Must be atleast 2 points for regression
      f.removeDataPoints(data)

    # Put the coordinates into their own lists
    xCoords = []
    yCoords = []
    for xCoord in data:
      xCoords.append(xCoord)
      yCoords.append(data[xCoord])

    # Use the lists to get values used in linear regression
    dataXY, meanX, meanY, squareX, squareY, stdX, stdY = f.miscValues(xCoords, yCoords) # std is extra

    # Convert the lists to tuples so they remain unaltered
    xCoords, yCoords = tuple(xCoords), tuple(yCoords)
    
    # DATA ANALYSIS FUNCTIONS
    
    # Calculate the line of best fit equation (y=ax+b)
    slope, intercept, undefined = e.linearRegressionAlgorithm(noOfPoints, xCoords, squareX, meanX, meanY, yCoords, dataXY) 

    # Calculate the Pearson Correlation Coefficient
    r, strength, proportionality = e.correlationCoefficientAlgorithm(noOfPoints, xCoords, yCoords, squareX, squareY, dataXY)

    # Show the results
    res.correlationResults(data, stdX, stdY, slope, intercept, r, strength, proportionality, undefined)
    
    # Interpret
    res.interpretData(slope)
    
    # Create a graph using matplotlib.pyplot
    if not undefined: 
      f.scatterPlot(xCoords, yCoords) 

      # Option to use model for a prediction
      while True:
        print('\nDo you want to use the regression to predict a value?')
        pre = input()
        if pre.lower().startswith('y'):
          os.system('clear')
          f.predict(slope, intercept)
          break
        elif pre.lower().startswith('n'):
          os.system('clear')
          break
        else:
          print('(Yes or no)')
    else:
      os.system('clear')
      print('ERROR: Regression was undefined.')
      
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
# PROGRAM END
