

def piece_position_similarity_checker(piece_coordinate, position_coordinate):
    x1_dif = abs(piece_coordinate[0][0] - position_coordinate[0][0])
    y1_dif = abs(piece_coordinate[0][1] - position_coordinate[0][1])
    x2_dif = abs(piece_coordinate[1][0] - position_coordinate[1][0])
    y2_dif = abs(piece_coordinate[1][1] - position_coordinate[1][1])

    if (x1_dif <= 30 and x2_dif <= 30 and y1_dif <= 30 and y2_dif <= 30):
        return True

def chess_notation(position_piece_pair_dict):
    file_notation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rank_notation = ['1', '2', '3', '4', '5', '6', '7', '8']
    pieces_notation = {"empty": "___", "white_rook": "W_r", "white_bishop": "W_b", "white_queen": "W_q",
                       "white_king": "W_k", "white_knight": "W_n", "white_pawn": "W_p", "black_rook": "B_r",
                       "black_bishop": "B_b", "black_queen": "B_q", "black_king": "B_k", "black_knight": "B_n",
                       "black_pawn": "B_p"}
    for i in range(8, 0, -1):  # row
        print(i, end="  ")
        for j in range(1, 9):  # column
            key = f'{i},{j}'

            print(pieces_notation[position_piece_pair_dict[key]], end=" ")
        print(" ")
        if (i == 1):
            print("\t", end="")
            for notation in file_notation:
                print(notation, end="\t")
    print(f'\nannotations')
    for symbol in pieces_notation.keys():
        print(f'{symbol} ---->  {pieces_notation[symbol]}')

