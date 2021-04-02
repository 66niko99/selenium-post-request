from selenium import webdriver
import selenium_post

# usage example for posting a checkout request.
checkout_data = {'utf8': '✓',
                 'authenticity_token': '',
                 'g-recaptcha-response': ''}
  
driver = webdriver.Chrome()
driver.get("http://example.com")
selenium_post.post(driver=driver, path='/checkout', params=checkout_data)
