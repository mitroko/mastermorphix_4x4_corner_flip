# MasterMorphix 4x4 Corner Flip script

When solving mastermorfix 4x4, one may face squares corner parity. This makes mastermorfix unsolvable.
This script helps to solve this parity by quickly swapping two yellow corners between green and red squares.

![squares](squares.png)

Formulas to remember:
- swap yellow corners: R' 2F U' R 2F U R F L'
- fix center starting with yellow square: R U R U' R
- fix center starting with red square: F L (2F U') R L (2F U') L

Squares elements are coded using triplets:
- gsy: (g\y - left top to the right bottom diagonal splitted square, green triangle at the left bottom, yellow triangle at the right top corner)
- ytg: (y/g - left bottom to the right top diagonal splitted square, yellow triangle is at the top left corner and green one is in front at the right bootom corner)

When crossing the horizont each element changes the order of colors, when crossing any of the borders it changes diagonal angle.
Solid elements of square are coded as two triangles with the same color. Diagonal direction matters.

    $ ./mm4_corner_flip.py
    [*] Debug mode: False
    [*] Strict mode: True
    [*] Algos to find min: 10
    [*] Input: rsrrtyrtyysygsyotogtggsy
    [*] Target: ['rsrrtyrtyosogsyytygtggsy']
    ------------------------------------
    [*] Bruteforce started: 2020-12-14 16:15:13.096533
    [*] Recursion level max: 14
    [+] SOLUTION FOUND
    [+] MOVES: R U R' R U R' R U R' F F U U U R U R' F F U R U R' F L U' U' U' L' F F
    [+] MOVES SHORTENED: R (U') R' 2F (U') (R U R') 2F U (R U R') F L (U) L' 2F
    [+] MOVES LEN: 18
    [*] Bruteforced in: 0:00:06.589056
    [+] SOLUTION FOUND
    [+] MOVES: R U R' R U R' R U R' F F U U U R U R' F F U R U R' F L U' U' U' L' F F U U U U
    [+] MOVES SHORTENED: R (U') R' 2F (U') (R U R') 2F U (R U R') F L (U) L' 2F 
    [+] MOVES LEN: 18
    [*] Bruteforced in: 0:00:06.616163
    [+] SOLUTION FOUND
    [+] MOVES: R U R' R U R' R U R' F F U U U R U R' F F U R U R' F L U' U' U' L' F F F F F F
    [+] MOVES SHORTENED: R (U') R' 2F (U') (R U R') 2F U (R U R') F L (U) L' 2F
    [+] MOVES LEN: 18
    [*] Bruteforced in: 0:00:06.636386

This script also can help to solve broken square centers. See an example:

![squares-yr](squares-yr.png)

    $ ./mm4_corner_flip.py ysrrtyytyrsrgsyytygtggsy rsrrtyrtyysygsyytygtggsy 10
    [*] Debug mode: False
    [*] Strict mode: True
    [*] Algos to find min: 10
    [*] Cube states are passed as argv
    [*] Recursion level is passed as argv
    [*] Input: ysrrtyytyrsrgsyytygtggsy
    [*] Target: ['rsrrtyrtyysygsyytygtggsy']
    ------------------------------------
    [*] Bruteforce started: 2020-12-14 16:19:12.105908
    [*] Recursion level max: 10
    [+] SOLUTION FOUND
    [+] MOVES: R U R' U R U R' F F F U F U U R U R'
    [+] MOVES SHORTENED: (R U R') U (R U R') (U') (R U R')
    [+] MOVES LEN: 11
    [*] Bruteforced in: 0:00:01.415665

![squares-ry](squares-ry.png)

    $ ./mm4_corner_flip.py ysrrtyrtrysygsyytygtggsy rsrrtyrtyysygsyytygtggsy 10
    [*] Debug mode: False
    [*] Strict mode: True
    [*] Algos to find min: 10
    [*] Cube states are passed as argv
    [*] Recursion level is passed as argv
    [*] Input: ysrrtyrtrysygsyytygtggsy
    [*] Target: ['rsrrtyrtyysygsyytygtggsy']
    ------------------------------------
    [*] Bruteforce started: 2020-12-14 16:29:38.567584
    [*] Recursion level max: 10
    [+] SOLUTION FOUND
    [+] MOVES: F L U' L' F F U R U R' F R U R' U U R U R' U U U
    [+] MOVES SHORTENED: F (L U' L') 2F U (R U R') F (R U R') 2U (R U R') (U')
    [+] MOVES LEN: 18
    [*] Bruteforced in: 0:00:02.930354
    [+] SOLUTION FOUND
    [+] MOVES: F L U' L' F F U U U R U R' L U' L' F F U U U L U' L'
    [+] MOVES SHORTENED: F (L U' L') 2F (U') (R U R') (L U' L') 2F (U') (L U' L')
    [+] MOVES LEN: 17
    [*] Bruteforced in: 0:00:03.083638

