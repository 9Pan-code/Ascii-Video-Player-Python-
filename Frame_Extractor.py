import cv2
import os

video_path = "YOUR VIDEO GOES HERE"
output_dir = "PUT FRAME FOLDER HERE"
os.makedirs(output_dir, exist_ok=True)
cap = cv2.VideoCapture(video_path)

frame_id = 0

while True:
  ret, frame = cap.read()
  if not ret:
    break
  path = os.path.join(output_dir, f"frame_{frame_id:06d}.png")
  cv2.imwrite(path, frame)
  frame_id += 1
  cap.release()
print(frame_id)