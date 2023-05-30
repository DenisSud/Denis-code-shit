import cv2
import mediapipe as mp

# Initialize the MediaPipe hand landmark detector.
mp_hands = mp.solutions.hands.Hands()

# Start a video capture loop.
cap = cv2.VideoCapture(0)

while True:
    # Capture the current frame.
    ret, frame = cap.read()

    # Convert the frame to RGB.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the hand landmarks.
    results = mp_hands.process(rgb_frame)

    # If hands are detected:
    if results.multi_hand_landmarks:
        # Get the hand landmarks for the first hand.
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get the index finger landmarks.
        index_finger_landmarks = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER]

        # Get the middle finger landmarks.
        middle_finger_landmarks = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER]

        # If the left index finger is up:
        if index_finger_landmarks.is_up:
            # Move the mouse cursor to the location of the left index finger.
            cv2.circle(frame, index_finger_landmarks.point, 10, (0, 255, 0), 2)
            cv2.imshow("Virtual Mouse", frame)

        # If the right index finger is up:
        elif middle_finger_landmarks.is_up:
            # Click the left mouse button.
            cv2.circle(frame, middle_finger_landmarks.point, 10, (0, 0, 255), 2)
            cv2.imshow("Virtual Mouse", frame)

    # If the `q` key is pressed, stop the loop.
    if cv2.waitKey(1) == ord('q'):
        break

# Close the video capture object.
cap.release()

# Close all windows.
cv2.destroyAllWindows()
