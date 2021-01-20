import sys

from Palindromo import mT_palindromo

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Uso:")
        print("python Test.py Palabra")
        print("donde Palabra es la palabra para ser probada como un palíndromo")
        sys.exit(0)

    Palabra = sys.argv[1]
    mT_palindromo(Palabra)