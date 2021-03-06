from nose.tools import eq_, ok_
import shows

shows_dir = "fixtures/fs/shows/"
castle_mkv = "Castle (2009)/Castle (2009) - 5x01 - After The Storm.mkv"
castle_banner = "Castle (2009)/banner.jpg"
true_blood_nfo = "/True Blood/Season 06/True Blood - S06E05 - Let's Boot and Rally - HD TV.nfo"

def test_extract_meata_data_returns_none_if_file_does_not_contain_meta_data():
  eq_(shows.extract_meta_data(castle_banner),
      None)

def test_extract_meata_data_finds_file_extention():
  eq_(shows.extract_meta_data(true_blood_nfo)['ext'],
      "nfo")
  eq_(shows.extract_meta_data(castle_mkv)['ext'],
      "mkv")

def test_extract_meata_data_finds_file_season_number():
  eq_(shows.extract_meta_data(true_blood_nfo)["season#"],
      6)
  eq_(shows.extract_meta_data(castle_mkv)["season#"],
      5)

def test_extract_meata_data_finds_file_episode_number():
  eq_(shows.extract_meta_data(true_blood_nfo)["episode#"],
      5)
  eq_(shows.extract_meta_data(castle_mkv)["episode#"],
      1)

def test_extract_meata_data_finds_season_title():
  eq_(shows.extract_meta_data(castle_mkv)['showname'],
      "Castle (2009)")
  eq_(shows.extract_meta_data(true_blood_nfo)['showname'],
      "True Blood")

def test_shows_list_returns_an_entry_for_every_file():
  eq_(len(shows.list(shows_dir)),
      10)

def test_shows_list_each_entr_has_a_filepath():
  for e in shows.list(shows_dir):
    ok_(e.has_key("filepath"))

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


def test_shows_find_returns_2_True_Blood_Entrys():
  result = shows.find(all_episodes, "True Blood")
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

def test_shows_find_returns_1_Warehouse_Entry():
  result = shows.find(all_episodes, "Warehouse")
  expectation = [{'filepath': "Warehouse 13/Season 02/Warehouse 13 2x5.mkv",
  'showname': "Warehouse 13",
  'episode#': 5,
  'season#': 2,
  'ext': "mkv"}]
  eq_(result, expectation)

def test_shows_find_returns_TrueBlood_EP10():
  result = shows.find(all_episodes, "True Blood", episode=10)
  expectation = [{'filepath': "True Blood/Season 06/True Blood 6x10.mkv",
  'showname': "True Blood",
  'episode#': 10,
  'season#': 6,
  'ext': "mkv"}]
  eq_(result, expectation)

def test_shows_find_returns_2_for_Castle_Season_1():
  result = shows.find(all_episodes, "Castle", season=1)
  expectation = [
      {'filepath': "Castle (2013)/Season 01/Castle (2013) - 1x2.mkv",
       'showname': "Castle (2013)",
       'episode#': 2,
       'season#': 1,
       'ext': "mkv"}]
  eq_(result, expectation)

