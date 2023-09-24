# Wordy

Simple CLI project, used to help with generating valid Bulgarian words  
from a specified sequence of letters and length.
I made this CLI script to help me with solving word puzzles from a popular bulgarian mobile app.

### The App:
---
> The app has some random letters and the goal is to create a valid word.
> The problem is often you get stuck on a word and to get a hint, you need to sped money.  
> The app look like this ⬇️

![app](https://i.imgur.com/6vNWu8F.jpg)



### Usage:
---- 

Whit no specified length option the default length is three letters.
~~~  powershell
wordy лонк
~~~  
With -l we specify the generated words length.
~~~  powershell
wordy лонк -l 4
~~~  
~~~  powershell
wordy ратпи -l 3
~~~  

![wordy, demo](https://i.imgur.com/DlVa1Fi.jpg)

### Installation:
----
I made this as a pip installable package, so when installed globally you can call the CLI script just by "wordy"  
To accomplish this we need to:  

First make a virtual environment in the terminal.

~~~  powershell
py install -m venv .venv
~~~  

Then activate it.

~~~  powershell
.venv\Scripts\activate
~~~  

Then install the requirements.

~~~  powershell
pip install -r requirements.txt
~~~  

in the functionality.py file you need to set the PATH = r"path to words.txt here" variable as the path to the words.txt that contains all the validated bulgarian words.

To run this as a CLI without using the py word_helper.py before running the CLI every time, we want to install this as a package.  
This install it locally in the virtual environment  
~~~  powershell
pip install --editable .
~~~  
To run this without activating a venv or from the folder of the CLI you need to install the package globally.
~~~  powershell
pip install --editable /path to the file location
~~~  
Note "--editable" lets you change code in the package.  


### How it works:
---
The scripts is fairly simple logic wise, it just takes the letter sequence and uses the build in python itertools module, the permutation function generates permutations of the sequence letters, checking them from a list of 250k + validated Bulgarian words, after confirming a permutation is a valid word it returns it. 

----