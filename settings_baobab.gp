set datafile separator ","
set grid
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set xtics format "%d-%m\n%H:%M"
set y2tics
set term png
set output "baobab.png"
