import pytest
from LinearRegressor import LinearRegressor

def test_init_AND_repr() -> None:
    # __init__
    myModel = LinearRegressor(1.5, 73.8)
    assert myModel.slope == 1.5, 'Slope is incorrect'
    assert myModel.y_int == 73.8, 'Y-intercept is incorrect'

    # __repr__
    assert myModel.__repr__() == 'y = 1.5x + 73.8', '__repr__ is incorrect'

def test_fit() -> None:
    myModel = LinearRegressor
    X = [1, 2, 3]
    y = [0, 1, 2]
    myModel.fit(myModel, X, y)

    assert myModel.slope == 1.0, 'Slope is incorrect'
    assert myModel.y_int == -1.0, 'Y-intercept is incorrect'


if __name__ == "__main__":
    pytest.main(["Linear Regression Model 2/test_LinearRegressor.py"])