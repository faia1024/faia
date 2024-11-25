from bs4 import BeautifulSoup
import time
import requests

proxies={'http':'http://127.0.0.1:7890'}
url = input('输入分享链接')
headers_img = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'cache-control': "max-age=0",
  'sec-ch-ua': "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Windows\"",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://accounts.pixiv.net/",
  'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  'priority': "u=0, i",
  'Cookie': "first_visit_datetime_pc=2024-10-14%2013%3A08%3A52; p_ab_id=4; p_ab_id_2=8; p_ab_d_id=30875270; yuid_b=GFOIYQM; __cf_bm=QifwYbeDfr_aGQUJxAnKn2XYn.u6ZkH5Pl5k2xMxGOM-1728878932-1.0.1.1-Xrm5ndWY_fmJSseb9vei_XNUFknMIz3Gkas7lp_8JWYbSU9cAp..Lg6lkg8o.HF1lGTUq_GuHOU3qRcfYBkgWORIHTCDBByvrXpAdnLRmgo; cf_clearance=xaVhPBoAAmbh0V7bz9SlT_4WIKTbaLAGlHG.J346pNg-1728878938-1.2.1.1-Nr1UcS1o5zf2iBFLKJaxQTJWN2tKZUOJ8p0Mk.uZx0jzwZsGuxEvT2e.aW1WO7yE4qQodAuV4_u0497bsiDfi1SxUtIjvSk3cvGWrOOaEmmBBQ1Kmy4Vaw0RExd_k.hh600K9u2WXQ81z.WfuL_ovx5AkHIL_3u7eTYvHYxNITy5og9JGEf1ZshOvoUxqY9zJYOJi6wJiKbhn_PIqkvHEKrv7xOPW.w_8b7YVrd7.QxfZndoXrBewuFy0_u.PRK9dCTd5_FFyuAvTR4EsovTzMNwu_l1ll9ODpvZ6jKbCccJjdKY3VOX9BHDSXZxBMBOG9WSpbmDFTHjDppMi7moszAauow.dYD.pOW35vrNsrOZWKm16yk4Rlp0vyD_U4RMUzgrP9_nySvtYWebSWTmLg; _gid=GA1.2.1083211267.1728878958; device_token=971a9652d659362ce2058377e63aabad; privacy_policy_notification=0; a_type=0; _im_vid=01JA4KFZPFQT44H4K13FP9DDAD; cc1=2024-10-14%2013%3A14%3A56; PHPSESSID=99953315_YkFj1CrbjMDKI5Qi4E0r3lUFjcoPjOl4; c_type=19; privacy_policy_agreement=0; b_type=1; _ga_MZ1NL4PHH0=GS1.1.1728878960.1.1.1728879328.0.0.0; _ga=GA1.2.1632289979.1728878932; _ga_75BBYNYN9J=GS1.1.1728878932.1.1.1728879359.0.0.0"
}


headers = {
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": (
        "first_visit_datetime_pc=2024-10-14%2013%3A08%3A52; "
        "p_ab_id=4; "
        "p_ab_id_2=8; "
        "p_ab_d_id=30875270; "
        "yuid_b=GFOIYQM; "
        "privacy_policy_notification=0; "
        "a_type=0; "
        "_im_vid=01JA4KFZPFQT44H4K13FP9DDAD; "
        "c_type=19; "
        "privacy_policy_agreement=0; "
        "b_type=1; "
        "_ga_MZ1NL4PHH0=GS1.1.1728878960.1.1.1728879328.0.0.0; "
        "PHPSESSID=kk2c58rcmrl1b56vtlsp7bbho8ebi63t; "
        "cc1=2024-11-25%2017%3A45%3A01; "
        "__cf_bm=WF65PQH6EJ2O_yE_GMmtFBtxE3T2_twtXzOaNV0K5fQ-1732524301-1.0.1.1-WaA7Nzwwe09._axJ_wG.EqZznnIpXONv7rJBqyQoDhl9CrXREQ2uvYmNr6Jh.ByRPgfNvrd0kHgOkgkRkhYEOLfX25XFz3SDc8iN3TvlsNM; "
        "cf_clearance=FZcDdvLexcy6zswu..w4_v4WYH4B08aFvZihqVxmmjo-1732524304-1.2.1.1-CKublzX64yh.bO_BwgFmyIPhz5cpt8Zxp.EMjcwZ_1oyVVGtLykgqjrMq5zN5DJDg9ukM16lmQFGSSBQ6bMn5bgm70Jr5HRB28Mj6clVsich.voFZRcce60c_Lhptl9_CU0lTzqu0GhfnKmqHVFJCELa0UTOB.gs_zIiLIaLO4OYn73XpXYJa.TUL0mwVCHn.JKveloq9Zih6Y83sb6GS1ZJnfM4Km_CuIupAABk26.UCAm6C9Od5zzIEZp1daC2C65wXwm4e2zuR8wlwrK.WznEUuOUkhXaM.1OP478WPk_lwE_HKUuRB49aWSpxsx669Ya77seoFSz6K_UtSZgEqJHiyYanhFYDGtkk5AzvHCrEsGAN8fNAoefQM5yqQwiq.3nOCtt5RUdErrFLs50lw; "
        "_im_uid.3929=b.685512bbf9e10178; "
        "_ga=GA1.2.1632289979.1728878932; "
        "_gid=GA1.2.775953554.1732524317; "
        "_ga_75BBYNYN9J=GS1.1.1732524303.3.1.1732524319.0.0.0"
    ),
    "priority": "u=0, i"
}
response = requests.get(url,proxies=proxies,headers=headers)



def extract_image_urls(html_content):
    """
    从 HTML 内容中提取所有以 https://i.pximg.net 开头的图片 URL。

    参数:
        html_content (str): HTML 文档的内容。

    返回:
        list: 包含所有图片 URL 的列表。
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = []

    # 查找所有带有 img 标签或 link preload 相关的标签
    for tag in soup.find_all(['img', 'link', 'body']):
        # 检查 src 属性
        if tag.has_attr('src') and tag['src'].startswith('https://i.pximg.net'):
            image_urls.append(tag['src'])
        # 检查 href 属性
        if tag.has_attr('href') and tag['href'].startswith('https://i.pximg.net'):
            image_urls.append(tag['href'])
        # 检查 body 直接文本内容
        if tag.string and 'https://i.pximg.net' in tag.string:
            text_links = tag.string.split()
            for link in text_links:
                if link.startswith('https://i.pximg.net'):
                    image_urls.append(link)

    return image_urls


image_urls = extract_image_urls(response.text)
for img_url in image_urls:
    a=0
    while True:
        img_url1 = img_url.replace('_p0_',f'_p{a}_')
        img = requests.get(img_url1,proxies=proxies,headers=headers_img)
        if img.status_code == 200:
            with open(f'img\\img{a}.jpg', 'wb') as f:
                f.write(img.content)
        else:
            print(f"结束")
            break
        print('正在爬取第'+str(a+1)+'张')
        a+=1
        time.sleep(0)
