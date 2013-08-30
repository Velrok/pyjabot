# pyjabot

## install
```
git clone git@github.com:Velrok/pyjabot.git
pip install -e pyjabot
```
*Note: "pip install -e" expects folder containing **setup.py** e.g. github/pyjabot*

## configure 

`cp example-conf.json ~/.config/pyjabot.json`
then adjust `~/.config/pyjabot.json` 

## run tests

We use nose and pinoccio for testing.
Run the tests by excuting:

`./run_tests.sh`


### autotesting

If you prefer that tests a run every time you change a file use 
[pyautotest](https://github.com/ascarter/pyautotest).
After the install you can start it calling `autotest` in the project root.

Also when you are using mac and want to get notifications you should install 
[terminal-notifier](https://github.com/alloy/terminal-notifier).

If you are using vim and the test are not run on save have a look 
[here](https://github.com/gorakhargosh/watchdog/issues/56?source=c).
