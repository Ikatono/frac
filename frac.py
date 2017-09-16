#stores a rational number to perfect precision as a ratio of longs
#combines with ints to produce a frac ( except __rpow__() ) and with floats to produce a float
#comparisons with floats might not work perfectly for very similar numbers, I need to test out the float casting a bit
#it's possible that order w/r/t floats that differ near the limit of precision may not work properly, and even break ordering
#one solution would be casting floats to fracs instead of vice-versa

import numbers

class frac:
    
    def __init__(self, num, den):
        self.num = long(num)
        self.den = long(den)
        self.reduce()
    
    def __repr__(self):
        return 'frac(%d, %d)' % (self.num, self.den)
    
    def __str__(self):
        return '%d/%d' % (self.num, self.den)
    
    def __int__(self):
        return int(self.num / self.den)
    
    def __long__(self):
        return self.num / self.den
    
    def __float__(self):
        return float(self.num) / self.den
    
    def __bool__(self):
        return bool(self.num)
    
    def __add__(self, other):
        if isinstance(other, frac):
            newnum = self.num * other.den + other.num * self.den
            newden = self.den * other.den
            return frac(newnum, newden)
        elif isinstance(other, (int, long)):
            return frac(self.num + other * self.den, self.den)
        elif isinstance(other, float):
            return other + float(self)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, frac):
            newnum = self.num * other.den - other.num * self.den
            newden = self.den * other.den
            return frac(newnum, newden)
        elif isinstance(other, (int, long)):
            return frac(self.num - other * self.den, self.den)
        elif isinstance(other, float):
            return float(self) - other
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        return -1 * (self - other)
    
    def __mul__(self, other):
        if isinstance(other, frac):
            return frac(self.num * other.num, self.den * other.den)
        elif isinstance(other, (int, long)):
            return frac(self.num * other, self.den)
        elif isisntance(other, float):
            return float(self) * other
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, frac):
            return frac(self.num * other.num, self.den * other.den)
        elif isintance(other, (int, long)):
            return frac(self.num * other, self.den)
        elif isinstance(other, float):
            return float(self) * other
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, frac):
            return frac(other.num * self.den, self.num * other.den)
        elif isinstance(other, (int, long)):
            return frac(self.den * other, self.num)
        elif isinstance(other, float):
            return other / float(self)
        else:
            return NotImplemented
    
    def __pow__(self, other):
        if isinstance(other, frac):
            return float(self) ** float(other)
        elif isinstance(other, (int, long)):
            return frac(self.num ** other, self.den ** other)
        elif isinstance(other, float):
            return float(self) ** other
        else:
            return NotImplemented
    
    def __rpow__(self, other):
        if isinstance(other, frac):
            return float(other) ** float(self)
        elif isinstance(other, (int, long)):
            return other ** float(self)
        elif isinstance(other, float):
            return other ** float(self)
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, frac):
            return self.num * other.den < other.num * self.den
        else:
            return float(self) < other
    
    def __le__(self, other):
        if isinstance(other, frac):
            return self.num * other.den <= other.num * self.den
        else:
            return float(self) <= other
    
    def __eq__(self, other):
        if isinstance(other, frac):
            return self.num * other.den == other.num * self.den
        else:
            return float(self) == other
    
    def reduce(self):
        pass