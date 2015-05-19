from delnone import delnone

def test_delnone_terminal():
  assert delnone(123) == 123
  assert delnone("abc") == "abc"
  assert delnone(None) == None

def test_delnone_dict():
  assert delnone({}) == {}
  assert delnone({"matt":"andrew"}) == {"matt":"andrew"}
  assert delnone({"matt":None}) == {}
  assert delnone({"matt":"andrew", "nick":None}) == {"matt":"andrew"}

def test_delnone_dict_recurse():
  assert delnone({"matt": {"test":None}}) == {"matt": {}}

def test_delnone_list():
  assert delnone([]) == []
  assert delnone(["matt"]) == ["matt"]
  assert delnone([None]) == []
  assert delnone(["matt", None]) == ["matt"]

def test_delnone_list_recurse():
  assert delnone([{"value":None}]) == [{}]

