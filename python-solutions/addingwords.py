var = dict()
while True:
    try:
        line = input()
    except:
        break
    line_list = line.split()
    if line_list[0] == "def":
        if line_list[1] in var:
            var[line_list[1]] = int(line_list[2])
        else:
            var.update({line_list[1] : line_list[2]})
    elif line_list[0] == "calc":
        eval_string = ""
        possible = True
        for i in range(1, len(line_list)-1):
            if i % 2 == 1:
                if line_list[i] in var:
                    eval_string += str(var[line_list[i]])
                else:
                    possible = False
                    break
            else:
                eval_string += line_list[i]
        if not possible:
            print(*line_list[1:], "unknown")
            continue
        else:
            found = False
            ans = eval(eval_string)
            for k, v in var.items():
                if int(v) == ans:
                    found = True
                    print(*line_list[1:], k)
                    break
            if not found:
                print(*line_list[1:], "unknown")
    else:
        var = dict()
