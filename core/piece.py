class Piece :
    def __init__(self,piece_type, color):
        self.piece_type = piece_type
        self.color = color
    def __repr__(self):
        return f"{self.color} {self.piece_type} "