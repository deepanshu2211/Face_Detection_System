import cv2
from mtcnn import MTCNN

# Replace 'input_video.mp4' with the path to your input video file
input_video_path = 'Video.mp4'
output_video_path = 'output_video.mp4'

# Initialize the video capture
video_capture = cv2.VideoCapture(input_video_path)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
output_video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (1080, 720))  # Output file name and parameters

# Initialize the MTCNN model
detector = MTCNN()

while True:
    ret, frame = video_capture.read()  # Read a frame from the input video

    if not ret:
        break

    # Detect faces in the frame
    faces = detector.detect_faces(frame)

    # Draw rectangles around detected faces
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)  # Red color

    # Write the frame to the output video
    output_video.write(frame)

# Release the video writer and video capture
output_video.release()
video_capture.release()

# Close all windows
cv2.destroyAllWindows()
