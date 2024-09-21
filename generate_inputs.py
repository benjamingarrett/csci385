import json
from math import sin, tan
import numpy as np
import sys


def recurrence_2a(t1, t2, t3, t4, max_n):
  r = [[1, t1], [2, t2], [3, t3], [4, t4]]
  i = 5
  while i<=max_n:
    tn = t4 + t1 + 2
    r.append([i, tn])
    t1 = t2
    t2 = t3
    t3 = t4
    t4 = tn
    i += 1
  return r


def recurrence_2b(t1, t2, t3, max_n):
  r = [[1, t1], [2, t2], [3, t3]]
  i = 4
  while i<=max_n:
    tn = (1.0/3)*t3 + 2*t2 - 7*t1
    r.append([i, tn])
    t1 = t2
    t2 = t3
    t3 = tn
    i += 1
  return r


def generate_input_files():
  functions = ['x**3 - 13*x + 18', 'x**2 * sin(1.0/x)', 'tan(x)']
  start = -10.0
  end = 10.0
  step = 0.1
  x = list(np.arange(start, end, step))
  zeros = [0 for k in x]
  f = lambda x: eval(functions[0])
  d = dict()
  d['plot_type'] = 'multi'
  d['problem_type'] = 'root_find'
  d['x'] = x
  d['zeros'] = zeros
  d['f(x)'] = [f(k) for k in x]
  d['show'] = [['x', 'f(x)', functions[0]], ['x', 'zeros', 'x-axis'], ['zeros', 'f(x)', 'y-axis']]
  d['input'] = {
    'function_body': functions[0], 
    'epsilon': 0.0001, 
    'max_iterations': 10, 
    'x0': -1.8, 'x1': 0.5}
  s = json.dumps(d)
  h = open('root_find_1a.json', 'w')
  h.write(s)
  h.close()
  f = lambda x: eval(functions[1])
  d['f(x)'] = [f(k) for k in x]
  d['show'] = [['x', 'f(x)', functions[1]], ['x', 'zeros', 'x-axis'], ['zeros', 'f(x)', 'y-axis']]
  d['input']['function_body'] = functions[1]
  s = json.dumps(d)
  h = open('root_find_1b.json', 'w')
  h.write(s)
  h.close()
  f = lambda x: eval(functions[2])
  d['f(x)'] = [f(k) for k in x]
  d['show'] = [['x', 'f(x)', functions[2]], ['x', 'zeros', 'x-axis'], ['zeros', 'f(x)', 'y-axis']]
  d['input']['function_body'] = functions[2]
  s = json.dumps(d)
  h = open('root_find_1c.json', 'w')
  h.write(s)
  h.close()
  v_2a = recurrence_2a(1, 3, 5, 8, 20)
  zeros = [0 for k in v_2a]
  d['problem_type'] = 'recurrence'
  d['x'] = [k[0] for k in v_2a]
  d['f(x)'] = [k[1] for k in v_2a]
  d['zeros'] = zeros
  d['show'] = [['x', 'f(x)', 't_n = t_n-1 + t_n-4 + 2'], ['x', 'zeros', 'x-axis'], ['zeros', 'f(x)', 'y-axis']]
  s = json.dumps(d)
  h = open('recurrence_2a.json', 'w')
  h.write(s)
  h.close()
  v_2b = recurrence_2b(1, 2, 3, 20)
  zeros = [0 for k in v_2b]
  d['x'] = [k[0] for k in v_2b]
  d['f(x)'] = [k[1] for k in v_2b]
  d['zeros'] = zeros
  d['show'] = [['x', 'f(x)', 't_n = (1/3)t_n-1 + 2t_n-2 - 7t_n-3'], ['x', 'zeros', 'x-axis'], ['zeros', 'f(x)', 'y-axis']]
  s = json.dumps(d)
  h = open('recurrence_2b.json', 'w')
  h.write(s)
  h.close()

