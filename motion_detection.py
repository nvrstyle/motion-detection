import argparse
import cv2

def main():
    # construct the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", type=str, help="path to the video file")
    parser.add_argument("-a", "--min-area", type=int, default=100, help="minimum area size")
    args = parser.parse_args()

    if args.video:
        video = cv2.VideoCapture(args.video)
    else:
        video = cv2.VideoCapture(0)

    reference_frame = None

    while True:

        status, frame = video.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        if reference_frame is None:
            reference_frame = blur_frame
            continue

        delta_frame = cv2.absdiff(reference_frame, blur_frame)
        thresh_frame = cv2.threshold( delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        dilate_frame = cv2.dilate(thresh_frame, None, iterations =2)

        #if we are using OpenCV 3.X, replace  (cnts, _) on (_, cnts, _)
        (cnts, _) = cv2.findContours(dilate_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < args.min_area :
                continue
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)

        cv2.imshow("Gray frame", gray_frame)
        cv2.imshow("Blur frame", blur_frame)
        cv2.imshow("Delta frame", delta_frame)
        cv2.imshow("Thresh frame", thresh_frame)
        cv2.imshow("Dilate frame", dilate_frame)
        cv2.imshow("Complete frame", frame)

        keypressed = cv2.waitKey(1)
        if keypressed == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    main()