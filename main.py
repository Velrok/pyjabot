from jabberbot import JabberBot, botcmd
from docopt import docopt, DocoptExit

from share_episode import run as share_episode
import logging
import datetime
import os
import json
import re
import shows
import sys

logging.basicConfig() # getLogger("jabberbot").

def get_config(config_file=None):
  config_file = os.path.expanduser(config_file)
  return json.load(open(config_file))

# 
def make_nice_string(episodes):
  return "Found {episodes_len} episodes:\n{}".format(
      "\n".join(["{0} S{1:02}E{2:02}d".format(e["showname"], e["season#"], e["episode#"]) for e in episodes]),
      episodes_len=len(episodes)
  )

class TvButtler(JabberBot):
  def __init__(self, config):
    self.config = config

    user = config["username"]
    password = config["password"]
    host = config["host"]
    connection_string = "{}@{}".format(user, host)
    logging.info("starting bot {}".format(connection_string))

    super(TvButtler, self).__init__(connection_string, password)

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
    shows_dir = self.config["shows_dir"]
    shows = ""
    movies_dir = self.config["movies_dir"]
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
      return "Please use 'list tv' or 'list movies' to list the available shows/movies."

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

    shows_dir = self.config["shows_dir"]
    episodes  = shows.list(shows_dir)

    found_episodes = shows.find(episodes, pattern, season=season, episode=episode)
    nice_string = make_nice_string(found_episodes)
    return nice_string

  @botcmd
  def share(self, message, args):
    """
    Links/Copies the specified episode to the share folder.

    Usage:
      share tv <pattern> <season> <episode>
    """
    try:
      arguments  = docopt(self.share.__doc__, args.split(" "))
    except DocoptExit:
      return self.share.__doc__

    shows_dir = self.config["shows_dir"]
    share_dir = self.config["share_dir"]
    episodes  = shows.list(shows_dir)

    found_episodes = shows.find(episodes, arguments['<pattern>'],
                                season=arguments['<season>'],
                                episode=arguments['<episode>'])

    if len(found_episodes) == 0:
      return "No episode matched your criteria. Please try again or use 'find' to search first."
    elif len(found_episodes) > 1:
      return "Your showname must match only one episode. Please be more specific with the pattern."
    else:
      try:
        share_episode(found_episodes[0]['filepath'], share_dir)
      except IOError as ioe:
        return "Failed to share file: {}".format(ioe)
      return "File shared: {}".format(found_episodes[0]['filename'])

def start_bot(config):
  """Returns a new bot instance using the configured parameters."""

  if not os.path.exists(config['shows_dir']):
    print "[ERROR] Can't read shows_dir: ", config['shows_dir']
    sys.exit(1)

  if not os.path.exists(config['movies_dir']):
    print "[ERROR] Can't read movies_dir: ", config['movies_dir']
    sys.exit(2)

  return TvButtler(config)


def main(args):
  """
  Runs a bot for exporting your TV shows / Movies via BitTorrent Sync.

  Usage:
    python main.py [options]

  Options:
    -h --help             Shows this help.
    -c --config <config>  The config file to use. [default: ~/.config/pyjabot.json]
  """
  arguments  = docopt(main.__doc__, args)

  config_file = arguments['--config']
  config = get_config(config_file)
  logging.info("Loading configfile from {}: {}".format(config_file, config))

  bot = start_bot(config)
  bot.serve_forever()

if __name__ == "__main__":
  main(sys.argv)

