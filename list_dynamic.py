"""
buatlah sebuah fungsi dengan parameter bertype list, dimana fungsi tersebut akan mencetak nilai genap dari nilai parameter-nya 
"""


def NilaiGenap(a: list):
    for i in a:
        if i % 2 == 0:
            print('Bilangan genap:', i)


if __name__ == "__main__":
    data = [1, 2, 4, 5, 6, 7, 10, 23, 47, 90]  # static
    list_a = []

    for n in data:
        if n % 2 != 0:
            list_a.append(n)

    print(list_a)
    print(list_a[0:3])
    print(list_a[-1])

    print(data[2:7])
    print(len(data))
    NilaiGenap(data)
