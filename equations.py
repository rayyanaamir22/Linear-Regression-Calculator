# EQUATIONS

# Modules
import math

# Other files
import functions as f

def linearRegressionAlgorithm():
  # Write out the line of best fit equation. Consider BEDMAS/PEMDAS

  # Separate the equation into numerator and demonimator for simplicity in calculating
  aNumerator = (f.n*sum(f.dataXY))-(sum(f.dataX)*sum(f.dataY))
  aDemonimator = (f.n*sum(f.squareX))-((sum(f.dataX))**2)

  # Find a (slope of line of best fit)
  global a
  a = aNumerator/aDemonimator

  # Use slope a and mean X and Y values to determine y-intercept b
  global b
  b = f.meanY - (a*f.meanX)


def correlationCoefficientAlgorithm():
  # The correlation coefficient represents a data set's covariance along with the direction of proportionality (direct or inverse)

  # Pearson correlation coefficient:
  global r # Let r represent the Pearson correlation coefficient
  
  # Not sure if this works
  #r = covariance / (deviationX * deviationY)
  rNumerator = f.n*sum(f.dataXY) - sum(f.dataX)*sum(f.dataY)
  rDenominator = math.sqrt((f.n*sum(f.squareX)-math.sqrt(sum(f.dataX)))*((f.n*sum(f.squareY)-sum(f.dataY))))
  
  r = rNumerator/rDenominator
  ar = abs(r) # Absolute value for convenience
  
  global rStrength # Overall correlation
  global rProportionality # Direct or inverse
  # r should always be within 1 and -1.
  if ar > 1:
    print('Something went wrong; r ≯ ±1') # Is not greater than magnitude of 1
    rStrength = 'Error'
    rProportionality = 'Error'
    raise ValueError

  # FINDING PROPORTIONALITY AND STRENGTH
    
  # An r value of 0 means there is zero correlation between the data (extremely unlikely and coincidental)
  if r == 0:
    rProportionality = None
  elif r > 0: # Directly proportional
    rProportionality = 'direct'
  elif r < 0: # Inversely proportional
    rProportionality = 'inverse'
  
  if r == 0:
    rStrength = None
  elif ar > 0 and ar <= 0.33:
    rStrength = 'weak'
  elif ar > 0.33 and ar <= 0.67:
    rStrength = 'moderate'
  elif ar > 0.67 and ar < 1:
    rStrength = 'strong'
  elif ar == 1:
    rStrength = 'perfect'