class LosslessTxLine:

    def __init__(self, Z0, Zs, Zl, l=1, v=0.5 * 3e8):

        self.Z0 = Z0
        self.Zs = Zs
        self.Zl = Zl
        self.v = v
        self.l = l
        self.T = l / v

    @property
    def GammaVs(self):

        return (self.Zs - self.Z0) / (self.Zs + self.Z0)

    @property
    def GammaVl(self):

        return (self.Zl - self.Z0) / (self.Zl + self.Z0)

    @property
    def GammaIs(self):

        return -self.GammaVs

    @property
    def GammaIl(self):

        return -self.GammaVl

    def V(self, Vd, x, t):

        Nbounces = int(t // self.T)

        Gammal = self.GammaVl
        Gammas = self.GammaVs
        T = self.T
        v = self.v

        Vs = Vd * self.Z0 / (self.Zs + self.Z0)

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
