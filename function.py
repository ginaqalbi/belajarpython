def penambahan():
    a = 5
    b = 3
    return a + b


def added(a: int, b: int) -> float:
    # function with parameter
    return a + b


def NilaiGenap(a: list):
    # buat code disini
    for i in a:
        if i % 2 == 0:
            print('Bilangan Genap:', i)


if __name__ == "__main__":
    x = 3.0
    y = 5

    c = added(x, y)

    print(c)

    data = [2, 5, 7, 8, 13, 27]

    NilaiGenap(data)
