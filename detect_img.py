import cv2
from mtcnn import MTCNN

# Load the image
image = cv2.imread('_MG_8135.JPG')

# Initialize the MTCNN model
detector = MTCNN()

# Detect faces in the image
faces = detector.detect_faces(image)

# Draw rectangles around detected faces
for face in faces:
    x, y, width, height = face['box']
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)


# Display or save the image
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the image with rectangles:
cv2.imwrite('output.jpg', image)
