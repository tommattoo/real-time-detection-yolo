import cv2
from ultralytics import YOLO

# Load the pre-trained YOLOv8 model (you can change this to a custom model if needed)
model = YOLO('yolov8n.pt')  # Pre-trained YOLOv8 model. You can also use 'yolov8s.pt', 'yolov8m.pt', etc.

# Open the camera (0 is typically the default webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Infinite loop for real-time detection
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform object detection
    results = model(frame)

    # Since results is a list, get the first result (if there are multiple)
    result = results[0]

    # Render the results on the frame (use the plot() method)
    frame_with_results = result.plot()  # Draw bounding boxes and labels on the frame

    # Display the resulting frame
    cv2.imshow("Real-Time Object Detection", frame_with_results)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close windows
cap.release()
cv2.destroyAllWindows()



