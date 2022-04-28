# selenium

- Selenium是一个用于Web应用程序测试的工具
- Selenium测试直接运行在浏览器中，模拟用户真实操作浏览器
- 支持各种driver（FirfoxDriver,IternetExplorerDriver,ChromeDriver等）驱动
- selenium支持无界面浏览器操作

## 为什么使用selenium？

**模拟浏览器功能，自动执行网页中的js代码，实现动态加载**

## 安装selenium

- ChromeDriver（http://chromedriver.storage.googleapis.com/index.html）
- pip install selenium

## selenium使用步骤

```python
from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get("https://www.baidu.com/")

# 通过id定位元素
button = browser.find_element_by_id("su")
print(button)

# 通过name定位元素
name = browser.find_elements_by_name("wd")
print(name)

# 通过xpath语发定位元素
img_xpath =  browser.find_elements_by_xpath("//div[@id='wrapper']//input")
print(img_xpath)

# 通过标签名定位元素
tag_name = browser.find_elements_by_tag_name('input')
print(tag_name)

# 通过css属性定位元素
css_selector = browser.find_elements_by_css_selector('#kw')
print(css_selector)

# 通过超链接文本定位
link_text = browser.find_element_by_link_text('贴吧')
print(link_text)

# 获取元素文本
print(link_text.text)

# 获取元素属性
print(link_text.get_attribute('class'))

# 获取标签名
print(link_text.tag_name)
# 关闭浏览器
browser.quit()
```

## Phantomjs

- 无界面浏览器
- 支持页面元素查找，js代码运行
- 由于不进行css和gui渲染，运行效率高

```python
from selenium import webdriver

browser = webdriver.PhantomJS('phantomjs.exe')
browser.get('https://www.baidu.com/')
# 保存屏幕快照
browser.save_screenshot('baidu.png')
browser.find_element_by_id('kw').send_keys('刘德华')
browser.find_element_by_id('su').click()
browser.save_screenshot('刘德华.png')
browser.quit()
```

## Chrome handless

- chrome-headless模式

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.binary_location = path
    return webdriver.Chrome(chrome_options=chrome_options)

browser = share_browser()
browser.get('https://www.baidu.com/')
```

