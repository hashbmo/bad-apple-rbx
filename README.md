# bad apple rbx

### Getting setup

- **Required libraries / modules: opencv [cv2], waitres, flask**
- Load server.py into your IDE of choice
- If you have the appropriate modules/libraries preinstalled, skip to the next step, otherwise create a new virtual environment and install and the required modules/libraries using pip
- Ensure that the bad apple video is in the same folder as server.py (and correctly named)
- Run server.py [console should output: "server running"] if everything is working correctly
- Open roblox game file and click play

### Notes

- Python code serves video data by converting each frame into an RLE compressed serialized array and then subsequently adding the array to larger one to create the video.
- This is slightly more efficient than the way it was previously written, however there are still some optimisations that can be made (which I may implement in the future).
- As expected, this can use a decent amount of memory, the magnitude of which only increases with video resolution.
- You can play around with the files as you wish, however be warned that there's a good chance your game will crash if you set the request resolution too high.
- Have fun! :)

[Video Demonstration](https://www.youtube.com/watch?v=loY_9MptVA0)
