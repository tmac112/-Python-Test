import sys
import requests
from bs4 import BeautifulSoup


def search_baidu(query):
    url = f"http://www.baidu.com/s?wd={query}"
    # 请求数据
    useragent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "Cookie": "BIDUPSID84EA42C0769096CF311D475FBE90FAA; PSTM=1594978855; __yjs_duid=1_b4a6d628aed0ed3cbc266bea40508ee21619416368551; BD_UPN=12314753; BDUSS=dqandNMW5Fa0M4Z2t0c3VpZkpNWTBPODBkWEN1dVY1eGF0eEtsVEpkbGlVVlppRVFBQUFBJCQAAAAAAAAAAAEAAACeDZM53~Pf87i03~Pf8-zhvaMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGLELmJixC5iTD; BDUSS_BFESS=dqandNMW5Fa0M4Z2t0c3VpZkpNWTBPODBkWEN1dVY1eGF0eEtsVEpkbGlVVlppRVFBQUFBJCQAAAAAAAAAAAEAAACeDZM53~Pf87i03~Pf8-zhvaMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGLELmJixC5iTD; H_WISE_SIDS_BFESS=110085_127969_128699_164870_171235_175756_176677_177407_178005_178328_178530_178622_179113_179345_179379_179450_180276_180408_180655_180701_180870_181106_181216_181398_181429_181433_181585_181631_181649_181664_181675_181712_181846_181942_182000_182024_182100_182179_182189_182233_182272_182321_182331_182382_182428_182529_182576_182594_182860_183002_183035_183123_183236_183330_183433_183548_183573_183713_183764_183870_184010_184240_184246_8000057_8000105_8000109_8000128_8000137_8000164_8000165_8000172_8000178_8000176_8000186_8000188; BAIDUID=AE8417FE1462D4084C7680501DAD9CAD:SL=0:NR=10:FG=1; MCITY=-288:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_ZTkwMmYyNjJhZjVmNTdmZDJiZjA3YzUxNjcwNDE4MDc3OWY2MzI3YjExOWY5MjYwOWJkY2Q0NmFiZGNjNjBiZmY5OTk3YThlYWYxNTNkNWMzNzZmYjUxNjdjOTZmZGZkNzY1Mzg0YjAwNWMwMjViMmMxZTkxMGZlZmZmOGM1NGQ2MDE1MWYzNDNkZWU5NzcyMTJiYzAyMjVmZWQ5OTk5Yg==; BAIDUID_BFESS=AE8417FE1462D4084C7680501DAD9CAD:SL=0:NR=10:FG=1; BA_HECTOR=0ga5ag0504242gal0g842m0p1hn40mr1f; ZFY=u8ds9OWPqXSAQ8iqfWxWtm0te:Bq2CAACXlm7ypUKA7Y:C; H_PS_645EC=d86c+YD89oCwt5CNX70dOFiYtichYxhyAuOcWzDorc1SaavfdRFuzLtr3CZy0JU4cKdN; BD_HOME=1; H_PS_PSSID=37781_36556_37555_37515_37687_37490_37729_36807_37535_37675_37743_26350_37478; sug=3; sugstore=0; ORIGIN=0; bdime=0"}
    # 发送请求并接受响应
    resp = requests.get(url, headers=useragent)
    # 解析响应数据
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, 'html.parser')
    results = soup.findAll("h3", {"class": {"c-title t t tts-title"}})
    if results:
        for tag in results:
            print("标题:", tag.find("a").get_text())
            print("超链接:", tag.find("a").attrs['href'])
        print('')
    else:
        print("No results found.")
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        search_baidu(query)
    else:
        print("Please provide a search query.")
