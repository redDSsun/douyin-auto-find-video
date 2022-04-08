# douyin-auto-find-video

### 准备环境

* 安卓模拟器
1. 推荐使用雷电模拟器： https://www.ldmnq.com/， 下载最新版即可
2. 打开模拟器，安装抖音

* 安装jdk8
1. 请从后面提供的百度网盘里下载 jdk-8u211-windows-x64.exe， 并安装
2. 配置环境变量JAVA_HOME 为jdk安装目录

* 安装python
1. 下载并安装 https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe
2. 安装appium client `pip install appium-python-client`

* 安装appium
1. 下载并安装 https://github.com/appium/appium-desktop/releases/download/v1.22.2/Appium-Server-GUI-windows-1.22.2.exe

* 安装安卓sdk
1. 请从后面提供的百度网盘中下载 androidsdk.zip，并解压
2. 添加环境变量 ANDROID_HOME 为解压目录
3. 添加目录到环境变量 path

* 下载脚本
1. GitHub https://github.com/redDSsun/douyin-auto-find-video

* 百度网盘
1. https://pan.baidu.com/s/19C9fGmoXne8DgfXhrTB2TQ  密码： kgwb

### 启动
* 启动安卓模拟器

* 启动appium server
1. 如果模拟器多开，appium server也需要多开同样的数量， 并用命令行启动
  `appium -a 127.0.0.1 -p 4723 -bp 4733 -U ML5RRPCUWO`
  注意端口不要重复
  
* 配置脚本
  ```
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
    },
    // 如有多个模拟器，请添加相应配置， deviceName， automationName请不要重复
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
  search_worlds = ['北京', '上海']  //抖音搜索栏搜索的词，请根据需要修改
  feature_worlds = ['消费']。//根据提供的词匹配视频文案， 匹配的视频就会点击
  max_videos_num = 5。//每个词搜索完，往下滑多少条视频
  ```
  
  * 启动脚本
  `python ./main.py`
 
