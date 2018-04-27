import sys 

class colour_print:
    colours_dict = {
        "normal": 39,
        "black": 30,
        "white": 37,
        "red": 31,
        "green": 32,
        "blue": 34,
        "yellow": 33,
        "cyan": 36,
        "purple": 35
    }

    styles_dict = {
        "normal": 0,
        "bold": 1,
        "faint": 2,
        "italic": 3,
        "underline": 4,
        "blinking": 5,
        "reverse": 7,
        "invisible": 8
    }

class Meta(type):
    def __getattr__(cls, attr):
        try:
            print_colour = colour_print.colours_dict.get(cls.__name__.lower())
            print_style = colour_print.styles_dict.get(attr.lower())
            return "\033[{0};{1};49m".format(print_style, print_colour)

        except (AttributeError, KeyError):
            return None

class Normal(metaclass=Meta):
    pass

class Black(metaclass=Meta):
    pass

class Red(metaclass=Meta):
    pass

class Green(metaclass=Meta):
    pass

class Yellow(metaclass=Meta):
    pass

class Blue(metaclass=Meta):
    pass

class Purple(metaclass=Meta):
    pass

class Cyan(metaclass=Meta):
    pass

class White(metaclass=Meta):
    pass

print (Normal.normal)
print (Black.normal + "I'm black!")
print (Red.normal + "I'm red!")
print (Green.normal + "I'm green!")
print (Yellow.normal + "I'm yellow!")
print (Blue.normal + "I'm blue!")
print (Purple.normal + "I'm purple!")
print (Cyan.normal + "I'm cyan!")
print (White.normal + "I'm white!")