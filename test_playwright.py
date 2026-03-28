from playwright.sync_api import sync_playwright


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file://{__file__.replace('playwright_test.py','index.html')}")

        page.fill('#username', 'admin')
        page.fill('#password', '1234')
        page.click('text=Login')

        result = page.inner_text('#result')
        assert result == 'Login Successful'

        browser.close()


def test_login_failure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file://{__file__.replace('playwright_test.py','index.html')}")

        page.fill('#username', 'user')
        page.fill('#password', 'wrong')
        page.click('text=Login')

        result = page.inner_text('#result')
        assert result == 'Login Failed'

        browser.close()

