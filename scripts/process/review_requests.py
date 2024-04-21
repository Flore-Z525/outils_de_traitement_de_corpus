import requests
from bs4 import BeautifulSoup

# 发送 GET 请求获取网页内容
url = "https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv"
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(response.content, "html.parser")

# 找到所有具有 class="text showmore__control" 的 div 元素
reviews = soup.find_all("div", class_="text show-more__control"
                        or "text show-more__control clickable"
                        or "text show-more__control custom-cursor-on-hover")

# 打印提取到的内容
for review in reviews:
    print(review.text.strip(), "\n*****\n")
