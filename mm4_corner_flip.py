#!/usr/bin/python3

__author__ = "Dzmitry Stremkouski"
__copyright__ = "Copyright 2020, Dzmitry Stremkouski."
__license__ = "GNU Public License 2.0"

from sys import exit as _exit
from sys import setrecursionlimit as _rlimit
import copy as _cp
from datetime import datetime as _dt

visited_states = []
max_recursion_level = 16
_wanted = [ 'rsrrtyrtyysygsyotogtggsy' ]
_input = 'rsrrtyrtyosogsyytygtggsy'
# _input = 'rsrrtyrtyosogsyytggtgysy'
max_moves = 250
start_time = _dt.now()
_len_size_limit = 120
all_moves = [ 'r1', 'r2', 'r3', 'l1', 'l2', 'l3', 't1', 't2', 't3', 's1', 's2', 's3']
_algos = []
_algos_min = 2
_debug = False
_word_print = False
_strict = True

# ------
# Colors:
# -------
# y: yellow
# g: green
# b: blue
# r: red
# o: orange
# Elements:
# ---------
# gsy: (g\y - left top to the right bottom diagonal splitted square, green triangle at the left bottom, yellow triangle at the right top corner)
# ytg: (y/g - left bottom to the right top diagonal splitted square, yellow triangle is at the top left corner and green one is in front at the right bootom corner)
# Movements:
# ----------
# R1: R U R'
# R2: R 2U R'
# R3: R 3U R'
# L1: L U' L'
# L2: L 2U' L'
# L3: L 3U' L'
# S1: U
# S2: U U
# S3: U U U
# T1: F
# T2: F F
# T3: F F F

_formulas = {
    "r1": "R U R'",
    "r2": "R U U R'",
    "r3": "R U U U R'",
    "l1": "L U' L'",
    "l2": "L U' U' L'",
    "l3": "L U' U' U' L'",
    "s1": "U",
    "s2": "U U",
    "s3": "U U U",
    "t1": "F",
    "t2": "F F",
    "t3": "F F F"
}

_taints = {
    'r1': [ 'r2', 'r3' ],
    'r2': [ 'r1', 'r3' ],
    'r3': [ 'r1', 'r2' ],
    'l1': [ 'l2', 'l3' ],
    'l2': [ 'l1', 'l3' ],
    'l3': [ 'l1', 'l2' ],
    's1': [ 's2', 's3' ],
    's2': [ 's1', 's3' ],
    's3': [ 's1', 's2' ],
    't1': [ 't2', 't3' ],
    't2': [ 't1', 't3' ],
    't3': [ 't1', 't2' ]
}

def _map():
    i = -1
    fmap = {}
    cmap = {}
    for e in all_moves:
        i += 1
        code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]
        fmap[code] = e
        cmap[e] = code
    return fmap, cmap

def _chd(l):
    if l == 't':
        return 's'
    elif l == 's':
        return 't'
    return l

def r1(s):
    return ''.join([
        s[8],  _chd(s[7]),  s[6],
        s[3],  s[4],        s[5],
        s[21], _chd(s[22]), s[23],
        s[9],  s[10],       s[11],
        s[12], s[13],       s[14],
        s[0],  _chd(s[1]),  s[2],
        s[18], s[19],       s[20],
        s[17], _chd(s[16]), s[15]
    ])

def r2(s):
    return r1(r1(s))

def r3(s):
    return r1(r1(r1(s)))

def l1(s):
    return ''.join([
        s[0],  s[1],        s[2],
        s[11], _chd(s[10]), s[9],
        s[6],  s[7],        s[8],
        s[18], _chd(s[19]), s[20],
        s[3],  _chd(s[4]),  s[5],
        s[15], s[16],       s[17],
        s[14], _chd(s[13]), s[12],
        s[21], s[22],       s[23]
    ])

def l2(s):
    return l1(l1(s))

def l3(s):
    return l1(l1(l1(s)))

