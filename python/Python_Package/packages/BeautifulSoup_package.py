# import requests
# from bs4 import BeautifulSoup

# url = "https://www.tcs.com/sitemap.xml"
# response = requests.get(url)

# webpage = response.content
# # print(f"Error: {response.status_code}")

# soup = BeautifulSoup(webpage, 'html.parser')
# items = soup.find_all('article', class_='product_pod')

# for item in items:
#     print(item)






from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>surj</p><p>deepak</p>','html.parser')
# print(soup.p.text)
print(soup.find_all('p')[1].text)