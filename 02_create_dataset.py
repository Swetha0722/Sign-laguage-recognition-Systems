import os
# import pickle
import joblib as jb
import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = "./data"

data = []
labels = []
DATA_DIR = "./data"
data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)

    # Check if the path is a directory
    if os.path.isdir(dir_path):
        for img_path in os.listdir(dir_path):
            data_aux = []
            x_ = []
            y_ = []

            img = cv2.imread(os.path.join(dir_path, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                data.append(data_aux)
                labels.append(dir_)

f = open("model.p", "wb")
jb.dump({"data": data, "labels": labels}, f)
f.close()


# import os
# import joblib as jb
# import mediapipe as mp
# import cv2
#
# mp_hands = mp.solutions.hands
#
# # Initialize MediaPipe hands module
# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
#
# # Directory containing image data
# DATA_DIR = "./data"
#
# data = []
# labels = []
#
# # Process each directory in the data directory
# for dir_ in os.listdir(DATA_DIR):
#     dir_path = os.path.join(DATA_DIR, dir_)
#
#     # Check if the path is a directory
#     if os.path.isdir(dir_path):
#         # Process each image in the directory
#         for img_path in os.listdir(dir_path):
#             try:
#                 data_aux = []
#                 x_ = []
#                 y_ = []
#
#                 # Read image
#                 img = cv2.imread(os.path.join(dir_path, img_path))
#
#                 # Convert image to RGB
#                 img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#                 # Process image to extract hand landmarks
#                 results = hands.process(img_rgb)
#
#                 # If hand landmarks are detected
#                 if results.multi_hand_landmarks:
#                     for hand_landmarks in results.multi_hand_landmarks:
#                         # Extract x, y coordinates of hand landmarks
#                         for landmark in hand_landmarks.landmark:
#                             x = landmark.x
#                             y = landmark.y
#
#                             x_.append(x)
#                             y_.append(y)
#
#                     # Normalize landmark coordinates
#                     min_x = min(x_)
#                     min_y = min(y_)
#                     for i in range(len(x_)):
#                         data_aux.append(x_[i] - min_x)
#                         data_aux.append(y_[i] - min_y)
#
#                     # Append normalized data and corresponding label to lists
#                     data.append(data_aux)
#                     labels.append(dir_)
#
#             except Exception as e:
#                 print(f"Error processing image {img_path}: {e}")
#
# # Save data and labels to a joblib file
# try:
#     with open("model.joblib", "wb") as f:
#         jb.dump({"data": data, "labels": labels}, f)
#     print("Data saved successfully to 'model.joblib'")
# except Exception as e:
#     print(f"Error saving data: {e}")
# finally:
#     # Release resources used by MediaPipe hands module
#     hands.close()


# import os
# import joblib as jb
# import mediapipe as mp
# import cv2
#
# mp_hands = mp.solutions.hands
#
# # Initialize MediaPipe hands module
# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
#
# # Directory containing image data
# DATA_DIR = "./data"
#
# data = []
# labels = []
#
# # Process each directory in the data directory
# for dir_ in os.listdir(DATA_DIR):
#     dir_path = os.path.join(DATA_DIR, dir_)
#
#     # Check if the path is a directory
#     if os.path.isdir(dir_path):
#         # Process each image in the directory
#         for img_path in os.listdir(dir_path):
#             try:
#                 data_aux = []
#                 x_ = []
#                 y_ = []
#
#                 # Read image
#                 img = cv2.imread(os.path.join(dir_path, img_path))
#
#                 # Convert image to RGB
#                 img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#                 # Process image to extract hand landmarks
#                 results = hands.process(img_rgb)
#
#                 # If hand landmarks are detected
#                 if results.multi_hand_landmarks:
#                     for hand_landmarks in results.multi_hand_landmarks:
#                         # Extract x, y coordinates of hand landmarks
#                         for landmark in hand_landmarks.landmark:
#                             x = landmark.x
#                             y = landmark.y
#
#                             x_.append(x)
#                             y_.append(y)
#
#                     # Normalize landmark coordinates
#                     min_x = min(x_)
#                     min_y = min(y_)
#                     for i in range(len(x_)):
#                         data_aux.append(x_[i] - min_x)
#                         data_aux.append(y_[i] - min_y)
#
#                     # Append normalized data and corresponding label to lists
#                     data.append(data_aux)
#                     labels.append(dir_)
#
#             except Exception as e:
#                 print(f"Error processing image {img_path}: {e}")
#
# # Save data and labels to a joblib file
# try:
#     with open("model.joblib", "wb") as f:
#         jb.dump({"data": data, "labels": labels}, f)
#     print("Data saved successfully to 'model.joblib'")
# except Exception as e:
#     print(f"Error saving data: {e}")
# finally:
#     # Release resources used by MediaPipe hands module
#     hands.close()
