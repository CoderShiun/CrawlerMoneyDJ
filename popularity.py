import requests
from bs4 import BeautifulSoup
url = "https://www.moneydj.com/InfoSvc/apis/vc"
payload = '{"counts":[{"svc":"NV","guid":"601865e2-637c-4535-b20a-5616dbb0af06"}]}'
head = {"Content-Type":"application/json"}
res = requests.post(url,data=payload, headers=head)
#soup = BeautifulSoup(res.text, "html.parser")
#popularity = soup.select(".float_right")

print()
print("The popularity of this article is %s"%res.text[20:23])
#print("-----------------")
#print(soup)
#print(popularity)