# **Number Guesser**
> this is a console number guessing game assignment project.  

***

### **Description:**
![Number Guesser](https://i.imgur.com/WOkz0eR.gif)

This game works fairly simple, it uses the python random module to generate a number from three ranges chosen by the player:
    
* easy difficulty 1 - 10
* medium difficulty 1 - 25
* hard difficulty 1 - 35  

After the range is picked, you have 5 chances to guess the number before you lose.

**** 
### Installation:

To play, first we need to install the colorama module for the colored text.

First create a virtual environment.

```` powershell
py install -m venv .venv
````

Then activate it.

```` powershell
.venv\Scripts\activate
````

After this install the requirements:

```` powershell
pip install -r requirements.txt
````
Or just install the package.

```` powershell
pip install colorama
````
***