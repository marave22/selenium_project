from form.base_page import Base
import pytest

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    pass
    # def test_2(self):
    #     driver = self.driver
    #     print(driver)