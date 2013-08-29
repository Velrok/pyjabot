# from jabberbot import JabberBot, botcmd
import datetime
import os
import json

def get_config_path():
  home = os.path.abspath(os.environ["HOME"])
  return os.path.join(home, ".pyjabot-config.json")

def get_config():
  return json.load(open(get_config_path()))

#class SystemInfoJabberBot(JabberBot):
#    @botcmd
#    def serverinfo( self, mess, args):
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
