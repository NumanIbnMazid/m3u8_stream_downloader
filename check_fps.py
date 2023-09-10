import cv2

# Path to the video file
video_path = '/home/numan/Workspace/GENISTAT/UTILS/m3u8_stream_downloader/downloaded_stream/my_video.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open video file.")    
    exit()

# Get the frames per second (fps) of the video  
fps = (cap.get(cv2.CAP_PROP_FPS))

# Print the fps
print(f"Frames per Second (fps): {fps}")

# Release the video file
cap.release()
