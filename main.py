def bar(s, x):
    print(f'{s} {x}')


class Matoki:
    def foo(self, s, x):
        print(f'{s} {x}')

def func(s):
    print(s)
if __name__ == '__main__':
    func('bla')
    metikut = Matoki()
    metikut.foo('matoki', 1)


