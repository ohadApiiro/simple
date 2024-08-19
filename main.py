def bar(s, x):
    print(f'{s} {x}')


class Matoki:
    def foo(self, s, x):
        print(f'{s} {x}')


if __name__ == '__main__':
    metikut = Matoki()
    metikut.foo('matoki', 1)

