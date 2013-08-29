from setuptools import setup, find_packages
setup(
    name = "pyjabot",
    version = "0.0.0",
    packages = find_packages(),
    install_requires = ['jabberbot>=0.15', 'xmpppy>=0.5.0rc1'],
    license = "MIT",
    keywords = "jabber bot",
    url = "https://github.com/Velrok/pyjabot"
)
