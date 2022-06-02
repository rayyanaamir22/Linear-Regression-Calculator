# EQUATIONS

# Modules
import math

def linearRegressionAlgorithm(n, dataX, squareX, meanX, meanY, dataY, dataXY):
  # Write out the line of best fit equation. Consider BEDMAS/PEMDAS

  # Equations separated into numerator and demonimator for simplicity
  global aNumerator, aDenominator
  aNumerator = (n*sum(dataXY))-(sum(dataX)*sum(dataY))
  aDemonimator = (n*sum(squareX))-((sum(dataX))**2)

  # Find a (slope of line of best fit)
  global a, b
  try:
    a = aNumerator/aDemonimator
    verticalLine = False # Undefined slope
    
    # Use slope a and mean X and Y values to determine y-intercept b
    b = meanY - (a*meanX)
  except ZeroDivisionError:
    verticalLine = True
    a = None
    b = None

  return a, b, verticalLine

def correlationCoefficientAlgorithm(n, dataX, dataY, squareX, squareY, dataXY):
  # The correlation coefficient represents a data set's covariance along with the direction of proportionality (direct or inverse)

  global r # Let r represent the Pearson correlation coefficient
  
  rNumerator = n*sum(dataXY) - sum(dataX)*sum(dataY)
  rDenominator = math.sqrt((n*sum(squareX)-(sum(dataX))**2)*(n*sum(squareY)-(sum(dataY))**2))
  try:
    r = rNumerator/rDenominator
  except ZeroDivisionError: # This happens when all y coordinates are equal (undefined slope)
    r = 0
  del rNumerator, rDenominator
  
  global rStrength, rProportionality
  ar = abs(r) # Absolute value for convenience

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

  return r, rStrength, rProportionality
