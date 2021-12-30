def main():
    while True:
        try:
            eq = input()
        except EOFError:
            break
        print("{:.2f}".format(eval(eq)))


if __name__ == "__main__":
    main()