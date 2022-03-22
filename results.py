# RESULTS

# Other files
import equations as e
import functions as f

def reuse():
  print('\nDo you want to reuse the Correlation Calculator?')
  reuse = input()
  if reuse.lower().startswith('y'):
    return True
  elif reuse.lower().startswith('n'):
    return False
  else:
    print('(Yes or no)')

def correlationResults(): # Return the equations' results
  
  # Line of best fit equation in y=ax+b form
  print('\nLine of best fit equation:\ny =', end=' ')
  if e.b > 0: # If y-int is positive
    print('{0}x + {1}' .format(e.a, e.b))
  elif e.b < 0: # If y-int is negative
    print('{0}x - {1}' .format(e.a, abs(e.b)))
  elif e.b == 0: # If y-int is zero
    print(e.a, 'x')

  # Correlation coefficient
  print('\nPearson Correlation Coefficient: ', e.r)
  print('The data has a {0}, {1} correlation.' .format(e.rStrength, e.rProportionality))
  
  # Covariance and Standard deviation
  '''
  print('Covariance: ', f.covariance, f.yAxis, '/', f.xAxis) # The unit of covariance is the quotient of the compared units
  '''
  
  print('\nStandard Deviation (X): ', f.deviationX) # Unitless
  print('Standard Deviation (Y): ', f.deviationY) # Unitless
  
  # Algorithm result





'''
Issues:
- Regression appears incorrect for inverse proportionalities
- If certain values equal 0, a zeroDivisionError occurs in the equations
'''