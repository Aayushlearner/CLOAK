Invisibility Cloak with Color Calibration

Overview

This project implements an Invisibility Cloak Effect using OpenCV, allowing users to calibrate a custom color for invisibility. Unlike fixed color detection, this version enables real-time calibration, making it more flexible for different lighting conditions and colors.

How It Works

Color Calibration: The script prompts the user to place the desired color in front of the camera and press c to capture it.

Background Capture: The script captures an initial background frame after waiting for 2 seconds.

Color Detection: The selected color is detected in real-time using its HSV range.

Mask Processing: Noise reduction techniques like blurring, dilation, and morphological transformations are applied.

Background Replacement: The detected color is replaced with the initial background, creating the invisibility effect.

Live Display: The processed frame is displayed in real-time, and the user can press q to exit.

Requirements

Ensure you have Python installed along with the required dependencies:

pip install opencv-python numpy

Usage

Run the script:

python invisibility_cloak.py

Follow the calibration steps:

Place the color you want to make invisible in front of the camera.

Press c to capture the color.

The script will display the selected HSV range.

Press any key to continue after calibration.

Wear the selected color and observe the invisibility effect.

Press q to exit.

Customization

Change HSV Range Sensitivity: Modify the tolerance values (±10 Hue, ±50 Saturation, ±50 Value) in calibrate_color().

Improve Detection: Adjust blurring (medianBlur), dilation, and morphological operations.

Change the Effect Color: Instead of pink, select any color dynamically during calibration.

Troubleshooting

Color not detected properly? Adjust the HSV tolerance.

Too much noise or flickering? Increase mask smoothing with better filtering.

Background not captured? Ensure stable lighting and no rapid movements during calibration.

Credits

Developed using: OpenCV & NumPy

Inspired by: Real-time computer vision applications & invisibility cloak techniques.

Enjoy experimenting with this dynamic invisibility effect! 🚀
