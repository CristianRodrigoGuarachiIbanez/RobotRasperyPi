"""
Ta = Abtastzeit
Kp = Verstärkungsfaktor
Ki = Regelungsfaktor
w = soll
x = ist
esum = esum + e
Kd = Regelungsfaktor
ealt = e
e = w - x
"""


class Pid:

    # set values for PID
    e_alt = 0
    e_sum = 0
    m_left_new = 0
    m_right_new = 0

    def set_motors(self, nano, m_left, m_right):

        kp = 0.0005
        ki = 0.001
        kd = 0.0001
        Ta = 0.0001

        val_should = m_left - m_right
        e_left, e_right = nano.get_encoders()
        val_is = e_left - e_right
        e = val_should - val_is
        self.e_sum = self.e_sum + e

        val_corr = kp * e + ki * Ta * self.e_sum + kd * (e - self.e_alt) / Ta
        self.e_alt = e

        self.m_left_new += val_corr

        nano.set_motors(int(m_left + self.m_left_new),
                        int(m_right + self.m_right_new))
