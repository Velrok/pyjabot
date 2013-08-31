from setuptools import setup, find_packages
setup(
    name = "pyjabot",
    version = "0.0.0",
    packages = find_packages(),
    install_requires = ['jabberbot>=0.15', 'xmpppy>=0.5.0rc1',
      'nose>=1.3.0', 'pinocchio>=0.3.1', "sniffer>=0.3.2",
      "docopt>=0.6.1"],
    license = "MIT",
    keywords = "jabber bot",
    url = "https://github.com/Velrok/pyjabot"
)
