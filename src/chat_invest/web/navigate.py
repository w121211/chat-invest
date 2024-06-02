from playwright.sync_api import sync_playwright

def run(playwright):
    # 啟動瀏覽器
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # 創建一個新頁面
    page = context.new_page()

    # 導航到一個網址
    page.goto("https://example.com")

    # 您的其他操作
    # ...

    # 保持瀏覽器開啟
    print("瀏覽器將保持開啟。按 Ctrl+C 結束。")
    input("按下 Enter 鍵結束程式並關閉瀏覽器...")

with sync_playwright() as playwright:
    run(playwright)
