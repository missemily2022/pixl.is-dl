from bs4 import BeautifulSoup
import cloudscraper

# Accepting Pixl.is URL from User
url = input("Enter your Pixl.is URL : ")

def pixl(url):
    count = 1
    dl_msg = ""
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"

    soup = BeautifulSoup(resp.content, "html.parser")
    thmbnailanch = soup.findAll(attrs={"class": "--media"})
    for ref in thmbnailanch:
        imgdata = client.get(ref.attrs["href"])
        imghtml = BeautifulSoup(imgdata.text, "html.parser")
        downloadanch = imghtml.find(attrs={"class": "btn-download"})
        currentimg = downloadanch.attrs["href"]
        currentimg = currentimg.replace(" ", "%20")
        dl_msg += f"{count}. {currentimg}\n"
        count += 1

    fld_msg = f"Your provided Pixl.is link is of Folder and I've Found {count - 1} files in the folder.\n"
    fld_link = f"\nFolder Link: {url}\n"
    final_msg = fld_link + "\n" + fld_msg + "\n" + dl_msg
    return final_msg

print(pixl(url=url))