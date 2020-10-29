import cv2

def liveSketch():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        cv2.imshow("Live Sketch", sketch(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def sketch(image):
    # Convert image to gray scale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract Edges
    canny_edges = cv2.Canny(img_gray_blur, 32, 72)

    # Do an invert binarize the image
    success, img = cv2.threshold(canny_edges, 120, 255, cv2.THRESH_BINARY_INV)

    return img

liveSketch()