# pyjabot

## install
```
git clone git@github.com:Velrok/pyjabot.git
pip install -e pyjabot
```

Note: "pip install -e" expects folder containing **setup.py** e.g. github/pyjabot

## configure 

`cp example-conf.json ~/.config/pyjabot.json`
then adjust `~/.config/pyjabot.json` 

## run tests

We use nose and pinoccio for testing.
Run the tests by excuting:

`./run_tests.sh`


### autotesting

If you prefer that tests a run every time you change a file use 
[sniffer](https://pypi.python.org/pypi/sniffer).
After the install you can start it calling `sniffer` in the project root.


If you are using vim and the test are not run on save have a look 
[here](https://github.com/gorakhargosh/watchdog/issues/56?source=c).
