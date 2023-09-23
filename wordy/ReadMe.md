# Wordy

Simple CLI project, used to help with generating valid Bulgarian words  
from a specified sequence of letters and length.
I made this CLI script to help me with solving word puzzles from a popular bulgarian mobile app

#### The App:
> The app has 5 random letters and the goal is to create a valid word.

![app](https://i.imgur.com/6vNWu8F.jpg)

> the problem is often you get stuck on a word and to get a hit, you need to sped money


### Usage:
---- 

Whit no specified length option it will default to one
~~~  powershell
wordy лонк
~~~  
With -l we specify the length of the words we are searching for.
~~~  powershell
wordy лонк -l 4
~~~  
~~~  powershell
wordy лонк -l 3
~~~  

![wordy, demo](https://i.imgur.com/DlVa1Fi.jpg)

### Installation:

I made this as a pip installable package, so when installed globally you can call the CLI script just by "wordy"

To accomplish this you need to first install the requirements.txt.  

First make a virtual environment in the terminal

~~~  powershell
pip install -m venv .venv
~~~  

Then activate it
~~~  powershell
.venv\Scripts\activate
~~~  
Then install the requirements.
~~~  powershell
pip install -r requirements.txt
~~~  

in the functionality.py file you need to set the PATH = r"path to words.txt here" variable as the path to the words.txt that contains all the validated bulgarian words.

To run this as a CLI whiteout changing using the word_helper.py command every time, we want to install this as a package.
~~~  powershell
pip install --editable .
~~~  
To run this whiteout activating a venv or from the folder of the CLI you need to install the package globally.
~~~  powershell
pip install --editable /path to the file location
~~~  
Note. --editable lets you change code in the package
