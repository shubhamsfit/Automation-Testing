from utils.browser import get_driver

def test_homepage_title():
    driver = get_driver()
    driver.get("https://example.com")
    assert "Test" in driver.title
    driver.quit()
