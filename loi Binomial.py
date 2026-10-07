class Math:

    def __init__ (self):
        pass

    def factorielle(self, n):
        result = 1

        for i in range(1, n+1):
            result = result * i
        
        return result

class Binomial(Math):

    def __init__(self):
        super().__init__()

    def coef_binomial(self, n, k):
        if k < 0 or k > n:
            return 0

        result = self.factorielle(n) // (self.factorielle(k) * self.factorielle(n - k))
        return result

    def p_exact(self, n, p, k):
        result = self.coef_binomial(n, k) * p**k * (1 - p)**(n-k)
        return(result)

    def p_inferieur_ou_egal(self, n, p, k):
        result = 0

        for i in range(1, k+1):
            result += self.p_exact(n, p, i)

        return result

    def echantillonage(self, n, p):
        for a in range(0, n+1):
            result = self.p_inferieur_ou_egal(n, p, a)

            if result >= 0.95:
                print("-> Seuil atteint à a = ", a, "| P(X <= a) = ", result, "\n")
                return a

            print("a = ", a, "| P(X <= a) = ", result,)
