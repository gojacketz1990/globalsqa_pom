class AngularJSMultiformPageLocators():
    name_text_box_locator =  [
        ("name", "name")
    ]


    email_text_box_locator =  [
        ("name", "email")
    ]

    next_section_button_locator = [
        ("css", "a.btn-block.btn-info"),
        # Very robust: XPath targeting the link text
        ("xpath", "//a[normalize-space()='Next Section']"),
    ]

    question_text_locator = [
        ("xpath", "//label[contains(normalize-space(), 'Console of Choice')]"),
    ]

    json_data_locator = [("xpath", "//pre[@class='ng-binding']")]
