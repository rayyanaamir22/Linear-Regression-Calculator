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

def correlationResults(data, stdX, stdY, a, b, r, strength, proportionality, verticalLine): # Return the equations' results
  # Display original points
  f.displayCurrentArray(data)
  dataUndefined = False 
  
  # Line of best fit equation in y=ax+b form
  global roundedSlope, roundedIntercept, roundedEquation

  # Variables starting with 'd' are for display
  if not verticalLine: # Account for all scenarios
    # Create 'ax' component
    if a == 1.0: # Slope does not need to be shown
      dSlope = 'x'
      roundedSlope = dSlope
    elif a == 0: # If a = 0 (horizontal line)
      dSlope = ''
      roundedSlope = dSlope
    elif a == -1: # just a negative symbol
      dSlope = '-x'
      roundedSlope = dSlope
    else:
      dSlope = f'{a}x'
      roundedSlope = f'{round(a, 3)}x'

    # Create intercept component
    if b > 0: # If y-int is positive
      dIntercept = f' + {b}'
      roundedIntercept = f' + {round(b, 3)}'
    elif b < 0: # If y-int is negative
      dIntercept = f' - {abs(b)}'
      roundedIntercept = f' - {round(abs(b), 3)}'
    elif b == 0: # If y-int is zero
      dIntercept = ''
      roundedIntercept = dIntercept

    # Concatenate equation
    equation = str(dSlope + dIntercept) # For console
    roundedEquation = str(roundedSlope + roundedIntercept) # For graph
    print(f'\nLinear Regression (Line of best fit equation):\ny = {equation}')

  else: 
    print('Data is undefined')
    dataUndefined = True
    
  # Correlation coefficient
  print(f'\nPearson Correlation Coefficient (r): {r}')
  print(f'The data has {strength} correlation of {proportionality} proportionality.')
  if abs(r) == 1.0:
    print('Since |r| = 1, all data points exist on the linear function above.')
  
  # Covariance and Standard deviation
  print(f'\nStandard Deviation (X): {stdX}') 
  print(f'Standard Deviation (Y): {stdY}')
  
  # Algorithm result
