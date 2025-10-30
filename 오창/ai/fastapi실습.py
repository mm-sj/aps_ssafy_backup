from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/lunch")
def get_lunch():

    # 이곳에 코드를 넣습니다.

    return {"lunch": "Big-mac"}