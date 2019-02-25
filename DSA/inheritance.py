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