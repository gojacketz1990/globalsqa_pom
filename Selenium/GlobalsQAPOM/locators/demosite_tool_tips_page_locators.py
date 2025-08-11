class DemoToolTipPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    st_stephens_img_locator = [("xpath", '//img[@alt="St. Stephen\'s Cathedral"]'),]
    tower_bridge_img_locator = [("xpath", "//img[@alt='Tower Bridge']")]
    london_link_locator = [("xpath", "//a[normalize-space()='London, England']")]
    cc_link_locator = [("link_text", "CC BY-SA 3.0")]
    tooltip_element_locator = [("xpath", "//div[@role='tooltip']")]
