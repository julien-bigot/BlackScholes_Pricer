import numpy as np
from scipy.stats import norm

N = norm.cdf
N_prime = norm.pdf


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

    def delta(self):

        if self.CP == "C":

            return N(self.d1() * np.exp(-self.q * self.T))

        if self.CP == "P":

            return N(self.d1()) - 1 * np.exp(-self.q * self.T)

        else:

            print("please enter either C or P")

    def gamma(self):

        if self.CP == "C" or "P":  # Gamma is the same for both call and put

            return (N_prime(self.d1()) * np.exp(-self.q * self.T)) / (self.S * self.v * np.sqrt(self.T))

        else:

            print("please enter either C or P")

    def vega(self):

        if self.CP == "C" or "P":  # Vega is the same for both call and put

            return (N_prime(self.d1()) * self.S * np.sqrt(self.T) * np.exp(-self.q * self.T)) / 100

    def theta(self):

        if self.CP == "C":

            #return 1/self.T * (-(N_prime(self.d1())) * (self.S * self.v * np.exp(-self.q * self.T)) / 2 * np.sqrt(self.T)) \
              #     - N(self.d2() * self.r * self.K * np.exp(-self.r * self.T) +
               #        N(self.d1() * self.q * self.S * np.exp(-self.q * self.T)))

            '''return - np.exp(-self.q * self.T) * self.S * self.v * N_prime(self.d1()) / (2 * np.sqrt(self.T)) \
                       + self.q * np.exp(-self.q * self.T) * self.S * N(self.d1()) \
                       - self.r * np.exp(-self.r * self.T) * self.K * N(self.d2())'''

            return -((N_prime(self.d1() * self.v * self.S)) / (2 * np.sqrt(self.T))) - ((N(self.d2() * self.r * self.K * np.exp(-self.r * self.T))))

        if self.CP == "P":

            return -((N_prime(self.d1() * self.v * self.S)) / (2 * np.sqrt(self.T))) + (-N(self.d2() * self.r * self.K * np.exp(-self.r * self.T)))

    def theta_bis(self):

        p1 = - self.S * N_prime(self.d1()) * self.v / (2 * np.sqrt(self.T))
        p2 = self.r * self.K * np.exp(-self.r * self.T) * N(self.d2())

        return p1 - p2









