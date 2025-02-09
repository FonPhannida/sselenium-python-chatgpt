def get_des_cap():
    des_cap = {
        "platformName": "Android",
        "deviceName": "emulator-5556",  # From adb devices
        "platformVersion": "15",  # Android version
        "automationName": "UiAutomator2",  # Standard for Android
        "appPackage": "com.openai.chatgpt",  # Target app package
        "appActivity": ".MainActivity"#,  # Main activity
        #"noReset": False  # Do not keeps app data intact
    }
    return des_cap

# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
