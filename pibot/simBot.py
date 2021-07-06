import threading
from time import sleep
from math import cos, sin, pi


class Nano:

    m_left = 0
    m_right = 0

    e_left = 0
    e_right = 0

    dist_left = 10
    dist_mid = 100
    dist_right = 0
    # distance to right wall at start
    dist_right_start = 10

    alpha_rad = 0
    alpha_deg = 0
    pos_vec = [0, 0]
    old_len = 0
    x_old = 0

    def __init__(self):
        # Reset Nano
        print("Simulating Nano...")
        self.reset_nano()
        threading.Thread(target=self.set_encoders).start()

    def set_encoders(self):

        while True:
            self.e_left += (self.m_left * 1.75)
            self.e_right += (self.m_right * 1.8)
            self.update_distances()
            sleep(0.1)

    def set_stat_led(self, toggle):
        pass

    def set_motors(self, left, right):

        self.m_left = left
        self.m_right = right

    def get_encoders(self):
        sleep(0.1)
        return int(self.e_left), int(self.e_right)

    def reset_encoders(self):

        self.e_left = 0
        self.e_right = 0

    def calc_angle(self, b1, b2, bot_width):
        # 1cm ~ 18 Ticks
        self.alpha_rad = (b2 - b1) / (18 * bot_width)
        if self.alpha_rad >= 2*pi:
            self.alpha_rad -= 2*pi
        self.alpha_deg = (180 / pi) * self.alpha_rad

    def calc_pos_x(self, enc):
        length = ((enc[0] + enc[1]) / 2 / 18) - self.old_len
        x_new = length * sin(self.alpha_rad)
        self.x_old += x_new
        self.old_len += length

    def update_distances(self):
        bot_width = 11.3
        enc = self.get_encoders()
        self.calc_angle(enc[0], enc[1], bot_width)
        self.calc_pos_x(enc)
        dist = self.x_old / cos(self.alpha_rad) + self.dist_right_start
        if dist > 3000 or dist < 0:
            dist = 0
        self.dist_right = dist

    # you can adept this function to your needs
    def get_distances(self):
        self.dist_mid = 100 - self.e_left // 18
        sleep(0.15)
        return int(self.dist_left), int(self.dist_mid), int(self.dist_right)

    def set_buzzer(self, freq, duration):
        pass

    def reset_nano(self):

        self.m_left = 0
        self.m_right = 0

        self.e_left = 0
        self.e_right = 0

        self.dist_mid = 100
