# import statement

from ultralytics import YOLO
import cv2
from collections import defaultdict
from grid_required_functions import *



def chess_grid_map(model_path, img_path, show_mapped_image=False):
    # image loading


    image = cv2.imread(img_path)

    # image preprocessing
    fx = 0.5  # Scale factor for width
    fy = 0.5  # Scale factor for height
    image = cv2.resize(image, None, fx=fx, fy=fy)

    # loading the YOLO v8 model
    model = YOLO(model_path)
    results = model(image, iou=0.4, conf=0.2)

    # chess board annotation
    # top left is (X1,Y1)
    # bottom right is (X2,Y2)
    X1 = None
    Y1 = None
    X2 = None
    Y2 = None

    pieces_detected_dict = defaultdict(list)
    for result in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        pieces_detected_dict[results[0].names[int(class_id)]].append([(x1, y1), (x2, y2)])
        if (int(class_id) == 0):
            X1 = x1
            Y1 = y1
            X2 = x2
            Y2 = y2
            print(f' chess board top left corner  is {(x1, y1)}')
            print(f' chess board bottom right corner is {(x2, y2)}')



    try:
        X_dif = (X2 - X1) / 8
        Y_dif = (Y2 - Y1) / 8

    except Exception as e:
        print('Deep Learning model not able to detect chess board ')
        print(e)
        exit(0)

    position_storing_dict = {}
    original_Y1 = Y1
    for i in range(8, 0, -1):  # row
        # print(i)
        original_X1 = X1
        for j in range(1, 9):  # column

            initial_point = original_X1
            final_point = original_X1 + X_dif

            text = f'{i},{j}'
            if (show_mapped_image == True):
                cv2.putText(image, text, (int(initial_point + 2), int(original_Y1 + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (100, 2, 200), 1,
                            cv2.LINE_AA)

            # storing the cordinate to dict
            key = text
            position_storing_dict[key] = [(int(initial_point), int(original_Y1)),
                                          (int(final_point), int(original_Y1 + Y_dif))]

            original_X1 = original_X1 + X_dif

        original_Y1 = original_Y1 + Y_dif

    if (show_mapped_image == True):
        for key in position_storing_dict.keys():
            cv2.rectangle(image, (position_storing_dict[key][0]), (position_storing_dict[key][1]), (0, 10, 150), 2)

    position_empty_or_piece = {}

    # used to map pieces with their specific position
    for piece in pieces_detected_dict.keys():  # piece is the name of the piece
        for piece_coord in pieces_detected_dict[piece]:  # piece_coord is a list structure is  [(x1,y1),(x2,y2)]
            # print(f'{piece} position is {piece_coord}')
            for position in position_storing_dict.keys():  # position is a list structure is  [(X1,y1),(x2,y2)]
                position_coord = position_storing_dict[position]
                checker = piece_position_similarity_checker(piece_coordinate=piece_coord,
                                                            position_coordinate=position_coord)
                if checker == True:
                    position_empty_or_piece[position] = piece

    # used to handle the positions where pieces are not present
    for position in position_storing_dict.keys():
        try:
            if (type(position_empty_or_piece[position]) == str):
                pass
        except Exception as e:
            position_empty_or_piece[position] = 'empty'

    print(position_empty_or_piece)


    # drawing the map of the chess_game
    chess_notation(position_empty_or_piece)

    if (show_mapped_image == True):
        cv2.imshow('Image with Bounding Boxes', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = '../tst_image/img7.jpeg'

    model_path = '../models/chess_colab_3/runs/detect/train/weights/best.pt'
    chess_grid_map(model_path=model_path, img_path=img_path, show_mapped_image=True)