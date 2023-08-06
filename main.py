class Board:
Def _init__(x_len:int:y_len:int, z_len:int=None)
If x_len is not None:
Riase Not Implemented Error
self. _board=[0 for j in range(x_leb)] for i   in. range(y_len)

Abstract Class Piece:
Value (none if oeice is critical)
Maximum_move_length=None
Moves
Attacks
Can jump=False
Can_promote=False
Special_initial_move=False
Has_moved=False
Has_directiobality=False
Def move
Def attack
Move
Remove piece



Class Pawn:
Value=1
Move_length=1
Can_promote=True
Special_initial_move=(
0,1,0
0,0,0
0,0,0
)
Special_initial_move_length=2
Moves=
(0,1,0
0,0,0,
0,0,0)
Attacks=
(1,0,0
0,0,0
0,0,0)


Class Rook:
Value=4
Moves=
(0,1,0
1,0,1
0,1,0)
Attack=
(0,1,0
1,0,1
0,1,0)
Special_initial_move=
0,0,0
1,0,1
0,0,0
Special_initial_move_length=2
Has_directionailoty=True

Class Knight:
Value=3


Class Bishop
Value=3.15


Class Queen:
Value=9

Class King:
Value=None


