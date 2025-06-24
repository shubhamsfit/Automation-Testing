from pages.load_page import LoadPage

def test_load_check(driver):
    load_page = LoadPage(driver)
    load_page.load()
    assert "Project-Website-One" in driver.current_url, "❌ URL is incorrect."
    print("✅ URL verified successfully.")       