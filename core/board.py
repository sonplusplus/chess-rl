class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_pieces = []
        self.black_pieces = []

    def _validate_position(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError(f"Invalid position: ({row}, {col})")

    def set_initial_pos(self):
        back_rank = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        for col in range(8):
            self.set_piece(0, col, Piece(back_rank[col], BLACK))
            self.set_piece(1, col, Piece(PAWN, BLACK))
            self.set_piece(6, col, Piece(PAWN, WHITE))
            self.set_piece(7, col, Piece(back_rank[col], WHITE)) 

    def get_piece(self, row, col):
        self._validate_position(row, col)
        return self.board[row][col]
    
    def set_piece(self, row, col, piece):
        self._validate_position(row, col)
        old_piece = self.board[row][col]
        
        # Xóa quân cũ khỏi cache
        if old_piece is not None:
            if old_piece.color == WHITE:
                self.white_pieces.remove((row, col))
            else:
                self.black_pieces.remove((row, col))
        
        # Thêm quân mới vào cache
        if piece is not None:
            if piece.color == WHITE:
                self.white_pieces.append((row, col))
            else:
                self.black_pieces.append((row, col))
        
        # Cập nhật board
        self.board[row][col] = piece
        return old_piece
    
    def get_all_pieces(self, color):
        pieces = []
        piece_positions = self.white_pieces if color == WHITE else self.black_pieces
        
        for row, col in piece_positions:
            piece = self.board[row][col]
            pieces.append((piece, row, col))
        
        return pieces
    
    def is_empty(self, row, col):
        self._validate_position(row, col)
        return self.board[row][col] is None