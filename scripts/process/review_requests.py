import requests
from bs4 import BeautifulSoup
import os

save_dir = os.path.abspath(os.path.join(os.getcwd(), "../../data/clean"))

# n = 0

# 发送 GET 请求获取网页内容
urls = ["https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt0120737/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt0167261/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt10648342/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt9419884/reviews?ref_=tt_urv"]

file_count = 0

for url in urls:
    response = requests.get(url)

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到所有具有 class="text showmore__control" 的 div 元素
    reviews = soup.find_all("div", class_="text show-more__control"
                            or "text show-more__control clickable"
                            or "text show-more__control custom-cursor-on-hover")

    # 遍历每个评论，将其保存为独立的txt文件
    for review in reviews:
        file_count += 1
        file_path = os.path.join(save_dir, f"review_{file_count}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(review.text.strip())

print(f'reviews sauvegardés dans le dossier "data/clean"')


