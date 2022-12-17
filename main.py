from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

# print(html_bytes)
# print('*'*10)
# print(html)

title_index = html.find("<title>")  #the position of first found <title>
start_index = title_index + len("<title>")

end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)