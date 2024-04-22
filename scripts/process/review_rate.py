import requests
from bs4 import BeautifulSoup
import os
import json

save_dir = os.path.abspath(os.path.join(os.getcwd(), "../../data/raw"))
all_dicos = []  # 用于存储所有dico的列表

urls = [
    "https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt0120737/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt0167261/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt10648342/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt9419884/reviews?ref_=tt_urv"
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有影评和评分
    reviews_with_ratings = soup.find_all("div", class_="lister-item-content")


    for review_with_rating in reviews_with_ratings:
        dico = {}  # 用于存储单个影评页面的dico
        # 提取影评内容
        review_text = review_with_rating.find("div", class_="text show-more__control"
                                                       or "text show-more__control clickable"
                                                       or "text show-more__control custom-cursor-on-hover")
        review = review_text.text
        # 提取评分信息
        rating_tag = review_with_rating.find("span", class_="rating-other-user-rating")
        if rating_tag:
            rating = rating_tag.find("span").text  # 假设每个评分标签下只有一个<span>包含数字
            dico[review] = rating

            all_dicos.append(dico)  # 将当前页面的dico添加到总列表中

# print(all_dicos)

# 目标文件路径
file_path = os.path.join(save_dir, "reviews_with_ratings.json")

# 写入JSON文件
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(all_dicos, file, indent=4, ensure_ascii=False)
