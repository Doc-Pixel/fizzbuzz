# @version >=0.3.8

@view
@external
def checkFB(i: uint256) -> String[78]:
    assert i > 0, "enter value greater than zero"
    if i % 3 == 0 and i % 5  == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        returnValue: String[78] = uint2str(i)
        return returnValue
