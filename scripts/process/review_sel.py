from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 打开 IMDb 电影评论页面
url = "https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv"
driver.get(url)

# 点击 "load more" 按钮，加载更多评论
load_more_button = driver.find_element(By.CLASS_NAME, "ipl-load-more__button")
load_more_button.click()

# 获取页面内容
page_source = driver.page_source

# 关闭浏览器
driver.quit()

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(page_source, "html.parser")

# 找到所有具有 class="text showmore__control" 的 div 元素
reviews = soup.find_all("div", class_="text showmore__control")

# 打印提取到的内容
for review in reviews:
    print(review.text.strip())
