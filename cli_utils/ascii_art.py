from .colors import Colors
def show_banner(color=Colors.YELLOW):
    """Print ASCII banner in color (default yellow)"""
    banner = r"""
   _____ _      _____
  / ____| |    |_   _|
 | |    | |      | |
 | |    | |      | |
 | |____| |____ _| |_
  \_____|______|_____|

     CLI TOOL
"""
    print(f"{color}{banner}{Colors.RESET}")



from .colors import Colors  # import your color codes
def show_cat_art(color=Colors.YELLOW):
    """Prints colored ASCII art of a cat (default yellow)"""
    art = r"""
            ,,
         ,,       ,\\//,
       ,\\//,    ,\\\///,   ,,
      ,\\\///,   \\\\//// ,\\//,
      \\\\////    \\\/// ,\\\///,
       \\\///     ###### \\\\////
       ######    ////\\\\ \\\///
      ////\\\\  /////\\\\\######
     /////\\\\\//////\\\\////\\\\
    //////\\\\\\/,///\\\/////\\\\\
   //////_?_\\\\(_)    //////\\\\\\,
      .'`---`'.    _j_///////\\\\\(_)
     /.'a   a  \.'`---`'.
     |:   ^    /.'d\ /b  \
     \'  www   |:   ^    |
      '._____.'\'  VVV   /
  jgs           '._____.'
"""
    print(f"{color}{art}{Colors.RESET}") 
    
    #color parameter defaults to Colors.YELLOW, Colors.RESET at the end ensures terminal color returns to normal
