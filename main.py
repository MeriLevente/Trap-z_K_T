def kerulet(a: float, b: float, c: float, d: float) -> float:
    return a + b + c + d


def terulet(a: float, c: float, m: float) -> float:
    return (a + c) / 2 * m


def Main() -> None:
    print('Trapéz K és T:')
    a: float = float(input("a:"))
    b: float = float(input("b:"))
    c: float = float(input("c:"))
    d: float = float(input("d:"))
    m: float = float(input("m:"))
    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or m <= 0:
        print('Nincs ilyen trapéz!')
    else:
        print(f'Trapéz kerülete: {kerulet(a, b, c, d)}')
        print(f'Trapéz területe: {terulet(a, c, m)}')


if __name__ == "__main__":
    Main()
