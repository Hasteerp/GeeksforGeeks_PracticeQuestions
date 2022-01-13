List = [12, 35, 9, 56, 24]

output = []
for i in range(1, len(List)+1):
    output.append(List[-i])

print(output)

newList = [23, 65, 19, 90]


def swap(Listed, pos1, pos2):
    startpos = pos1-1
    endpos = pos2-1
    temp = 0

    temp = Listed[startpos]
    Listed[startpos] = Listed[endpos]
    Listed[endpos] = temp
    return Listed


answer = swap([1, 2, 3, 4, 5], 2, 5)
print(answer)


def find_length(List):
    count = 0
    for i in List:
        count = count + 1
    return count


anslist = find_length(answer)
print(anslist)

pov = [
    [1, 2, 3, 4],
    [4, 2, 7, 6],
    [3, 5, 1, 9],
    [2, 4, 6, 8]
]

k = 3


def fixing(pov_answer, number):
    newed = [row[:] for row in pov_answer]
    for index in range(len(pov_answer)):
        newed[index].sort()
        chn_number = newed[index][number - 1]
        pov_answer[index][index] = chn_number
        for value in range(len(pov_answer[index])):
            print(pov_answer[index][value], end=" ")
        print()


fixing(pov, k)












