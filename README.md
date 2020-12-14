# MasterMorphix 4x4 Corner Flip script

When solving mastermorfix 4x4, one may face squares corner parity. This makes mastermorfix unsolvable.
This script helps to solve this parity by quickly swapping two yellow corners between green and red squares.

![squares](squares.png)

Squares elements are coded using triplets:
- gsy: (g\y - left top to the right bottom diagonal splitted square, green triangle at the left bottom, yellow triangle at the right top corner)
- ytg: (y/g - left bottom to the right top diagonal splitted square, yellow triangle is at the top left corner and green one is in front at the right bootom corner)

When crossing the horizont each element changes the order of colors, when crossing any of the borders it changes diagonal angle.
Solid elements of square are coded as two triangles with the same color. Diagonal direction matters.

    [mirantis@magellan mastermorphix_4x4_corner_flip]$ ./mm4_corner_flip.py r
    [*] Debug mode: False
    [*] Strict mode: True
    [*] Algos to find min: 10
    [*] Reverse function order requested
    [*] Input: rsrrtyrtyosogsyytggtgysy
    [*] Target: ['rsrrtyrtyysygsyotogtggsy']
    ------------------------------------
    [*] Bruteforce started: 2020-12-14 13:18:35.831905
    [*] Recursion level max: 10
    [+] SOLUTION FOUND
    [+] MOVES: F U R U R' R U R' R U R' L U' L' R U R' F R U U U R' F F F
    [+] MOVES SHORTENED: F U R (U') R' (L U' L') (R U R') F R (U') R' (F')
    [+] MOVES LEN: 16
    [*] Bruteforced in: 0:00:03.118456

This script also can help to solve broken square centers. See an example:

    $ ./mm4_corner_flip.py ysrrtyytyrsrgsyytygtggsy rsrrtyrtyysygsyytygtggsy
    [*] Debug mode: False
    [*] Strict mode: True
    [*] Algos to find min: 10
    [*] Cube states are passed as argv
    [*] Input: ysrrtyytyrsrgsyytygtggsy
    [*] Target: ['rsrrtyrtyysygsyytygtggsy']
    ------------------------------------
    [*] Bruteforce started: 2020-12-14 13:26:16.942917
    [*] Recursion level max: 10
    [+] SOLUTION FOUND
    [+] MOVES: R U R' U R U R' F F F U F U U R U R'
    [+] MOVES SHORTENED: (R U R') U (R U R') (U') (R U R')
    [+] MOVES LEN: 11
    [*] Bruteforced in: 0:00:01.379887

