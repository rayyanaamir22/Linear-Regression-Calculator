# Model

class LinearRegressor():
    def __init__(self, slope, y_int) -> None: # Can initialize with values if given
        self.slope = slope
        self.y_int = y_int
    
    def __repr__(self) -> str:
        if (self.slope != 0 and self.y_int != 0):
            return f'y = {self.slope}x + {self.y_int}'
        elif (self.slope == 0 and self.y_int != 0):
            return f'y = {self.y_int}'
        elif (self.slope != 0 and self.y_int == 0):
            return f'y = {self.slope}x'
        else:
            return 'y = 0'

    def square(self, array: list[float]) -> list[float]:
        '''
        Given an array, return a new array with each item in the original array squared.
        '''
        return [i**2 for i in array]

    def dotProduct(self, X: list[float], y: list[float]) -> list[float]:
        '''
        Given parallel lists of the explanatory and response variable, return the dot product.
        '''
        return [X[i]*y[i] for i in range(len(X))]

    def mean(self, array: list[float]) -> float:
        '''
        Return the arithmetic mean of a 1D array
        '''
        return sum(array) / len(array)

    # Fit the model
    def fit(self, X: list[float], y: list[float]) -> None:
        '''
        Given parallel lists of the explanatory variable and response variable, 
        return the linear regression equation of the data.
        '''
        # Values for regression formula
        if len(X) == len(y):
            if (len(X) != 0):
                n = len(X)
            else:
                print("ERROR: X or y is empty.")
                return None
        else:
            print("ERROR: Parallel lists X and y are off different lengths.")
            return None
        squareX = self.square(self, X)
        dotProduct_XY = self.dotProduct(self, X, y)

        # Linear regression formula, divided in 2 to better handle ZeroDivisionError
        numerator = ((n * sum(dotProduct_XY)) - (sum(X) * sum(y)))
        denominator = ((n * sum(squareX)) - (sum(X) ** 2))

        # Form equation
        try:
            self.slope = numerator/denominator
            self.y_int = self.mean(self, y) - self.slope*self.mean(self, X)
        except ZeroDivisionError:
            print("ERROR: slope is undefined.")
            return None

    def predict(self, X: float) -> float:
        '''
        Predict the value of y at a given value of X.
        '''
        try:
            return self.slope * X + self.y_int
        except NameError:
            print("ERROR: Model must be fitted before predicting.")