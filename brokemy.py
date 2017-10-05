#!/bin/python2.7

import time,random,curses;stdscr=curses.initscr();curses.noecho()
curses.start_color();curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
curses.init_pair(4,curses.COLOR_BLUE,curses.COLOR_BLACK)
stdscr.addstr(stdscr.getmaxyx()[0]/2-1,(stdscr.getmaxyx(
)[1]/2-12),"will you break my heart ?")
for i in range(1000):
	stdscr.addstr(int(random.randint(0,stdscr.getmaxyx()[0]-1)
),int(random.randint(0,stdscr.getmaxyx()[1]-1)),random.choice('\
       ...+$+.$...+$                 ...+$+.$...+\
     !$+-.+-x!$+-.+-x!$+-          !$+-.+-x!$+-.+-x!\
   ;,+"-+x-;,+"-+x-;,+"-+x-     ;,+"-+x-;,+"-+x-;,+"-+\
 .+-x_^;..+-x_^;..+-x_^;..+-   .+-x_^;..+-x_^;..+-x_^;..\
"-+--+x=-+-"-+x=-+-"-+x=-+-"-+x=-+-"-+x=-+-"+x=-+-"+-x=-+\
:-.+.+=x-.+:.+=x-.+:.+=x-.+:.+=x-.+:.+=x-.+:+=x.-.+:+=x.-.\
 +x^;=x*+x^ ;=x*+x^ ;=x*+x^ ;=x*+x^ ;=x*+x^ =x*;+x^ =x*;+x\
"  *+--+  *"+--+  *"+--+  *"+--+  *"+--+  *"--+  *"-+-+  *\
*[??^|-x[??*^|-x[??*^|-x[??*^|-x[??*^|-x[??*|-x^[??*|-x^[?\
_/x^;.../x^_;.../x^_;.../x^_;.../x^_;.../x^_...;/x^_...;/x\
 `"-+_x-`"-+_x-`"--+_-`"--+_x-`"-+_-x-"-+`_--"-+`_--x"-+`\
  ._.x.^;=._.x.^;=._x.^.;=_x..^.=_x;...=_^x;...=_^x;...=\
   %-^|&^+.%-^|&^+.%^|&-^+%^|.&-^%^|+&-^.%^|+&-^.%^|+&-\
     )*?^|-x+)*?^|-x)*?+^|x)*-?+^x)*|?+^-x)*|?+^-x)*|?\
      _.x^;+|._.x^;+._.|x^+._;.|x^._;.|+x^._;.|+x^._\
        -[-+x-|^-[-+x|^-[-+x-|^-[-+-|^x-[-+-|^x-[-\
           +;-x=+.++;-x=+.++;-x=+.++;-x=+.++;-x=\
              -.?x**-?-.?x**-?.?x**--?.?x**-\
                 .-^"-+_@.-^"-+@.-^_"-+@.\
                    !--+$x-|!--+$x-|!-\
                       -?=*?^|--?=*\
                           +-x=+\
                             -\
'),curses.color_pair(random.choice([1,2,3,4])))
	stdscr.refresh();time.sleep(0.02)	
stdscr.getch();curses.echo();curses.endwin()
