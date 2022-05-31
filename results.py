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
    print(f'({f.dataX[i]}, {f.dataY[i]})')

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
      slope = f'{e.a}x'
      roundedSlope = f'{round(e.a, 3)}x'

    # Create intercept component
    if e.b > 0: # If y-int is positive
      intercept = f' + {e.b}'
      roundedIntercept = f' + {round(e.b, 3)}'
    elif e.b < 0: # If y-int is negative
      intercept = f' - {abs(e.b)}'
      roundedIntercept = f' - {round(abs(e.b), 3)}'
    elif e.b == 0: # If y-int is zero
      intercept = ''
      roundedIntercept = intercept

    # Concatenate equation
    equation = str(slope + intercept) # On console
    roundedEquation = str(roundedSlope + roundedIntercept) # On graph
    print(f'\nLinear Regression (Line of best fit equation):\ny = {equation}')

  else: # THIS DOES NOT WORK IDKY
    print('Data is undefined')

  # Correlation coefficient
  print(f'\nPearson Correlation Coefficient (r): {e.r}')
  print(f'The data has {e.rStrength} correlation of {e.rProportionality} proportionality.')
  if e.ar == 1.0:
    print('Since |r| = 1, all data points exist on the linear function above.')
  
  # Covariance and Standard deviation
  print(f'\nStandard Deviation (X): {f.stdX}') 
  print(f'Standard Deviation (Y): {f.stdY}')
