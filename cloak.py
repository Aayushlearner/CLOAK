import cv2
import numpy as np

def calibrate_color():
    print("\nColor Calibration Mode:")
    print("1. Place the color you want to make invisible in front of the camera")
    print("2. Press 'c' to capture the color")
    print("3. Press 'q' to quit calibration")
    
    # Create a window to show calibration
    cv2.namedWindow("Calibration")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Display the frame
        cv2.imshow("Calibration", frame)
        
        # Wait for keyboard input
        key = cv2.waitKey(1)
        
        if key == ord('c'):  # Capture color
            # Convert to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # Get the color from the center of the frame
            center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
            selected_color = hsv[center_y, center_x]
            
            # Create a range around the selected color
            lower_hsv = np.array([
                max(0, selected_color[0] - 10),  # Hue
                max(0, selected_color[1] - 50),  # Saturation
                max(0, selected_color[2] - 50)   # Value
            ])
            upper_hsv = np.array([
                min(179, selected_color[0] + 10),  # Hue
                min(255, selected_color[1] + 50),  # Saturation
                min(255, selected_color[2] + 50)   # Value
            ])
            
            print(f"\nSelected color HSV: {selected_color}")
            print(f"HSV Range: {lower_hsv} to {upper_hsv}")
            print("\nCalibration complete! Press any key to start the invisibility effect.")
            cv2.waitKey(0)
            cv2.destroyWindow("Calibration")
            return lower_hsv, upper_hsv
            
        elif key == ord('q'):  # Quit
            cv2.destroyWindow("Calibration")
            return None, None

# Initialize webcam
cap = cv2.VideoCapture(0)

# Capture the background frame (Wait 2 seconds for stability)
cv2.waitKey(2000)
ret, init_frame = cap.read()
if not ret:
    print("Error: Could not capture background frame.")
    cap.release()
    exit()

# Calibrate color
print("\nStarting color calibration...")
lower_hsv, upper_hsv = calibrate_color()

if lower_hsv is None:
    print("Color calibration cancelled. Exiting...")
    cap.release()
    exit()

# Create a kernel for smoothing mask
kernel = np.ones((5,5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for detecting the selected color
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 7)  # Reduce noise more
    mask = cv2.dilate(mask, kernel, iterations=2)  # Expand the detected areas more
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # Fill small holes
    mask_inv = cv2.bitwise_not(mask)  # Invert mask

    # Extract non-cloak regions from current frame
    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Extract cloak region from the background frame
    cloak_area = cv2.bitwise_and(init_frame, init_frame, mask=mask)

    # Combine both parts
    final_output = cv2.addWeighted(frame_bg, 1, cloak_area, 1, 0)

    # Display result
    cv2.imshow("Invisibility Effect", final_output)

    # Press 'q' to exit
    if cv2.waitKey(3) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
