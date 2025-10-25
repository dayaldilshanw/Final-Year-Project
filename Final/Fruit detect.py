import cv2
from yolov5.detect import run
import os
import shutil
import urllib.request
import numpy as np

# IP camera URL
camera_url = "http://192.168.1.4:8080/video"  #  camera's URL
# YOLOv5 model and image paths
weights_path = "Weight/Foodwaste.pt"
current_dir = os.getcwd()
exp_dir = os.path.join(current_dir, "runs", "detect", "exp")


def capture_frames(camera_url):
    while True:
        try:


            #cap = cv2.VideoCapture(camera_url)
            cap = cv2.VideoCapture(2)
            if not cap.isOpened():
                raise Exception("Failed to open camera stream.")

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to retrieve frame from the IP camera.")
                    break



                cv2.imwrite("current_frame.jpeg", frame)


                results = run(source="current_frame.jpeg", weights=weights_path, save_crop=True, max_det=1, conf_thres=0.5)

                if os.path.isdir(exp_dir):
                    crops_dir = os.path.join(exp_dir, "crops")
                    if os.path.isdir(crops_dir):
                        print("Food Detected")
                        for root, dirs, files in os.walk(crops_dir):
                            for crop_file in files:
                                crop_path = os.path.join(root, crop_file)
                                relative_path = os.path.relpath(crop_path, crops_dir)
                                # Extract the first directory (animal name) from the relative path
                                Food_name, _ = os.path.split(relative_path)
                                print("Food Name:", Food_name)
                    else:
                        print("Food not detected")
                else:
                    print("Exp folder not detected.")

                os.remove("current_frame.jpeg")


                if os.path.isdir(exp_dir):
                    shutil.rmtree(exp_dir)

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    capture_frames(camera_url)
