import pytest
from app import MathOperations

@pytest.mark.it("The 'MathOperations' class should exist")
def test_math_operations_class_exists():
    try:
        assert MathOperations
    except AttributeError:
        raise AttributeError("The class 'MathOperations' should exist in app.py")


@pytest.mark.it("The MathOperations class includes the 'calculate_circle_area' class method")
def test_math_operations_has_calculate_circle_area_class_method():
    assert hasattr(MathOperations, "calculate_circle_area")


@pytest.mark.it("The 'calculate_circle_area' class method should return the expected circle area")
def test_calculate_circle_area_class_method_returns_expected_area():
    result = MathOperations.calculate_circle_area(5)
    assert result == 78.53975

@pytest.mark.it("The 'calculate_circle_area' class method should return the expected circle area. Testing with different values")
def test_calculate_circle_area_class_method_returns_expected_area_for_radius_10():
    result = MathOperations.calculate_circle_area(10)
    assert result == 314.159
