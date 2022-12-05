import csv

f = open("data.csv", "r")
data = list(csv.reader(f))
f.close()

sum = 0
ser = 0
avg = []

for i in range(len(data[0])):
    sum += float(data[1][i])

ser = round(sum / len(data[1]), 3)

for i in range(len(data[0])):
    if float (data[1][i]) < ser:
        avg.append(data[0][i])

print(f"Сумма осадков за месяц- {sum}, среднее количество осадков - {ser}")
print(f"Числа месяца, в которых было больше всего осадков чем в среднем в месяц - {','.join(avg)}")