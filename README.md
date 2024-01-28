---> chess analysis.py  ia sbout analyzing the chess image with input of activeColor and then outputs the best move for the image and activeColor

---> chess_grid.py converts image and display it in form of grid in console 

---> (object detection of chess piecce and chess board  are done through yolov8 with custom data using yolov8m.yaml model )
## model link from drive https://drive.google.com/drive/folders/1vEgy9hCdINOu7-Bii5a568VAE2zhIMhY?usp=sharing


---> the dataset is collected from game name (Chess-Play vs Computer) all images is based on 2D chess board (the dataset is very limited and the model will only able to inetrprate images from these games with 2d structire )

----> use stockfish library and exe file to connect with the chess engine (modify the path of .exe file from both required functions file based on your file path)

## In Image white pieces(rank 1 and rank2 ) should be at bottom side of image and black pieces(rank 7 and rank 8) should be at top side side of Image (ULtra Imp Note: the model logic is based on these condition )



---> Example

input is image and model built using yolo v8

![img7](https://github.com/nis12ram/Chess_Analysis_Computer_vision/assets/145199311/a64ef1d0-f58b-4010-b221-4284ad9b6170)





output of chess_grid,py for specific image









![Screenshot 2024-01-28 115931](https://github.com/nis12ram/Chess_Analysis_Computer_vision/assets/145199311/7fb40bab-146f-41e2-a667-93be1a00ef5b)

![Screenshot 2024-01-28 120652](https://github.com/nis12ram/Chess_Analysis_Computer_vision/assets/145199311/0bc57d53-f799-45d6-b7ad-b490c4a35cdb)






output of chess_analysis.py

## activeColor = "b" for black (param at chess_board_analysis())





![Screenshot 2024-01-28 120932](https://github.com/nis12ram/Chess_Analysis_Computer_vision/assets/145199311/f96edaa4-ec3c-4ebd-91bd-e44303c4bb8d)
