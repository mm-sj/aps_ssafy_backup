import re

# cURL로 복사한 원본 파일 (curl_list.txt)
with open("curl_list.txt", "r", encoding="utf-8") as f:
    data = f.read()

# 정규식으로 page-images 안의 jpg 링크만 추출
pattern = r'https://edu\.ssafy\.com/[^\s"\']*?/assets/page-images/[^\s"\']+\.jpg'
urls = re.findall(pattern, data)

# 중복 제거 + 정렬
unique_urls = sorted(set(urls))

# urls.txt 파일로 저장
with open("urls.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(unique_urls))

print(f"✅ {len(unique_urls)}개의 이미지 URL 추출 완료 → urls.txt 생성됨")
