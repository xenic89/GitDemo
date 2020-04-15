import pytest

from pytetdemo.BaseClass import BaseClass


@pytest.mark.usefixtures("data_Load")
class Test_example2(BaseClass):

    def test_editProfile(self, data_Load):
        log = self.test_getLogger()
        log.info(data_Load[0])
        #print(data_Load)
        #print(data_Load[0])

        print(data_Load[2])
