import asyncio
import requests
from requests.auth import HTTPDigestAuth

from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False 하면 브라우저 보임
        page = await browser.new_page()
        await page.goto("https://example.com")
        title = await page.title()
        print(f"Page title: {title}")

    url = "https://httpbin.org/digest-auth/auth/user/passwd"
    response = requests.get(url, auth=HTTPDigestAuth('user', 'passwd'))

    if response.status_code == 200:
        print("인증 성공!")
        print(response.json())
    else:
        print(f"인증 실패: {response.status_code}")


        await browser.close()

# 실행
asyncio.run(run())
