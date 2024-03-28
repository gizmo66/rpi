set object 1 rectangle from graph 0, first 44000 to graph 1, first 42000
set object 1 fillstyle solid fillcolor "light-blue"
set object 1 behind

set object 2 rectangle from graph 0, first 42000 to graph 1, first 38000
set object 2 fillstyle solid fillcolor "light-green"
set object 2 behind

set datafile separator ","
set grid
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set xtics format "%d-%m\n%H:%M"
set y2tics
set term png
set output "baobab.png"
