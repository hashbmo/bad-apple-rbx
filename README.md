# bad apple rbx

### Getting setup

- Load server.py into your IDE of choice
- If you have the appropriate modules/libraries preinstalled, skip to the next step, otherwise create a new virtual environment and install and the required modules/libraries using pip
- Ensure that the bad apple video is in the same folder as server.py (and correctly named)
- Run server.py [console should output: "server running"] if everything is working correctly
- Open roblox game file and click play

### Notes

- Python code serves video data by converting each frame into a lightly compressed 2D array, serially adding it to a larger array and then JSON encoding the entire thing
- As you might expect, this requires a large amount of ram, the magnitude of which only increases with video resolution
- Although this can likely be heavily rectified by further compressing the data with an algorithm such as RLE (a route that I did ultimately explore on the server side), laziness won over and having a lag spike before the video starts rendering is preferrable to optimizing and debugging an RLE decoder in-game
- If you tamper with the code and make the resolution too large, it will likely crash roblox due to the way it loads the video data
- Like my previous project, this only works locally but I'm considering making it web based
