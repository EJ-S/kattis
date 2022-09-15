def gcd(a, b):
    a, b = max(a,b), min(a,b)
    while b != 0:
        a, b = b, a%b
    return a


def simplify(frac):
    div = gcd(frac[0], frac[1])
    frac[0] = frac[0]//div
    frac[1] = frac[1]//div
    return frac



n = int(input())
for _ in range(n):
    num1, den1, op, num2, den2 = input().split()
    if op == "+":
        add_f = [((int(num1)*int(den2)) + (int(num2)*int(den1))), (int(den2)*int(den1))]
        ans = simplify(add_f)
        
    elif op == "-":
        sub_f = [((int(num1)*int(den2)) - (int(num2)*int(den1))), (int(den2)*int(den1))]
        ans = simplify(sub_f)
    elif op == "*":
        mult_f = [int(num1)*int(num2), int(den1)*int(den2)]
        ans = simplify(mult_f)
    else:
        div_f = [int(num1)*int(den2), int(den1)*int(num2)]
        ans = simplify(div_f)
    if ans[0] < 0 and ans[1] < 0:
        ans[0] *= -1
        ans[1] *= -1
    elif ans[1] < 0:
        ans[0] *= -1
        ans[1] *= -1 
    print(ans[0],"/",ans[1])
