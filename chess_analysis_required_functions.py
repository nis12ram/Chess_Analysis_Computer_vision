import  chess
from stockfish import Stockfish

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

def chess_piece_mapping(position_empty_or_piece):
    ranker_starter_dict = {}
    starter_value = -1
    for rank in range(1, 9):
        ranker_starter_dict[rank] = starter_value
        starter_value = starter_value + 8

    # print(ranker_starter_dict)
    index_empty_or_piece = {}
    for key in position_empty_or_piece.keys():
        first_pos, second_pos = key.split(",")
        first_pos, second_pos = int(first_pos), int(second_pos)
        # print(first_pos,second_pos)
        base_value = ranker_starter_dict[first_pos]
        # print(base_value)
        key_idx = base_value + second_pos
        # print(key_idx)
        index_empty_or_piece[key_idx] = position_empty_or_piece[key]
        # break
    # print(index_piece_or_empty)

    color_chess_dict = {'black': chess.BLACK, 'white': chess.WHITE}
    piece_chess_dict = {'rook': chess.ROOK, 'bishop': chess.BISHOP, 'queen': chess.QUEEN, 'king': chess.KING,
                        'knight': chess.KNIGHT, 'pawn': chess.PAWN}
    chess_board_dict = {}
    ### setting the piecee into chess_board_dict
    for idx in index_empty_or_piece.keys():
        value = index_empty_or_piece[idx]
        if value != 'empty':
            color_value, piece_value = value.split("_")
            chess_board_dict[idx] = chess.Piece(piece_chess_dict[piece_value], color_chess_dict[color_value])
    return chess_board_dict

def get_info_from_fen(fen_string,depth,skill_level):

    stockfish = Stockfish(r'C:\Users\Ram\PycharmProjects\detecting_chess\stockfish\stockfish-windows-x86-64-avx2.exe')
    stockfish.set_depth(depth) # looking 20moves ahead
    stockfish.set_skill_level(skill_level)# Highest skill level
    # # print(stockfish.get_parameters())
    stockfish.set_fen_position(fen_string)
    evaluation_info = stockfish.get_evaluation()
    top_moves = stockfish.get_top_moves()
    best_move = stockfish.get_best_move()
    return evaluation_info,top_moves,best_move

def beautify_result(evaluation_info,top_moves,best_move):
    print('------------------------------ Fen Analysis Start -----------------------------')
    print(f"Current Centipawn score -->{evaluation_info['value']}")
    print('-------------------------------------------------------------------------------')

    print(f'Top moves to play ')
    move_number = 1
    for move in top_moves:
        print(f'## Move {move_number} info')

        print(f"Move : {move['Move']}")
        print(f"New Cantipawn Score : {move['Centipawn']}")
        print(f"Checkmate Possible : {move['Mate']}")
        move_number+=1
    print('------------------------------------------------------------------------------')
    print(f'Best Move : {best_move}')
    print('------------------------------ Fen Analysis Over -----------------------------')

def board_instance(chess_board_dict,show_board):
    board = chess.Board()

    board.set_piece_map(chess_board_dict)
    if (show_board == True):
        print(board)

    return board


def get_fen(board,activeColor):
    fen_lst = board.fen().split(" ")
    fen_lst[1] = activeColor
    fen = " ".join(fen_lst)
    return fen
