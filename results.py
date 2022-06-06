# RESULTS

# Other files
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
  
  # Line of best fit equation in y=ax+b form
  global roundedSlope, roundedIntercept, roundedEquation

  # Variables starting with 'd' are for display
  if not verticalLine:
    # Create slope 'ax' component
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
    if dSlope == '':
      if b == 0:
        dSlope = ''
        dIntercept = '0'
        roundedIntercept = dIntercept
      else:
        dIntercept = roundedIntercept = str(b) # No need to print +/- before
    else:
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
    # Maybe say 'x=aConstant' instead of this
    print('The regression is undefined')
    
  # Correlation coefficient
  print(f'\nPearson Correlation Coefficient (r): {r}')
  print(f'The data has {strength} correlation of {proportionality} proportionality.')
  if abs(r) == 1.0:
    print('Since |r| = 1, all data points exist on the linear function above.')
  
  # Covariance and Standard deviation
  print(f'\nStandard Deviation (X): {stdX}') 
  print(f'Standard Deviation (Y): {stdY}')
  
  # Algorithm result
def interpretData(slope):
  if slope > 0:
    print("The growth rate for this population is ", slope, "If this rate continues, the population could see a ")
  elif slope < 0 > 2:
    print("The decline rate for this population is ", slope, "The species is currently on it's way of becoming scarce")
  elif slope > 2:
    print("The decline rate for this species is ", slope, "There is a good possibility that this species is heading towards endangerment and in extreme cases, extinction")
    
  elif slope == 1:
   print("The population is stable, reasons for this include but are not limited to: not having enough data, the species has not made a significant impact, or teh species has reached its equilibrium within its environment")

  # Algorithm result
