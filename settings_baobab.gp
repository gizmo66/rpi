set object 1 rectangle from graph 0, first 48000 to graph 1, first 41500
set object 1 fillstyle solid fillcolor "light-cyan"
set object 1 behind

set object 2 rectangle from graph 0, first 41500 to graph 1, first 39000
set object 2 fillstyle solid fillcolor "seagreen"
set object 2 behind

set object 3 rectangle from graph 0, first 39000 to graph 1, first 36500
set object 3 fillstyle solid fillcolor "lemonchiffon"
set object 3 behind

set object 4 rectangle from graph 0, first 36500 to graph 1, first 30000
set object 4 fillstyle solid fillcolor "pink"
set object 4 behind

set datafile separator ","
set grid
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set xtics format "%d-%m\n%H:%M"
set y2tics
set term png
set output "baobab.png"
