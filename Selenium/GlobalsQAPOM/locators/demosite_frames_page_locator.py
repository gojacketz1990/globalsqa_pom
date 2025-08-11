class DemoFramesPageLocators():

    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    click_here_button =  [
        ("xpath", "//div[contains(@class, 'resp-tab-content-active')]//a[text()='Click Here']"),

    ]

    iframe_tab_locator = [
        ("id","iFrame"),
        ("xpath", "//li[normalize-space()='iFrame']"),
    ]
    open_new_browser_tab_locator = [
        ("id","Open New Tab"),
        ("xpath", "//li[normalize-space()='Open New Tab']"),
    ]
    open_new_window_tab_locator = [
        ("id","Open New Window"),
        ("xpath", "//li[normalize-space()='Open New Window']"),

    ]

    globalsqa_iframe_locator = [
        ("class_name", "iframe"),
        ("css","iframe[name='globalSqa']")
    ]

    loadrunner_training_link_locator = [
        ("xpath","//a[.//img[@alt='LoadRunner Training']]")
    ]

    heading_in_iframe = [
        ("css","div[class='page_heading'] h1"),
    ]

