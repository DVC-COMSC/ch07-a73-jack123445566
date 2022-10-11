number = list(map(int, input().split()))
print (number)

insnum = int(input())
for i in range(len(number)):
  if insnum <= number[i]:
    number.insert(i,insnum)
    break
else:
    number.append(insnum)
	