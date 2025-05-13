<h1>Dino Autp</h1>
<hr><p>Automates google's dino game</p><h2>General Information</h2>
<hr><ul>
<li>Game Automation Script
Overview
This Python script automates gameplay for a game (e.g., Chrome's Dinosaur Game) by taking screenshots, analyzing a specific region for obstacles, and simulating key presses to avoid them. It uses the pyautogui library for screenshot capture and keyboard simulation, PIL for image processing, and keyboard for detecting a quit condition.
Requirements</li>
</ul>
<p>Python: Version 3.x
Libraries:
Pillow (PIL): For image processing
pyautogui: For screenshot capture and key simulation
keyboard: For detecting key presses</p>
<p>Install dependencies using:pip install pillow pyautogui keyboard</p>
<p>Operating System: Tested on Windows; may require adjustments for macOS/Linux due to keyboard and pyautogui behavior.
Permissions: Run the script with administrator privileges (required for keyboard on some systems).</p>
<p>Usage</p>
<p>Prepare the Game:
Open the game window (e.g., Chrome Dinosaur Game by navigating to chrome://dino in Google Chrome).
Ensure the game is visible and focused.</p>
<p>Run the Script:
Save the script as game_automation.py.
Execute it using:python game_automation.py</p>
<p>Script Behavior:
The script waits 3 seconds, allowing you to switch to the game window.
It presses the "space" key to start the game.
It continuously captures screenshots, converts them to grayscale, and checks a predefined region (coordinates: left=220, top=520, right=300, bottom=580) for dark pixels (pixel value &lt; 100).
If an obstacle is detected, it presses the "space" key to jump and waits 0.1 seconds.
The loop runs every 0.005 seconds.
Press the "q" key to stop the script.</p>
<p>Debugging:
The script prints pixel values for the scanned region to the console.
If an obstacle is detected, it saves a screenshot as debug_screenshot.png for analysis.</p>
<p>Customization</p>
<p>Region Coordinates: Adjust left, top, right, bottom in the is_obstacle_present function to match the game's obstacle detection area.
Pixel Threshold: Modify the pixel_value &lt; 100 condition to adjust sensitivity for obstacle detection.
Timing: Change time.sleep(0.1) or time.sleep(0.005) to fine-tune response speed.
Key Input: Replace "space" with another key if the game uses a different control.</p>
<p>Notes</p>
<p>Performance: Frequent screenshot capture may impact system performance. Adjust time.sleep(0.005) if needed.
Game Compatibility: The script is tailored for games with a consistent obstacle appearance (e.g., dark objects on a light background). Test and adjust coordinates/thresholds for other games.
Safety: pyautogui simulates key presses, so ensure the game window is active to avoid unintended inputs elsewhere.
Debugging Tip: Use the saved debug_screenshot.png to verify the detection region's accuracy.</p>
<p>Limitations</p>
<p>The script assumes a fixed game window position and resolution.
It may not work reliably on high-DPI displays or scaled resolutions without coordinate adjustments.
The keyboard library may require root/admin access on some systems.</p>
<p>License
This script is provided as-is for educational purposes. Use responsibly and ensure compliance with the game's terms of service.</p><h2>Technologies Used</h2>
<hr><ul>
<li>python</li>
</ul>
