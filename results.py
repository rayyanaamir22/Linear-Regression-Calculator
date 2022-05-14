# RESULTS

# Other files
import equations as e
import functions as f

def reuse():
  reuse = ''
  while not reuse.lower().startswith('y') or reuse.lower().startswith('n'):
    print('\nDo you want to reuse the Correlation Calculator?')
    reuse = input()
    if reuse.lower().startswith('y'):
      return True
    elif reuse.lower().startswith('n'):
      return False
    else:
      print('(Yes or no)')

def correlationResults(): # Return the equations' results
  # Plot the graph
  #f.scatterPlot()
  
  # Show inputted data points for user to compare
  print('Original Data Points:')
  for i in range(len(f.dataX)):
    # Print each point as an ordered pair
    print('({0}, {1})' .format(f.dataPoints[0], f.dataPoints[1]))
    # Remove the first ordered pair
    f.dataPoints.pop(0)
    f.dataPoints.pop(0)

  # Line of best fit equation in y=ax+b form
  global slope, intercept, equation
  global roundedSlope, roundedIntercept, roundedEquation
  if e.verticalLine == False: # Account for all scenarios
    # Create 'ax' component
    if e.a == 1.0: # Slope does not need to be shown
      slope = 'x'
      roundedSlope = slope
    elif e.a == 0: # If a = 0 (horizontal line)
      slope = ''
      roundedSlope = slope
    elif e.a == -1: # just a negative symbol
      slope = '-x'
      roundedSlope = slope
    else:
      slope = '{0}x' .format(e.a)
      roundedSlope = '{0}x' .format(round(e.a, 3))

    # Create intercept component
    if e.b > 0: # If y-int is positive
      intercept = ' + ' + str(e.b)
      roundedIntercept = ' + ' +str(round(e.b, 3))
    elif e.b < 0: # If y-int is negative
      intercept = ' - ' + str(abs(e.b))
      roundedIntercept = ' - ' +str(round(abs(e.b), 3))
    elif e.b == 0: # If y-int is zero
      intercept = ''
      roundedIntercept = intercept

    # Concatenate equation
    equation = str(slope + intercept) # On console
    roundedEquation = str(roundedSlope + roundedIntercept) # On graph
    print('\nLinear Regression (Line of best fit equation):\ny = ' + equation)

  elif e.verticalLine == True: # THIS DOES NOT WORK IDKY
    print('\nLinear Regression (Line of best fit equation): x =', f.tdataY[0])

  # Correlation coefficient
  print('\nPearson Correlation Coefficient (r): ', e.r)
  print('The data has {0} correlation of {1} proportionality.' .format(e.rStrength, e.rProportionality))
  if e.ar == 1.0:
    print('Since |r| = 1, all data points exist on the linear function above.')
  
  # Covariance and Standard deviation
  ''' # Not sure how to display covariance
  print('Covariance: ', f.covariance, f.yAxis, '/', f.xAxis) # The unit of covariance is the quotient of the compared units
  '''
  
  print('\nStandard Deviation (X): ', f.stdX) # Unitless
  print('Standard Deviation (Y): ', f.stdY) # Unitless
  
  
  # Algorithm result
  # Neural network?
