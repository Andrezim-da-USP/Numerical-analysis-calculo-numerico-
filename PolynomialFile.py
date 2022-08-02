
# POLYNOMIAL CLASS TO HANDLE POLYNOMIALS 

from __future__ import annotations

class Polynomial:
    def __init__(self, coeff:tuple):
        self.coeff = coeff
        self.n = len(coeff)
        self.deg = self.n - 1

    def __add__(self,other)->Polynomial:
        size = 1
        if self.n > other.n:
            size = self.n
            smaller = other.n
        else:
            size = other.n
            smaller = self.n
        result = []
        for i in range(smaller):
            result.append(self.coeff[i] + other.coeff[i])
        if smaller == other.n:
            for j in range(smaller,size):
                result.append(self.coeff[j])
        elif smaller == self.n:
            for j in range(smaller,size):
                result.append(other.coeff[j])
        return Polynomial(tuple(result))

    def __sub__(self, other)->Polynomial:
        size = 1
        if self.n > other.n:
            size = self.n
            smaller = other.n
        else:
            size = other.n
            smaller = self.n
        result = []
        for i in range(smaller):
            result.append(self.coeff[i] - other.coeff[i])
        if smaller == other.n:
            for j in range(smaller,size):
                result.append(self.coeff[j])
        elif smaller == self.n:
            for j in range(smaller,size):
                result.append(-other.coeff[j])
        return Polynomial(tuple(result))

    def __mul__(self:Polynomial, other:Polynomial)->Polynomial:
        n = self.n
        m = other.n
        result = [0 for i in range(m+n-1)]
        for i in range(n):
            for j in range(m):
                result[i+j] += self.coeff[i]*other.coeff[j]
        return Polynomial(tuple(result))
    
    def scalar_mul(self:Polynomial, scalar:float)->Polynomial:
        result = []
        for i in range(self.n):
            result.append(self.coeff[i]*scalar)
        return Polynomial(tuple(result))
    
    def __str__(self)->str:
        result = ''
        for i in range(self.n):
            if i == 0:
                result += str(self.coeff[i]) + ''
            else:
                result += str(self.coeff[i]) + 'x^' + str(i) 
            if i != self.n - 1:
                result += ' + '
            else: pass
        return result