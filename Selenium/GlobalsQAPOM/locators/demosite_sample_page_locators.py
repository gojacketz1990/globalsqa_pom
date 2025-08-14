class DemoSamplePageLocators():

    name_text_locator =  [
        ("id", "g2599-name"),
        ("class_name","name")
    ]

    email_locator =  [
        ("id", "g2599-email"),
        ("class_name","email")
    ]

    experience_select_locator =  [
        ("id", "g2599-experienceinyears"),
        ("name", "g2599-experienceinyears"),
    ]

    expertise_checkbox_parent_locator = [
        ("css",".grunion-checkbox-multiple-options")
    ]

    expertise_checkbox_locator = [
        ("css",".grunion-checkbox-multiple-options input[type='checkbox']")
    ]
    # This finds the input checkbox based on the text of its sibling <span>.
    expertise_checkbox_label_text_locator = [
        #("xpath", ".//label[.//span[text()='{}']]/input")
        ("xpath", "//label[.//span[text()='{}']]/preceding-sibling::input")
    ]
    education_radio_parent_locator = [
        ("css",".grunion-radio-options")
    ]
    education_radio_label_text_locator = [
        #("xpath", ".//label[.//span[text()='{}']]/input")
        ("xpath", "//label[.//span[text()='{}']]/preceding-sibling::input")
    ]
