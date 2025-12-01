import cv2


def main():
    cap = cv2.VideoCapture(0)  # open the default camera

    key = ord("a")
    while key != ord("q"):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame comes here
        # Convert RGB image to grayscale
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur the image
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        # Detect edges on the blurred image
        img_edges = cv2.Canny(img_filtered, 0, 30, 3)

        # Display the result of our processing
        cv2.imshow("result", img_edges)
        # Wait a little (30 ms) for a key press - this is required to refresh the image in our window
        key = cv2.waitKey(30)

    # When everything done, release the capture
    cap.release()
    # and destroy created windows, so that they are not left for the rest of the program
    cv2.destroyAllWindows()


def zad1():
    img = cv2.imread("lab1/Screenshot 2025-10-06 160242.png", cv2.IMREAD_COLOR)
    cv2.imshow("res", img)
    cv2.waitKey(0)
    # cv2.imwrite("lab1/newimg.png",img)

    print(type(img))
    print(img.shape)

    print(f"jasnosc piksela 270x270: {img[270, 270]}")

    roi = img[270:370, 270:370]
    # cv2.imshow("roi",roi,cv2.IMREAD_COLOR)
    # cv2.waitKey(0)

    cv2.imshow("new colors", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)


def zad2():
    img = cv2.imread("lab1/AdditiveColor.png", cv2.IMREAD_COLOR)
    cv2.imshow("def", img)
    cv2.waitKey(0)

    imgr, imgg, imgb = cv2.split(
        img,
    )

    cv2.imshow("red", imgr)
    cv2.imshow("green", imgg)
    cv2.imshow("blue", imgb)
    cv2.waitKey(0)

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    cv2.imshow("red", r)
    cv2.imshow("green", g)
    cv2.imshow("blue", b)
    cv2.waitKey(0)


def zad3():
    cap = cv2.VideoCapture(0)

    key = 32
    while key != ord("q"):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ord(" ") == key:
            cv2.imshow("frame", frame)

        cv2.waitKey(0)


if __name__ == "__main__":
    zad3()
