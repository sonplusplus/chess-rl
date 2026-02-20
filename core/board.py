class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    def set_initial_pos(self):
        pass
    def get_piece(self, row, col):
        return self.board[row][col]
    def set_piece(self, row, col, piece):
        self.board[row][col] = piece
    def remove_piece(self, row, col):
        self.board[row][col] = None
    def get_all_pieces(self, color):
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    pieces.append((piece, row, col))
        return pieces
    def is_empty(self, row, col):
        return self.board[row][col] is None
    