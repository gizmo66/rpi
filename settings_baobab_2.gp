set object 1 rectangle from graph 0, first 68 to graph 1, first 64
set object 1 fillstyle solid fillcolor "light-green"
set object 1 behind

set datafile separator ","
set grid
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set xtics format "%d-%m\n%H:%M"
set y2tics
set term png
set output "baobab_2.png"
