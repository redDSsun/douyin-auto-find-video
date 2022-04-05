from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
import threading

envs = [
    {
        'platformName': 'Android', # 被测手机是安卓
        'platformVersion': '7', # 手机安卓版本
        'deviceName': 'test', # 设备名，安卓手机可以随意填写
        'appPackage': 'com.ss.android.ugc.aweme', # 启动APP Package名称
        'appActivity': '.main.MainActivity', # 启动Activity名称
        'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
        'resetKeyboard': True, # 执行完程序恢复原来输入法
        'noReset': True,       # 不要重置App
        'newCommandTimeout': 15000,
        'automationName' : 'UiAutomator2',
        'url': 'http://localhost:4723/wd/hub'
    }
]
search_worlds = ['北京', '上海']
feature_worlds = ['消费']
max_videos_num = 5


def prepare():
    drivers = []
    for env in envs:
        desired_caps = {
            'platformName': env.get('platformName'),
            'platformVersion': env.get('platformVersion'),
            'deviceName': env.get('deviceName'),
            'appPackage': env.get('appPackage'),
            'appActivity': env.get('appActivity'),
            'unicodeKeyboard': env.get('unicodeKeyboard'),
            'resetKeyboard': env.get('resetKeyboard'),
            'noReset': env.get('noReset'),
            'newCommandTimeout': env.get('newCommandTimeout'),
            'automationName': env.get('automationName')
        }
        driver = webdriver.Remote(env.get('url'), desired_caps)
        time.sleep(5)
        drivers.append(driver)
    return drivers

def find_match_feature_worlds(text):
    match_worlds = []
    for feature_world in feature_worlds:
        if feature_world in text:
            match_worlds.append(feature_world)
    return match_worlds


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

def swipe_up(driver):
    size = get_size(driver)
    driver.swipe(start_x=size[0]*0.8, start_y=size[1]*0.8, end_x=size[0]*0.8, end_y=size[0]*0.6, duration=1000)
    driver.swipe(start_x=size[0]*0.8, start_y=size[1]*0.8, end_x=size[0]*0.8, end_y=size[0]*0.8, duration=0)


def search(driver, world):
    found_videos = []

    search_input = driver.find_elements(By.CLASS_NAME, 'android.widget.EditText')[0]
    search_input.send_keys(world)
    print('搜索：'+world+', 搜索条件： '+','.join(feature_worlds))

    driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="搜索"]').click()
    time.sleep(2)

    video_button_code = 'new UiSelector().text("视频").className("android.widget.Button")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, video_button_code).click()
    time.sleep(2)

    while True:
        videos = driver.find_elements(By.ID, 'com.ss.android.ugc.aweme:id/lh_')
        for video in videos:
            try:
                text_element = video.find_element(By.ID, 'com.ss.android.ugc.aweme:id/desc')
            except:
                continue
            text = text_element.text
            if text not in found_videos:
                found_videos.append(text)
                if len(found_videos) > max_videos_num:
                    return
                print('搜索了' + str(len(found_videos)) + '条视频')
                match_worlds = find_match_feature_worlds(text_element.text)
                if len(match_worlds) > 0:
                    print('发现相关视频： '+text_element.text+', 符合搜索条件： '+','.join(match_worlds))
                    video.click()
                    time.sleep(5)
                    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
                    time.sleep(2)
        swipe_up(driver)
        time.sleep(2)


def run(driver):
    driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="搜索"]').click()
    time.sleep(2)
    while True:
        for world in search_worlds:
            search(driver, world)


def start(drivers):
    for index, driver in enumerate(drivers):
        threading.Thread(target=run, args=(driver,), name='thread'+str(index)).start()


if __name__ == '__main__':
    drivers = prepare()
    start(drivers)







