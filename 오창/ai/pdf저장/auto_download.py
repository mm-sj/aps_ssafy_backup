import os, requests, time

headers = {
    "Cookie": "2.1.k5$i1761704287$u229411614; _gcl_au=1.1.487771634.1761704288; _fwb=38sw1pYP2Eua0rNM3HXvDY.1761704288141; _ga=GA1.1.790398618.1761704288; _fbp=fb.1.1761704288537.851814351490534646; dable_uid=53043309.1761704288712; _gcl_aw=GCL.1761712506.EAIaIQobChMI1t3I95fIkAMVvEzCBR0wPQqwEAEYASAAEgI3QPD_BwE; _ga_HPYZ9Z9XP7=GS2.1.s1761712505$o2$g1$t1761712513$j52$l0$h2048132116; JSESSIONID_HAKSAF=1I8zfORKbzGXPwxf4yK943qr3G1LEtyNgIE2XIwHjI2_RdYkdjRV!-2096080651!1456852319!1761800414282"
}   
save_dir = r"C:\Users\SSAFY\Desktop\오창\ai\pdf저장\images"
os.makedirs(save_dir, exist_ok=True)

with open(r"C:\Users\SSAFY\Desktop\오창\ai\pdf저장\urls.txt", "r", encoding="utf-8") as f:
    urls = [u.strip() for u in f if u.strip()]

for i, url in enumerate(urls, start=1):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200 and res.headers.get("Content-Type", "").startswith("image"):
            path = os.path.join(save_dir, f"page_{i:03d}.jpg")
            with open(path, "wb") as out:
                out.write(res.content)
            print(f"{i} 저장 완료 ✅")
        else:
            print(f"{i} 실패 ❌ {res.status_code} ({res.headers.get('Content-Type')})")
        time.sleep(0.2)
    except Exception as e:
        print(f"{i} 에러: {e}")
