import urllib2
from pyquery import PyQuery as pq


def ensodl():
    try:
        response=urllib2.urlopen('http://www.ggweather.com', timeout=1)
        print([
                 float(v) for v in
                 [pq(td).text().strip()
                    for tr in pq(url='http://ggweather.com/enso/oni.htm')('table[width="805"]')('tr')[2:]
                        for td in pq(tr)('td')[4:]]
                    if len(v) > 0
        ])

        return True
    except urllib2.URLError, e:
        z = e
        print e
        return False

def ensowr():
    target = open("enso.json", 'w')
    target.write([
                 float(v) for v in
                 [pq(td).text().strip()
                    for tr in pq(url='http://ggweather.com/enso/oni.htm')('table[width="805"]')('tr')[2:]
                        for td in pq(tr)('td')[4:]]
                    if len(v) > 0
    ])
    target.close()

def main():
    testcon = testcon()
    print(testcon)

if __name__=="__main__":
    ensodl()
