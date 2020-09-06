from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#firm = 'apple-computer-inc'
firm = 'tesla-motors'

url = 'https://www.investing.com/equities/' + firm + '-news'

opts = Options()
opts.add_argument("--headless")
driver = Firefox(options=opts)
driver.get(url)

count = 0;
while True:
    count += 1;
    print(count)
    results = driver.find_elements_by_xpath("//div[contains(@class, 'mediumTitle1')]/article")
    for result in results:
        print(result.text)
    try:
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
        )
        link.click()
    except:
        break

driver.quit()
