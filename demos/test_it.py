from cli_utils import print_separator 
print_separator()

# from cli_utils import double_line_break
# double_line_break()  # divider between functions

from cli_utils import print_char_separator
char = input("Enter a character for the separator: ")
print_char_separator(char)

from cli_utils import print_custom_separator
char = input("Enter a character for the custom separator: ")
length = int(input("Enter the length for the custom separator: "))
print_custom_separator(char, length)  

from cli_utils import print_labeled_separator
label = input("Enter a label for the separator: ")  
char = input("Enter a character for the labeled separator (default '*'): ")
width = int(input("Enter the width for the labeled separator (default 30): ") or 30)
print_labeled_separator(label, char, width)     

from cli_utils import print_box
message = input("Enter a message to display in the box: ")
char = input("Enter a character for the box border (default '*'): ")
print_box(message, char)

from cli_utils import Colors, color_text
text = input("Enter text to color: ")
color_choice = input("Choose a color (red, green, yellow, blue): ").lower()
color_map = {           
    "red": Colors.RED,
    "green": Colors.GREEN,
    "yellow": Colors.YELLOW,
    "blue": Colors.BLUE
}
colored_text = color_text(text, color_map.get(color_choice, Colors.RESET))
print(colored_text) 


from cli_utils import show_cat_art, show_banner, Colors
# Show colored cat ASCII art
show_cat_art(Colors.BLUE)  # You can change to RED, GREEN, BLUE, etc.
show_banner(Colors.GREEN)
