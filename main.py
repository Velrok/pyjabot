from jabberbot import JabberBot, botcmd
import datetime
import os
import json

def get_config_path():
  home = os.path.abspath(os.environ["HOME"])
  return os.path.join(home, ".config/pyjabot.json")

def get_config():
  return json.load(open(get_config_path()))

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
      return "Sorry, command not avabile. Type help list for a list of commands."
    



def start_bot():
  """Returns a new bot instance using the configured parameters."""
  config = get_config()
  print "config loaded from {}: {}".format(get_config_path(), config)

  user = config["username"]
  password = config["password"]
  host = config["host"]
  connection_string = "{}@{}".format(user, host)

  print "starting bot {}".format(connection_string)
  return TvButtler(connection_string, password)

if __name__ == "__main__":
  bot = start_bot()
  bot.serve_forever()



