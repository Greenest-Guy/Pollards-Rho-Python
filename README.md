# Pollards-Rho-Python
A simple Python implementation of Pollard's Rho algorithm for integer factorization.

```python
# Pollard's Rho Algorithm for Integer Factorization
import random
import math


class PollardsRho:
    def __init__(self, num):
        self.num = num

    def factorize(self):
        if self.num <= 0:
            raise ValueError("Number must be a positive integer")
        if self.num == 1:
            return 1
        if self.num % 2 == 0:
            return 2

        x = random.randint(2, self.num - 1)
        y = x
        c = random.randint(1, self.num - 1)
        d = 1

        while d == 1:
            x = (pow(x, 2, self.num) + c) % self.num

            y = (pow(y, 2, self.num) + c) % self.num
            y = (pow(y, 2, self.num) + c) % self.num

            d = math.gcd(abs(x - y), self.num)

        return d
```

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Rho-example-animated.gif" width="400">
