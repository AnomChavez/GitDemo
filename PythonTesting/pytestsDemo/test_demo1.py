# Any pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in method only
# method name should have sense, so that you can use reg expressions to refer to them specifically
# -k stands for method names execution (reg expression), -s logs in/out put, -v stands for more info (verbose)
# Can run a specific file with py.test <filename>
# can use @pytest.mark.xfail to run a method without reporting on pass or fail status, for logistical purposes

import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

