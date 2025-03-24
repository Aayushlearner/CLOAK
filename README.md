# Invisibility Cloak Effect using OpenCV

## Overview
This project creates an "invisibility cloak" effect using a webcam and OpenCV. It makes a specific color (e.g., green cloth) invisible by replacing it with the background captured earlier.

## How It Works
1. **Background Capture**: The program captures a static background frame when the script starts.
2. **Color Calibration**: The user calibrates the color to be made invisible by placing it in front of the camera and pressing `c` to capture the color. The program calculates the HSV range for the selected color.
3. **Invisibility Effect**: The program detects the calibrated color in the live video feed, creates a mask, and replaces the detected color region with the corresponding area from the background frame.

## Instructions
1. **Place the color** to be made invisible in front of the camera.
2. **Press `c`** to capture the color.
3. **Press `q`** to quit calibration and start the invisibility effect.
4. **Press `q`** while the video window is active to exit the program.

## Example Use Case
Use a green cloth as the "invisibility cloak". When you hold it in front of the camera, the program will replace the green area with the background, making it appear as if you are invisible.

## Notes
- Ensure the background remains static after the initial capture.
- The effectiveness of the effect depends on the lighting conditions and the distinctness of the selected color from the background.
- You can adjust the HSV range in the `calibrate_color()` function for better results.

## Limitations
- The effect may not work well in low-light conditions or if the background changes dynamically.
- The selected color should not be present in the background, as it will also be replaced.

## Future Improvements
- Add support for dynamic background updates.
- Implement a GUI for easier calibration and control.
- Extend the effect to work with multiple colors or patterns.

---

Enjoy creating your invisibility effect! 🎥✨


