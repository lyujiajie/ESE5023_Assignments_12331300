
#probelm5 [1]
def make_50(self) -> list:
    str = list(self)
    spr = ['+', '-', '']
    sum_50 = []
    for a in spr:
        for b in spr:
            for c in spr:
                for d in spr:
                    for e in spr:
                        for f in spr:
                            for g in spr:
                                for h in spr:
                                    sum = str[0] + a + str[1] + b + str[2] + c + str[3] + d + str[4] + e + str[5] + f + str[6] + g + str[7] + h + str[8]
                                    if eval(sum) == 50:
                                        print(sum+"=50")
                                        sum_50.append(sum)
    return sum_50

if __name__ == "__main__":
    results = make_50("123456789")
    for result in results:
        assert eval(result) == 50
    print("OK")









#probelm5 [2]
def make_50(self,x) -> list:
    str = list(self)
    spr = ['+', '-', '']
    i=0
    for a in spr:
        for b in spr:
            for c in spr:
                for d in spr:
                    for e in spr:
                        for f in spr:
                            for g in spr:
                                for h in spr:
                                    sum = str[0] + a + str[1] + b + str[2] + c + str[3] + d + str[4] + e + str[5] + f + str[6] + g + str[7] + h + str[8]
                                    if eval(sum) == x:
                                        i=i+1
    return i

Total_solutions={}
for x in range(1,101):
    results = make_50("123456789",x)
    Total_solutions[x] = results
print(tinydict)
min_Total_solutions = min(zip(Total_solutions.values(), Total_solutions.keys()))
max_Total_solutions = max(zip(Total_solutions.values(), Total_solutions.keys()))
print(min_Total_solutions)
print(max_Total_solutions)