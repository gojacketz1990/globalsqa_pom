class DemoDropDownPageLocators():

    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    country_dropdown_locator = [
        ("xpath", "//div[@rel-title='Select Country']//select")
    ]

    country_options_locator = [
        ("xpath", "//div[starts-with(@class,'single_tab_div')]//select/option")
    ]

    select_country_tab_locator = [
        ("id","Select Country"),
        ("xpath","//button[text()='Select Country'")
    ]
