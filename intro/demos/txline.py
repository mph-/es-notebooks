class LosslessTxLine:

    def __init__(self, Z0, Rs, Rl, l=1, v=0.5 * 3e8):

        self.Z0 = Z0
        self.Rs = Rs
        self.Rl = Rl
        self.v = v
        self.l = l
        self.T = l / v

    @property
    def GammaVs(self):

        return (self.Rs - self.Z0) / (self.Rs + self.Z0)

    @property
    def GammaVl(self):

        return (self.Rl - self.Z0) / (self.Rl + self.Z0)

    @property
    def GammaIs(self):

        return -self.GammaVs

    @property
    def GammaIl(self):

        return -self.GammaVl

    def Vstep(self, Vd, x, t):

        Nbounces = int(t // self.T)

        Gammal = self.GammaVl
        Gammas = self.GammaVs
        T = self.T
        v = self.v

        Vs = Vd * self.Z0 / (self.Rs + self.Z0)

        if (Nbounces & 1) == 0:
            # Outward propagating pulse.

            V = Vs * (Gammal * Gammas) ** (Nbounces // 2) * \
                ((x / v) <= (t - Nbounces * T))

            for b in range(Nbounces // 2):
                V += Vs * (1 + Gammal) * (Gammal * Gammas)**b

        else:
            # Inward propagating pulse.

            V = Vs * Gammal * \
                (Gammal * Gammas) ** (Nbounces // 2) * \
                (((self.l - x) / v) <= (t - Nbounces * T))

            for b in range((Nbounces - 1) // 2):
                V += Vs * (1 + Gammas) * Gammal * (Gammas * Gammal)**b
            V += Vs

        return V

    def Istep(self, Vd, x, t):

        Nbounces = int(t // self.T)

        Gammal = self.GammaIl
        Gammas = self.GammaIs
        T = self.T
        v = self.v

        Is = Vd / (self.Rs + self.Z0)

        if (Nbounces & 1) == 0:
            # Outward propagating pulse.

            I = Is * (Gammal * Gammas) ** (Nbounces // 2) * \
                ((x / v) <= (t - Nbounces * T))

            for b in range(Nbounces // 2):
                I += Is * (1 + Gammal) * (Gammal * Gammas)**b

        else:
            # Inward propagating pulse.

            I = Is * Gammal * \
                (Gammal * Gammas) ** (Nbounces // 2) * \
                (((self.l - x) / v) <= (t - Nbounces * T))

            for b in range((Nbounces - 1) // 2):
                I += Is * (1 + Gammas) * Gammal * (Gammas * Gammal)**b
            I += Is

        return I

    def Vpulse(self, Vd, t):

        Nbounces = int(t // self.T)

        Gammal = self.GammaVl
        Gammas = self.GammaVs

        Vs = Vd * self.Z0 / (self.Rs + self.Z0)

        if (Nbounces & 1) == 0:
            # Outward propagating pulse.

            return Vs * (Gammal * Gammas)**Nbounces

        else:
            # Inward propagating pulse.

            return Vs * Gammal * (Gammas * Gammal)**Nbounces
