class LosslessTxLine:

    def __init__(self, Z0, Rs, Rl, l=1, v=0.5 * 3e8):

        self.Z0 = Z0
        self.v = v
        self.l = l
        self.T = l / v

        # Perhaps these should not be attributes??
        self.Rs = Rs
        self.Rl = Rl

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

    def Ipulse(self, Vd, t):

        return self.Vpulse(Vd, t) / self.Z0

    def Vstep(self, Vd, x, t, Vt=0):

        Nbounces = int(t // self.T)

        Gammal = self.GammaVl
        Gammas = self.GammaVs
        T = self.T
        v = self.v

        V0 = self.Rs / (self.Rs + self.Rl) * Vt
        Vp = Vd * self.Z0 / (self.Rs + self.Z0) - V0

        if (Nbounces & 1) == 0:
            # Outward propagating pulse.

            V = Vp * (Gammal * Gammas) ** (Nbounces // 2) * \
                ((x / v) <= (t - Nbounces * T))

            for b in range(Nbounces // 2):
                V += Vp * (1 + Gammal) * (Gammal * Gammas)**b

        else:
            # Inward propagating pulse.

            V = Vp * Gammal * \
                (Gammal * Gammas) ** (Nbounces // 2) * \
                (((self.l - x) / v) <= (t - Nbounces * T))

            for b in range((Nbounces - 1) // 2):
                V += Vp * (1 + Gammas) * Gammal * (Gammas * Gammal)**b
            V += Vp

        return V + V0

    def Istep(self, Vd, x, t, Vt=0):

        Nbounces = int(t // self.T)

        Gammal = self.GammaIl
        Gammas = self.GammaIs
        T = self.T
        v = self.v

        I0 = -Vt / (self.Rs + self.Rl)
        Ip = Vd / (self.Rs + self.Z0)

        if (Nbounces & 1) == 0:
            # Outward propagating pulse.

            I = Ip * (Gammal * Gammas) ** (Nbounces // 2) * \
                ((x / v) <= (t - Nbounces * T))

            for b in range(Nbounces // 2):
                I += Ip * (1 + Gammal) * (Gammal * Gammas)**b

        else:
            # Inward propagating pulse.

            I = Ip * Gammal * \
                (Gammal * Gammas) ** (Nbounces // 2) * \
                (((self.l - x) / v) <= (t - Nbounces * T))

            for b in range((Nbounces - 1) // 2):
                I += Ip * (1 + Gammas) * Gammal * (Gammas * Gammal)**b
            I += Ip

        return I + I0
