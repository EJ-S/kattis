def main():
    eye = input()
    count_before = 0
    count_after = 0
    found = False
    for c in eye:
        if found:
            if c != ")":
                count_after += 1
        else:
            if c == "(":
                found = True
            else:
                count_before += 1
    if(count_before == count_after):
        print("correct")
    else:
        print("fix")

        



if __name__ == "__main__":
    main()
