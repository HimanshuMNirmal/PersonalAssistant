import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open webcam
cap = cv2.VideoCapture(0)

# Initialize variables for previous hand position
prev_x, prev_y = None, None

# Initialize variables for filtered hand position
filtered_x, filtered_y = None, None

# Filter parameters
alpha = 0.5  # Smoothing factor (0 < alpha < 1)


while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)
    print(results.handness)
# # Loop to capture frames from the webcam
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to RGB (MediaPipe requires RGB input)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process the frame with MediaPipe hands model
#     results = hands.process(rgb_frame)

#     # Check if hands are detected
#     if results.multi_hand_landmarks:
#         # Get hand landmarks
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Get hand centroid
#             cx, cy = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]), int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

#             if prev_x is not None and prev_y is not None:
#                 # Calculate displacement of hand
#                 dx, dy = cx - prev_x, cy - prev_y

#                 # Smooth the movement using a low-pass filter
#                 if filtered_x is not None and filtered_y is not None:
#                     filtered_x = alpha * cx + (1 - alpha) * filtered_x
#                     filtered_y = alpha * cy + (1 - alpha) * filtered_y
#                 else:
#                     filtered_x, filtered_y = cx, cy

#                 # Move mouse by filtered displacement
#                 pyautogui.move(filtered_x - prev_x, filtered_y - prev_y)

#             # Update previous hand position
#             prev_x, prev_y = cx, cy

#     # Display the frame
#     cv2.imshow('Frame', frame)

#     # Check for 'q' key press to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture, destroy windows, and close MediaPipe hands
# cap.release()
# cv2.destroyAllWindows()
# hands.close()
