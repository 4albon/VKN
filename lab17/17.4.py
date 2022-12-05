import pandas as pd

way = int(input("Введіть маршрут: "))

with open("trains.csv", "r") as f:
    data = pd.read_csv(f, sep=";", encoding="cp1251")

    heads = data.columns.to_list()
    Follow_The_Damn_Train_CJ = []

    for i in heads:
        train = data[i].to_list()
        if way in train:
            Follow_The_Damn_Train_CJ.append(i)

    if len(Follow_The_Damn_Train_CJ) == 0:
        Follow_The_Damn_Train_CJ.append("Маршрутов не было найдено")

    new_data = pd.DataFrame(Follow_The_Damn_Train_CJ, columns=[way])

new_data.to_csv("search.csv", index=False)