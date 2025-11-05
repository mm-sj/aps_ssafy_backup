import os, requests, time

headers = {
    "Cookie": "JSESSIONID_HAKSAF=TZxG6_f7GGVqaZa7XHmp0-8MEp1RhukfmFcY9vUB8aes0JqVwsnl!-2096080651!1456852319!1762126460923"
}   
save_dir = r"C:\Users\SSAFY\Desktop\오창민\aps_ssafy_backup\오창\ai\pdf저장\pdf압축\images"
os.makedirs(save_dir, exist_ok=True)

with open(r"C:\Users\SSAFY\Desktop\오창민\aps_ssafy_backup\오창\ai\pdf저장\pdf압축\urls.txt", "r", encoding="utf-8") as f:
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
