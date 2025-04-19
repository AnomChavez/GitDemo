# Any pytest file should start with test_ or end with _test
# Pytest method names should start with test
#Any code should be wrapped in method only
#Method names should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
# you can mark (tag) tests and then run with -m, @pytest.mark.smoke
# you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used for setup and tear down methods for test cases- conftest file to generalize fixture
#and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


#@pytest.mark.smoke
#@pytest.mark.skip

def test_GreetProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 ==6, "Addition do not match"


@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")






