def main():
    start_h, start_m, start_s = map(int, input().split(':'))
    end_h, end_m, end_s = map(int, input().split(':'))

    add_s = end_s - start_s
    if(add_s < 0):
        add_s = end_s + (60-start_s)
        start_m += 1
    add_m = end_m - start_m
    if(add_m < 0):
        add_m = end_m + (60-start_m)
        start_h += 1
    add_h = end_h - start_h
    if(add_h < 0):
        add_h = end_h + (24-start_h)
    
    if(add_h == 0 and add_m == 0 and add_s == 0):
        add_h = 24
    
    add_s = str(add_s)
    add_m = str(add_m)
    add_h = str(add_h)

    if len(add_s) == 1:
        add_s = "0" + add_s
    if len(add_m) == 1:
        add_m = "0" + add_m
    if len(add_h) == 1:
        add_h = "0" + add_h

    print("{}:{}:{}".format(add_h, add_m, add_s))
        

if __name__ == "__main__":
    main()
