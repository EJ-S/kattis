def fizz_buzz(num):
    output = []
    for i in range(1, num+1):
        out = ""
        if i % 3 == 0:
            out += "fizz"
        if i % 5 == 0:
            out += "buzz"
        if out == "":
            out = str(i)
        output.append(out) 
    return output

n, m = map(int, input().split())
correct = fizz_buzz(m)
most_correct = 0
loc_correct = 0
for _ in range(n):
    count = 0
    ans = input().split()
    for i, s in enumerate(ans):
        if correct[i] == s:
            count += 1
    if count > most_correct:
        most_correct = count
        loc_correct = _

print(loc_correct+1)
