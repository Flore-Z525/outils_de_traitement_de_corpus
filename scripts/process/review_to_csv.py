import csv
import json

# 读取json文件
with open("../../data/raw/reviews_with_ratings.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 创建CSV文件并写入数据
with open("../../data/clean/reviews_with_ratings.csv", "w", newline="", encoding="utf-8") as csvfile:
    # 定义CSV文件的列名
    fieldnames = ["commentaire", "classe"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 写入negatif评论
    for dico in data:
        comment = list(dico.keys())[0]
        rating = int(list(dico.values())[0])

        if rating in [1, 2, 3, 4, 5]:
            writer.writerow({"commentaire": comment, "classe": "negatif"})

    # 写入positif评论
    for dico in data:
        comment = list(dico.keys())[0]
        rating = int(list(dico.values())[0])

        if rating in [6, 7, 8, 9, 10]:
            writer.writerow({"commentaire": comment, "classe": "positif"})
