import numpy as np
from scipy.stats import norm

N = norm.cdf


class BSOption:

    def __init__(self, CP, S, K, T, r, v, q=0):

        self.CP = CP
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.v = v
        self.q = q

    def d1(self):

        return (np.log(self.S / self.K) + (self.r - self.q + 0.5 * self.v ** 2)) * self.T / (self.v * np.sqrt(self.T))

    def d2(self):

        return self.d1() - self.v * np.sqrt(self.T)

    def price(self):

        if self.CP == "C":

            return self.S * N(self.d1()) - self.K * np.exp(-self.r * self.T) * N(self.d2())

        elif self.CP == "P":

            return N(-self.d2()) * self.K * np.exp(-self.r * self.T) - N(-self.d1()) * self.S




