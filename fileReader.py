from bs4 import BeautifulSoup


def HtmlReader():
    """
    Note: Parses the bookmark html file using BeautifulSoup to get the url of bookmarked websites
    Input: None
    Output: ans(List of bookmarked URLs)
    """
    with open("bookmarks_9_9_22.html", 'r', encoding='utf-8') as f:
        cont = f.read()
        ans = list()
        soup = BeautifulSoup(cont, 'html.parser')
        # print(soup.title)
        strHtml = soup.prettify()
        # print(strHtml)
        htmlLis = strHtml.split(" ")
        for i in range(len(htmlLis)):
            if "href=" in htmlLis[i]:
                val = htmlLis[i]
                ans.append(val[6:len(val) - 1])
        return ans


