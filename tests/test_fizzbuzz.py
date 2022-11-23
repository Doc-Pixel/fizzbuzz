import pytest
from brownie import accounts, Contract

##### test fixtures #####
@pytest.fixture
def fbContract(fizzbuzz, scope="module", autouse=True):
    yield accounts[0].deploy(fizzbuzz)


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


def test_checkFB(fbContract):
    assert fbContract.checkFB(1) == '1'
    assert fbContract.checkFB(3) ==  'fizz'
    assert fbContract.checkFB(5) ==  'buzz'
    assert fbContract.checkFB(15) ==  'fizzbuzz'