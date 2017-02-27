black = "\033[0;30;49m"
green = "\033[0;32;49m"
yellow = "\033[0;33;49m"
blue = "\033[0;34;49m"
purple = "\033[0;35;49m"
cyan = "\033[0;36;49m"
white = "\033[0;37;49m"
class Red:
	normal = "\033[0;31;49m"
	bold = "\033[1;31;49m"
	faint = "\033[2;31;49m"
	italic = "\033[3;31;49m"
	underline = "\033[4;31;49m"
	blinking = "\033[5;31;49m"
	reverse = "\033[7;31;49m"
	invisible = "\033[8;31;49m"
print ("I'm normal")
print (black + "I'm black!")
print (Red.normal + "I'm red!")
print (green + "I'm green!")
print (yellow + "I'm yellow!")
print (blue + "I'm blue!")
print (purple + "I'm purple!")
print (cyan + "I'm cyan!")
print (white + "I'm white!")
