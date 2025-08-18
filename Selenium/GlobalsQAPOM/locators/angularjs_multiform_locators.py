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

    success_header_locator = [
        ("xpath", "//h3[normalize-space()='Thanks For Your Money!']"),
    ]

    json_data_locator = [("xpath", "//pre[@class='ng-binding']")]


    console_radio_buttons = [("css", "input[type='radio'][value='{}']")]


    submit_payment_button = [
        ("css","button[type='submit']")
    ]
