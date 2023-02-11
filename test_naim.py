from appium import webdriver

desired_caps = {
    "appium:deviceName": "emulator-5554",
    "platformName": "android",
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main",
    "appium:noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.get('https://www.tiktok.com/profile/')
# el1 = driver.find_element(
#    by=AppiumBy.ID, value="com.android.chrome:id/negative_button")
# el1.click()
# el2 = driver.find_element(
#    by=AppiumBy.ID, value="com.android.chrome:id/search_box_text")
# el2.send_keys("tiktok")
# el3 = driver.find_element(
#    by=AppiumBy.ID, value="com.android.chrome:id/url_bar")
# el3.click()
# el4 = driver.find_element(
#    by=AppiumBy.ID, value="com.android.chrome:id/feed_stream_recycler_view")
# el4.click()
#actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(
#    driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location([object Object], undefined)
# actions.w3c_actions.pointer_action.pointer_down()
#actions.w3c_actions.pointer_action.move_to_location(undefined, undefined)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
#
#actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(
#    driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location([object Object], undefined)
# actions.w3c_actions.pointer_action.pointer_down()
#actions.w3c_actions.pointer_action.move_to_location(undefined, undefined)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
#
# el5 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.app.Dialog/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button[1]")
# el5.click()
# el6 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
# el6.send_keys("tiktok")
# el7 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.widget.EditText")
# el7.send_keys("tiktok")
# el7.click()
# el8 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout")
# el8.click()
# el9 = driver.find_element(
#    by=AppiumBy.ID, value="com.android.chrome:id/url_bar")
# el9.send_keys("tiktok")
# el10 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
# el10.click()
# el11 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
# el11.click()
# el12 = driver.find_element(
#    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout")
# el12.click()
#
