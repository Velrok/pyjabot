from nose.tools import nottest
def test_true():
  assert True

@nottest
def test_fail():
  assert False