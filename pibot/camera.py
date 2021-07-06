from time import sleep

import cv2
import imutils as imutils
from picamera.array import PiRGBArray
from picamera import PiCamera


class Camera:
    def __init__(self, width=640, height=480):
        """
        Initializes the camera
        :param width: width of the images captured by the camera
        :param height: height of the images captured by the camera
        """
        self.width = width
        self.height = height
        self.RED_LOWER = (125, 0, 0)
        self.RED_UPPER = (255, 100, 100)
        self.BLUE_LOWER = (0, 0, 125)
        self.BLUE_UPPER = (100, 100, 255)
        self.windows = []

    def rotate_image(self, orig, angle):
        """
        Rotates an image
        :param orig: The image to be rotated
        :param angle: The angle of the rotation
        :return: The rotated image
        """
        dimensions = (self.width // 2, self.height // 2)
        mat = cv2.getRotationMatrix2D(dimensions, angle, 1)
        rotated = cv2.warpAffine(orig, mat, (self.width, self.height))
        return rotated

    def capture_image(self):
        """
        Captures one image from the camera
        :return: the image captured by the camera
        """
        with PiCamera() as camera:
            camera.resolution = (self.width, self.height)
            with PiRGBArray(camera, size=(self.width, self.height)) as output:
                output.truncate(0)
                camera.capture(output, 'bgr', use_video_port=True)
                return self.rotate_image(output.array.copy(), 180)

    def capture_multiple_images(self, amount, delay):
        """
        Captures multiple images
        :param amount: (int) How many images should be captured
        :param delay: (int or float) The time between two captures
        :return: (list) a list of the captured images
        """
        with PiCamera() as camera:
            camera.resolution = (self.width, self.height)
            with PiRGBArray(camera, size=(self.width, self.height)) as output:
                images = []
                if amount > 128:
                    amount = 128
                for _ in range(amount):
                    output.truncate(0)
                    camera.capture(output, 'bgr', use_video_port=True)
                    images.append(self.rotate_image(output.array.copy(), 180))
                    sleep(delay)
                return images

    def check_for_ball(self, image, color, radius):
        """
        Checks if the image contains a ball with the specified color
        :param image: (2d color array) The image to be checked
        :param color: (str) Either red or blue
        :param radius: (int or float) The radius which the ball needs to be
        recognized as a ball (in px)
        :return: (tuple) returns two values: boolean whether the ball is
        detected or not and the (manipulated) image
        """
        if image is not None:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if color == "red":
                mask = cv2.inRange(rgb, self.RED_LOWER, self.RED_UPPER)
                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
            elif color == "blue":
                mask = cv2.inRange(rgb, self.BLUE_LOWER, self.BLUE_UPPER)
                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
            else:
                raise Exception("Only check for red or blue ball is \
                supported. Given: {}".format(color))

            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), r) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                if M["m00"] > 0:
                    center = (int(M["m10"] /
                              M["m00"]), int(M["m01"] /
                              M["m00"]))

                    # only proceed if the radius meets a minimum size
                    if r > radius:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                        image_manipulated = image.copy()
                        cv2.circle(image_manipulated,
                                   (int(x), int(y)),
                                   int(r), (0, 255, 255), 2)
                        cv2.circle(image_manipulated,
                                   center, 5, (0, 0, 255), -1)
                        return True, image_manipulated
            return False, image
        else:
            raise Exception("You haven't captured an image yet")

    def view_image(self, image, window_name):
        """
        Views an image
        :param image: The image to be viewed
        :param window_name: The name of the window where the image should
        be put in
        """
        cv2.imshow(window_name, image)
        if window_name not in self.windows:
            cv2.waitKey(1000)
