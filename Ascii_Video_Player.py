import cv2
import os
import time

frame_dir = "PUT YOUR PATH TO WHERE THE FRAMES GOT EXTRACTED!"

ascii_char = "@%#*+=-:."

frames = sorted(os.listdir(frame_dir))

width = 120
height = 40

for file in frames:
  frame_path = os.path.join(frame_dir, file)
  frame = cv2.imread(frame_path)
  frame = cv2.resize(frame, (width, height))
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ascii_frame = ""
  for row in gray:
    ascii_frame += "".join(ascii_chars[min(int(pixel) *len(ascii_chars) // 256, len(ascii_chars) -1 )] for pixel in row) + "\n"
  os.system("cls" if os.name == "nt" else "clear")
  print(ascii_frame)
  
  time.sleep(1/30) # you can control FPS here