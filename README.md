# ColOurs
ColOurs is an easy-to-use python module which will add the ability to print with colours.
## Installation
To install, just put the provided python file inside the directory which you need the module for. Then, in your python file, type `import colours`. Then, the module will be imported into your python file. Then, to reference the module, use `colours.` as a prefix.
If you don't want to use `colours.` as a prefix, instead of `import colours`, type `from colours import *`, which will import everything without you having to use `colours.` as a prefix.
## Use
Here are a list of colours available:
* Black
* White
* Red
* Green
* Yellow
* Blue
* Purple
* Cyan
* Normal (This is just the normal colour your terminal/console uses.
Here are a list of "effects" you can use:
* Normal (Just plain normal text)
* Bold
* Faint
* Italic
* Underline
* Blinking
* Reverse (This will switch the background colour and the foreground colour)
* Invisible
To use or change a colour, you must reference the colour (eg. Red), add a dot (.), then add the effect (eg. bold). So it would look like this: `Red.bold`. If you were to use it in a print statment, it would be `print(color.effect + text)`. Note: The first letter of each colour is bold, while for each effect, the whole name is lowercase.