def s1(s):
    return ''.join([
        s[8],  _chd(s[7]),  s[6],
        s[0],  _chd(s[1]),  s[2],
        s[9],  _chd(s[10]), s[11],
        s[5],  _chd(s[4]),  s[3],
        s[12], s[13],       s[14],
        s[15], s[16],       s[17],
        s[18], s[19],       s[20],
        s[21], s[22],       s[23]
    ])

def s2(s):
    return s1(s1(s))

def s3(s):
    return s1(s1(s1(s)))

def t1(s):
    return ''.join([
        s[0],  s[1],        s[2],
        s[3],  s[4],        s[5],
        s[6],  s[7],        s[8],
        s[9],  s[10],       s[11],
        s[20], _chd(s[19]), s[18],
        s[12], _chd(s[13]), s[14],
        s[21], _chd(s[22]), s[23],
        s[17],_chd(s[16]), s[15]
    ])

def t2(s):
    return t1(t1(s))

def t3(s):
    return t1(t1(t1(s)))

def _check_comb(comb):
    global _combinations
    global _input
    if comb == _input:
        if _debug:
            print("Cycle found: %s" % comb)
        return False
    else:
        if comb not in _combinations:
            _combinations.append(comb)
        return True

def _xprint(s):
    global _debug
    global _word_print
    if _word_print:
        if len(s) > 3 and s[0:4] == 'Word':
            print(s)
    elif _debug:
        print(s)

def _brute(cube, level, moves):

    global max_recursion_level
    global _taints
    global _static_map
    global _static_rmap
    global _algos

    if level > max_recursion_level:
        return cube

    if len(moves) > max_moves:
        return cube

    if cube in _wanted:
        print("[+] SOLUTION FOUND")
        _m = ''
        for m in str(moves):
            _m = '%s %s' % (_m, _formulas[_static_map[m]])
        _m = _m.strip()
        print("[+] MOVES: %s" % _m)
        for d in ['R', 'L', 'U', 'F']:
            _m = _m.replace('%s %s %s' % (d, d, d), "(%s')" % d)
            _m = _m.replace("%s' %s' %s'" % (d, d, d), "(%s)" % d)
        for d in ['R', 'L', 'U', 'F', "R'", "L'", "U'", "F'"]:
            _m = _m.replace('%s %s' % (d, d), "2%s" % d)
        _m = _m.replace("R U R'", "(R U R')")
        _m = _m.replace("L U' L'", "(L U' L')")
        print("[+] MOVES SHORTENED: %s" % _m)
        print("[+] MOVES LEN: %s" % str(len(moves)))
        global start_time
        time_elapsed = _dt.now() - start_time
        print('[*] Bruteforced in: {}'.format(time_elapsed))
        if len(_algos) == _algos_min:
            print('[d] Algos minimum reached: %s' % str(_algos_min))
            _exit(0)

    global visited_states
    if cube in visited_states:
        return cube

    new_cube = _cp.deepcopy(cube)

    if _debug:
        print("[*] Reached level: %s, len_moves: %s, len_visited: %s" % (str(level), str(len(moves)), str(len(visited_states))))
        print("[d] moves: %s" % (str(moves)))
    visited_states.append(new_cube)

    for func in _static_rmap:
        if _strict and func in _taints:
            if len(moves) > 0 and _static_map[moves[-1]] in _taints[func]:
                continue

        changed_cube = eval("%s(new_cube)" % func)
        _brute(changed_cube, level+1, "%s%s" % (moves, _static_rmap[func]))

    return new_cube

_static_map,_static_rmap = _map()
print("[*] Debug mode: %s" % _debug)
print("[*] Strict mode: %s" % _strict)
print("[*] Algos to find min: %s" % str(_algos_min))
print("[*] Input: %s" % _input)
print("[*] Target: %s" % _wanted)
print("------------------------------------")
print('[*] Bruteforce started: {}'.format(start_time))
print("[*] Recursion level max: %s" % str(max_recursion_level))
_rlimit(max_recursion_level+len(_static_map))
_brute(_cp.copy(_input), 0, "")
