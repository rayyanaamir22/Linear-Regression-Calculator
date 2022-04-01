# EQUATIONS

# Modules
import math

# Other files
import functions as f

def linearRegressionAlgorithm():
  # Write out the line of best fit equation. Consider BEDMAS/PEMDAS

  # Separate the equation into numerator and demonimator for simplicity in calculating
  global aNumerator
  global aDenominator
  aNumerator = (f.n*sum(f.dataXY))-(sum(f.tDataX)*sum(f.tDataY))
  aDemonimator = (f.n*sum(f.squareX))-((sum(f.tDataX))**2)

  # Find a (slope of line of best fit)
  global a
  global b
  global verticalLine
  try:
    a = aNumerator/aDemonimator
    verticalLine = False
    
    # Use slope a and mean X and Y values to determine y-intercept b
    b = f.meanY - (a*f.meanX)
  except ZeroDivisionError:
    verticalLine = True
    a = 0
    b = 0
    print()


def correlationCoefficientAlgorithm():
  # The correlation coefficient represents a data set's covariance along with the direction of proportionality (direct or inverse)

  # Pearson correlation coefficient:
  global r # Let r represent the Pearson correlation coefficient
  
  # Not sure if this works
  rNumerator = f.n*sum(f.dataXY) - sum(f.tDataX)*sum(f.tDataY)
  rDenominator = math.sqrt((f.n*sum(f.squareX)-(sum(f.tDataX))**2)*(f.n*sum(f.squareY)-(sum(f.tDataY))**2))
  try:
    r = rNumerator/rDenominator
  except ZeroDivisionError: # This happens when all y coordinates are equal
    r = 0


  
  
  global rStrength # Overall correlation
  global rProportionality # Direct or inverse
  global ar
  ar = abs(r) # Absolute value for convenience
  if ar > 1: # r should always be within 1 and -1.
    print('Something went wrong; r ≯ ±1') # Is not greater than magnitude of 1
    rStrength = 'Error'
    rProportionality = 'Error'
    raise ValueError

  # FINDING PROPORTIONALITY AND STRENGTH
    
  # An r value of 0 means there is zero correlation between the data (extremely unlikely and coincidental)
  if r == 0:
    rProportionality = 'no'
  elif r > 0: # Directly proportional
    rProportionality = 'direct'
  elif r < 0: # Inversely proportional
    rProportionality = 'inverse'
  
  if r == 0:
    rStrength = 'no'
  elif ar > 0 and ar <= 0.33:
    rStrength = 'a weak'
  elif ar > 0.33 and ar <= 0.67:
    rStrength = 'a moderate'
  elif ar > 0.67 and ar < 1:
    rStrength = 'a strong'
  elif ar == 1:
    rStrength = 'a perfect'
