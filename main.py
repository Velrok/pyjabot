from jabberbot import JabberBot, botcmd
import datetime
import os
import json

def get_config_path():
  home = os.path.abspath(os.environ["HOME"])
  return os.path.join(home, ".config/pyjabot.json")

def get_config():
  return json.load(open(get_config_path()))

#class SystemInfoJabberBot(JabberBot):
#    def bla(self):
#      pass
#
#    @botcmd
#    def serverinfo(self, mess, args):
#        """Displays information about the server"""
#        version = open('/proc/version').read().strip()
#        loadavg = open('/proc/loadavg').read().strip()
#
#        return '%s\n\n%s' % ( version, loadavg, )
#
#    @botcmd
#    def time( self, mess, args):
#        """Displays current server time"""
#        return str(datetime.datetime.now())
#
#    @botcmd
#    def rot13( self, mess, args):
#        """Returns passed arguments rot13'ed"""
#        return args.encode('rot13')
#
#    @botcmd
#    def whoami(self, mess, args):
#        """Tells you your username"""
#        return mess.getFrom().getStripped()
#
#username = 'my-jabberid@jabberserver.example.org'
#password = 'my-password'
#bot = SystemInfoJabberBot(username,password)
#bot.serve_forever()

class TvButtler(JabberBot):
  @botcmd
  def hello(self, message, args):
    return "Hello!"

  @botcmd
  def debug (self, message, args):
    return "message \t{}\nargs \t{}".format(message, args)

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



