#!/usr/bin/env Python3

figure = input("what figure to draw? ")

parallel_line = ( '-' * 5 ) + '\n'
vertical_line = '|' + ( ' ' * 3 ) + '|\n'


if figure == "line":
  print(parallel_line)

elif figure == "square":
  print(parallel_line)
  print(vertical_line * 2)
  print(parallel_line)

elif figure == "parallel horizontal lines":
  print(parallel_line * 2)

elif figure == "parallel vertical lines":
  print(vertical_line * 2)

else:
  print("CAN'T DRAW SUCH FIGURE!")
