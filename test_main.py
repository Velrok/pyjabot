from main import *
from nose.tools import nottest, eq_

all_episodes = [
  {'filepath': "True Blood/Season 06/True Blood 6x10.mkv",
  'showname': "True Blood",
  'episode#': 10,
  'season#': 6,
  'ext': "mkv"},
  {'filepath': "True Blood/Season 06/True Blood 6x11.mkv",
  'showname': "True Blood",
  'episode#': 11,
  'season#': 6,
  'ext': "mkv"},
  {'filepath': "Warehouse 13/Season 02/Warehouse 13 2x5.mkv",
  'showname': "Warehouse 13",
  'episode#': 5,
  'season#': 2,
  'ext': "mkv"},
  {'filepath': "Castle (2013)/Season 01/Castle (2013) - 1x2.mkv",
  'showname': "Castle (2013)",
  'episode#': 2,
  'season#': 1,
  'ext': "mkv"},
  {'filepath': "Castle (2013)/Season 02/Castle (2013) - 2x5.mkv",
  'showname': "Castle (2013)",
  'episode#': 5,
  'season#': 2,
  'ext': "mkv"}
  ]


def test_maiks_filter_returns_2_True_Blood_Entrys():
  result = maiks_filter(all_episodes, "True Blood")
  expectation = [{'filepath': "True Blood/Season 06/True Blood 6x10.mkv",
  'showname': "True Blood",
  'episode#': 10,
  'season#': 6,
  'ext': "mkv"},
  {'filepath': "True Blood/Season 06/True Blood 6x11.mkv",
  'showname': "True Blood",
  'episode#': 11,
  'season#': 6,
  'ext': "mkv"}]
  eq_(result, expectation)

def test_maiks_filter_returns_1_Warehouse_Entry():
  result = maiks_filter(all_episodes, "Warehouse")
  expectation = [{'filepath': "Warehouse 13/Season 02/Warehouse 13 2x5.mkv",
  'showname': "Warehouse 13",
  'episode#': 5,
  'season#': 2,
  'ext': "mkv"}]
  eq_(result, expectation)

def test_maiks_filter_returns_TrueBlood_EP10():
  result = maiks_filter(all_episodes, "True Blood", episode=10)
  expectation = [{'filepath': "True Blood/Season 06/True Blood 6x10.mkv",
  'showname': "True Blood",
  'episode#': 10,
  'season#': 6,
  'ext': "mkv"}]
  eq_(result, expectation)

def test_maiks_filter_returns_2_for_Castle_Season_1():
  result = maiks_filter(all_episodes, "Castle", season=1)
  expectation = [
      {'filepath': "Castle (2013)/Season 01/Castle (2013) - 1x2.mkv",
       'showname': "Castle (2013)",
       'episode#': 2,
       'season#': 1,
       'ext': "mkv"}]
  eq_(result, expectation)

