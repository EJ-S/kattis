import sys


def main():
    cin = sys.stdin.readlines()
    monthly_mb = int(cin[0])
    months = int(cin[1])
    out = monthly_mb
    for i in range(months):
        out += monthly_mb - int(cin[i+2])
    print(out)

    
if __name__ == "__main__":
    main()
