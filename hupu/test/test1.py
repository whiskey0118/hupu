from lxml import etree


haha='''<div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
     '''
# with open('nba.txt','rb') as f:
#     html = etree.HTML(f.read())
#     print(html)
parser = etree.HTMLParser(encoding="utf-8")

html = etree.parse('nba.txt',parser=parser)

# print(html.xpath('//*[@target="_blank"]/text()'))
print(html.xpath('/html/body/div[3]/div[4]/table/tbody/tr[3]/td[2]/b/a/text()'))


# for i in html_data:
#     print(i.text)


# with open("nba.html",'rb') as f:
#     print(f.read())
