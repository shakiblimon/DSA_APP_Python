__author__ = "Shakib Limon"
__version__ = "1.0.0"

'''
    Hierarchy of Numeric Progressions
'''

class Prograssion:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current+=1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(''.join(str(next(self)) for j in range(n)))



'''
        Arithmetic Progression
'''

class ArithmeticProgression(Prograssion):
    def init (self, increment=1, start=0):
        super( ). init (start)
        self. increment = increment

    def advance(self):
        self. current += self. increment


'''
        A Geometric Progression Class
'''

class GeometricProgression(Prograssion):
    def __init__(self, base =2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *=self._base


'''
        A Fibonacci Progression Class
'''

class FibonacciProgression(Prograssion):
    def __init__(self, first=0, second =1):
        super().__init__(first)
        self._prev = second-first


    def _advance(self):
        self._prev, self._current = self._current, self._prev+ self._current


'''
        Testing Progression Now
'''

if __name__ == '__main__':
    print('Default prograssion: ')
    Prograssion().print_progression(10)

    print('Arithmetic prograssion with increment 5 is: ')
    ArithmeticProgression().print_progression(10)