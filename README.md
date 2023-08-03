Do you know these?

![image](https://github.com/SinanAkkoyun/POV/assets/43215895/76b96782-e845-4a29-8a14-507caa78b212)

Yup, now, you can easily simulate them in your fav 3D modelling software.


# POV simulation

This repo will show you how to design your own POV display and view the final result.
(WIP)

# 1: Model your POV display in Blender.
Choose a high refresh rate (I used 240Hz) and model all the LED timings in such a way, that a full rotation equals "one second" (240 frames), but this full revolution does not represent real time.

Blender driver examples:
Rotation: `-((frame/57.3)/240*360)`
LED Driver: `(abs(cos(frame/240*pi*2))>0.99925)`

# 2: Render the full revolution into EXR file format as an image sequence.

# 3: Copy the averageexr.py script into the image sequence folder and run `python3 averageexr.py`

# 4: Enjoy your final POV image!




# Q&A:

Q: How does it work?
A: This works by mimicking how our human eye and the persistence of vision works.
I first tried to simply enable motion blur but Blender does not interpolate well in-between frames with changing material properties (just uses the motion vec and the mat properties in the current frame) and it would not represent a true POV image.
By my method, you render a full revolution out and then my script averages every sinlge frame together. This somewhat achieves the same effect as a camera recording one image with the shutter open for a full revolution. This way, we can, just like we would in real life, see the integral of all momentary snapshots of the POV display in one picture.

Q: Why EXR and not PNG/JPG?
A: First, I tried to use PNG files but quickly realized that the display would not be visible at all. In a POV display, the LEDs need to be very bright so that the short time period the LED is seen by the eye gets compensated for.
When increasing the intensity, in a normal PNG file it will just clip to the same white (1,1,1), which in fact is way too dimm for a POV display and thus just vanishes. On the other hand, when using EXR images, the full intensity information gets preserved and correctly averaged.
The final output will be an image in sRGB color space.


NOTE: I wrote that script on my own and do not know python that well. Feel free to enhhance it!
