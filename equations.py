# EQUATIONS

# Modules
import math

# Other files
import functions as f

def linearRegressionAlgorithm(n, dataX, squareX, dataY, dataXY):
  # Write out the line of best fit equation. Consider BEDMAS/PEMDAS

  # Equations separated into numerator and demonimator for simplicity
  global aNumerator
  global aDenominator
  aNumerator = (n*sum(dataXY))-(sum(dataX)*sum(dataY))
  aDemonimator = (n*sum(squareX))-((sum(dataX))**2)

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

def correlationCoefficientAlgorithm(n, dataX, dataY, squareX, squareY, dataXY):
  # The correlation coefficient represents a data set's covariance along with the direction of proportionality (direct or inverse)

  # Pearson correlation coefficient:
  global r # Let r represent the Pearson correlation coefficient
  
  rNumerator = n*sum(dataXY) - sum(dataX)*sum(dataY)
  rDenominator = math.sqrt((n*sum(squareX)-(sum(dataX))**2)*(n*sum(squareY)-(sum(dataY))**2))
  try:
    r = rNumerator/rDenominator
  except ZeroDivisionError: # This happens when all y coordinates are equal (undefined slope)
    r = 0
  del rNumerator, rDenominator
  
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
