import pytest
from app import Student

@pytest.mark.it("The Student class should exist")
def test_student_class_exists():
    try:
        assert Student
    except AttributeError:
        raise AttributeError("The class 'Student' should exist in app.py")

@pytest.mark.it("The Student class includes the 'name' attribute")
def test_student_has_name_attribute():
    student = Student("John", 21, 75)
    assert hasattr(student, "name")

@pytest.mark.it("The Student class includes the 'age' attribute")
def test_student_has_age_attribute():
    student = Student("John", 21, 75)
    assert hasattr(student, "age")

@pytest.mark.it("The Student class includes the 'grade' attribute")
def test_student_has_grade_attribute():
    student = Student("John", 21, 75)
    assert hasattr(student, "grade")

@pytest.mark.it("The Student class includes the 'introduce' method")
def test_student_has_introduce_method():
    student = Student("Alice", 22, 90)
    assert hasattr(student, "introduce")

@pytest.mark.it("The introduce method should return the expected string. Testing with different values")
def test_student_introduce_method_returns_expected_string():
    student1 = Student("Alice", 22, 90)
    student2 = Student("Bob", 19, 85)
    assert student1.introduce() == "Hello! I am Alice, I am 22 years old, and my current grade is 90."
    assert student2.introduce() == "Hello! I am Bob, I am 19 years old, and my current grade is 85."

@pytest.mark.it("The Student class includes the 'study' method")
def test_student_has_study_method():
    student = Student("John", 21, 75)
    assert hasattr(student, "study")

@pytest.mark.it("The study method should return the expected string. Testing with different values")
def test_student_study_method_returns_expected_string():
    student1 = Student("Eve", 20, 78)
    student2 = Student("Charlie", 23, 88)
    assert student1.study(3) == "After studying for 3 hours, Eve's new grade is 79.5."
    assert student2.study(2) == "After studying for 2 hours, Charlie's new grade is 89.0."
