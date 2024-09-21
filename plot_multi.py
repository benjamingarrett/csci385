import json
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import sys

# NOTE: This module must not be changed, because it needs to be the 
#       same one used by everyone, including the instructor.

def plot_input(fname):
  print(f'Processing {fname}')
  h = open(fname,'r')
  s = h.read()
  h.close()
  j = json.loads(s)
  fig = plt.figure()
  ax = fig.add_subplot(111)
  if 'plot_type' in j:
    if j['plot_type'] == 'multi':
      print('found plot_type == multi')
      for v in j['show']:
        x_label = v[0]
        y_label = v[1]
        x = j[x_label]
        y = j[y_label]
        ax.plot(x, y, label=v[2])
      if 'boxes' in j:
        for v in j['boxes']['series']:
          ax.plot([v[0],v[2],v[2],v[0],v[0]],[v[1],v[1],v[3],v[3],v[1]])
      if 'lines' in j:
        print('found lines')
        for v in j['lines']['series']:
          ax.plot([v[0],v[2]], [v[1],v[3]])
      if 'plot_title' in j:
        t = fname + '\n' + j['plot_title']
        plt.title(t)
      ax.legend(loc='upper right')
      plt.show()
    if j['plot_type'] == 'time_series':
      print('found plot_type == time_series')
      for v in j['show']:
        y = j[v[0]]
        x = [k for k in range(len(y))]
        ax.plot(x, y, label=v[1])
      if 'plot_title' in j:
        t = fname + '\n' + j['plot_title']
        plt.title(t)
      ax.legend(loc='upper right')
      plt.show()


def plot_folder(dir_name):
  allFiles = [f for f in listdir(dir_name) if isfile(join(dir_name, f))]
  for fn in allFiles:
    if len(fn.split('.')) > 1:
      if fn.split('.')[1] == 'json':
        plot_input(fn)
 

if __name__ == '__main__':
  if len(sys.argv) < 2:
    input_dir = '.'         # if no command-line argument is given, by default it scans the current directory
  else:
    input_dir = sys.argv[1] # the first argument is the fold to scan for input files

