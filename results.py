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
  # Show inputted data points for user to compare
  print('Original Data Points:')
  for i in range(len(f.tDataX)):
    # Print each point as an ordered pair
    print('({0}, {1})' .format(f.dataPoints[0], f.dataPoints[1]))
    # Remove the first pair of XY coordinates
    f.dataPoints.pop(0)
    f.dataPoints.pop(0)

  # Line of best fit equation in y=ax+b form
  if e.verticalLine == False: # Account for all scenarios
    print('\nLinear Regression (Line of best fit equation):\ny =', end=' ')

    # IMPROVE THIS
    if e.a == 1: # slope does not need to be shown
      e.a = ''
    if e.a == 0: # If a = 0 (horizontal line)
      print(e.b)
    elif e.a == -1: # just a negative symbol
      e.a = '-'
    elif e.b > 0: # If y-int is positive
      print('{0}x + {1}' .format(e.a, e.b))
    elif e.b < 0: # If y-int is negative
      print('{0}x - {1}' .format(e.a, abs(e.b)))
    elif e.b == 0: # If y-int is zero
      print(e.a, 'x')

    elif e.verticalLine == True: # THIS DOES NOT WORK IDKY
      print('\nLinear Regression (Line of best fit equation): x =', f.tdataY[0])

  # Correlation coefficient
  print('\nPearson Correlation Coefficient: ', e.r)
  print('The data has {0} correlation of {1} proportionality.' .format(e.rStrength, e.rProportionality))
  if e.ar == 1.0:
    print('Since |r| = 1, all data points exist on the linear function above.')
  
  # Covariance and Standard deviation
  ''' # Not sure how to display covariance
  print('Covariance: ', f.covariance, f.yAxis, '/', f.xAxis) # The unit of covariance is the quotient of the compared units
  '''
  
  print('\nStandard Deviation (X): ', f.deviationX) # Unitless
  print('Standard Deviation (Y): ', f.deviationY) # Unitless
