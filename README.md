# DropToken
This program is written in Python and tested with Python2.7. Please make sure you have Python2.7 installed on your machine before executing the program. Please follow this [installation guide](https://wiki.python.org/moin/BeginnersGuide/Download) if you do not have Python2.7 installed yet.

## How to play the game:
 ```
 python DropToken.py
 ```
 or `C:\Python27\python.exe DropToken.py` on Windows if you installed Python2.7 in the default directory

## How to test ```DropToken.py```
The testing part consists of 2 test modules. `DropTokenDocTests.py` tests `inputProcess()` function in `DropToken.py` because the output of `inputProcess()` is printed to command line and it is easier to use doctest to test it. `DropTokenUnitTests.py` tests `DropToken.py` except for `inputProcess()`.
```
python DropTokenUnitTests.py
python DropTokenDocTests.py
```
or
```
C:\Python27\python.exe DropTokenUnitTests.py
C:\Python27\python.exe DropTokenDocTests.py
```
on Windows
