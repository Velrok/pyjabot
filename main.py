from jabberbot import JabberBot, botcmd
from docopt import docopt, DocoptExit
import logging
import datetime
import os
import json
import re
import shows
import sys

logging.basicConfig() # getLogger("jabberbot").

def get_user_config_path():
  home = os.path.abspath(os.environ["HOME"])
  return os.path.join(home, ".config/pyjabot.json")

def get_config(config_file=None):
  if config_file is None:
    config_file = get_user_config_path()
  return json.load(open(config_file))

# 
def make_nice_string(episodes):
  return "Found {episodes_len} episodes:\n{}".format(
      "\n".join(["{0} S{1:02}E{2:02}d".format(e["showname"], e["season#"], e["episode#"]) for e in episodes]),
      episodes_len=len(episodes)
  )

class TvButtler(JabberBot):
  @botcmd
  def hello(self, message, args):
    return "Hello!"

  @botcmd
  def debug (self, message, args):
    """Print back the message and args values received by a method."""
    return "message \t{}\nargs \t{}".format(message, args)

  @botcmd
  def list (self, message, args):
    """
    Returns a list of all TV shows or movies
    Usage:
      list tv
      list movies
    Help:
      help list -> Shows this screen
    """
    config = get_config()
    shows_dir = config["shows_dir"]
    shows = ""
    movies_dir = config["movies_dir"]
    movies = ""

    if args.lower() == "tv":
      for show in os.listdir(shows_dir):
        shows += show + "\n"
      return shows

    elif args.lower() == "movies":
      for movie in os.listdir(movies_dir):
        movies += movie + "\n"
      return movies

    else:
      return "Sorry, command not available. Type help list for a list of commands."

  @botcmd
  def find(self, message, args):
    """
    Find episodes based on regex.

    usage:
      find <pattern> [<season_number> [<episode_number>]]

    """
    season = episode = None

    try:
      arguments  = docopt(self.find.__doc__, args.split(" "))
    except DocoptExit:
      return self.find.__doc__

    pattern   = arguments['<pattern>']
    if arguments['<season_number>'] != None:
        season    = int(arguments['<season_number>'])
    if arguments['<episode_number>'] != None:
        episode   = int(arguments['<episode_number>'])

    conf      = get_config()
    shows_dir = conf["shows_dir"]
    episodes  = shows.list(shows_dir)

    found_episodes = shows.find(episodes, pattern, season=season, episode=episode)
    nice_string = make_nice_string(found_episodes)
    return nice_string



def start_bot(config):
  """Returns a new bot instance using the configured parameters."""
  user = config["username"]
  password = config["password"]
  host = config["host"]
  connection_string = "{}@{}".format(user, host)

  if not os.path.exists(config['shows_dir']):
    print "[ERROR] Can't read shows_dir: ", config['shows_dir']
    sys.exit(1)

  if not os.path.exists(config['movies_dir']):
    print "[ERROR] Can't read movies_dir: ", config['movies_dir']
    sys.exit(2)

  print "starting bot {}".format(connection_string)
  return TvButtler(connection_string, password)


def main(args):
  """
  Runs a bot for exporting your TV shows / Movies via BitTorrent Sync.

  Usage:
    python main.py [--config <config>]
  """
  arguments  = docopt(main.__doc__, args)

  if arguments['--config'] and arguments['<config>'] is not None:
    config_file = arguments['<config>']
  else:
    config_file = get_user_config_path()

  config = get_config(config_file)
  logging.info("Loading configfile from {}: {}".format(config_file, config))

  bot = start_bot(config)
  bot.serve_forever()

if __name__ == "__main__":
  main(sys.argv)

