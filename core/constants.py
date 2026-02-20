WHITE = 0
BLACK = 1
SQUARE_SIZE = 80  # pixel
LIGHT_SQUARE = (240, 217, 181)  # light beige
DARK_SQUARE = (181, 136, 99)    # brown
PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(6)
BOARD_SIZE = 8
DIRECTIONS = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'NE': (-1, 1),
    'NW': (-1, -1),
    'SE': (1, 1),
    'SW': (1, -1),
}
KNIGHT_MOVES = {
    (-2, -1), (-2, 1),
    (2, 1), (2, -1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
}
def pos_to_algebraic(row, col):
    """
    (row, col) -> algebaric notation
    (0,0) -> a8
    (7,7) -> h1
    """
    alpha = chr(ord('a') + col)
    numeric = str(BOARD_SIZE - row)
    return alpha + numeric
def algebraic_to_pos(algebraic):
    """algebraic notation -> (row, col)
    a8 -> (0,0)
    h1 -> (7,7)
    """
    col = ord(algebraic[0]) - ord('a') 
    row = BOARD_SIZE - int(algebraic[1])
    return row, col