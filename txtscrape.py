import re

fp = open('scrape.txt')
for line in fp:
    x = re.findall(".*?([a-zA-Z]+\s[0-9][0-9],\s[0-9][0-9][0-9][0-9]).*",line)
    if len(x) !=0:
        outfile = open("./scraped.txt","a")
        outfile.write(str(x))
        print(x)
    