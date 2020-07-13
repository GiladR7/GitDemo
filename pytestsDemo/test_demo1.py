import pytest

from pytestsDemo.LoggingDemo import LogClass


@pytest.mark.usefixtures("setup" , "Datetype")
class Test_Demo1(LogClass):
    def test_print(self , Datetype):
        Log = self.getlogger()
        Log.info("This is the info message ")





    def test_print1(self):
        print("i will run first ")

    def test_print2(self):
        print("i will run first ")