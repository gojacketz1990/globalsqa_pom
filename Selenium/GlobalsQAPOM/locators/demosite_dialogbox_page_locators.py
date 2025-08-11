class DemoDialogBoxPageLocators():
    message_box_demo_iframe =  [
        ("xpath", "//div[@rel-title='Message Box']//iframe")
    ]

    form_demo_iframe =  [
        ("xpath", "//div[@rel-title='Form']//iframe")
    ]

    confirmation_box_demo_iframe =  [
        ("xpath", "//div[@rel-title='Confirmation Box']//iframe")
    ]
    form_tab = [
        ("id","Form"),
        ("xpath", "//li[normalize-space()='Form']"),
    ]

    messagebox_tab = [
        ("id","Message Box"),
        ("xpath", "//li[normalize-space()='Message Box']"),
    ]

    confirmationbox_tab = [
        ("id","Confirmation Box"),
        ("xpath", "//li[normalize-space()='Confirmation Box']")
    ]

    existing_users_table = [
        ("id", "users"),

    ]

    name_header_locators = [("xpath", "//th[text()='Name']")]
    email_header_locators = [("xpath", "//th[text()='Email']")]
    password_header_locators = [("xpath", "//th[text()='Password']")]

    _table_locator = [("id", "users")]
    _row_locator = [("xpath", "//table[@id='users']/tbody/tr")]
    _cell_locator = [("tag_name", "td")]

    new_user_button_locator = [
        ("id","create-user"),
    ]

    new_user_popup_locator = [
        ("xpath","//div[@role='dialog']"),
    ]

    name_text_field_locator = [
        ("name","name"),
        ("id","name"),
    ]
    email_text_field_locator = [
        ("name","email"),
        ("id","email"),
    ]

    password_text_field_locator = [
        ("name","password"),
        ("id","password"),
    ]

    create_account_button_locators = [
        ("xpath", "//button[text()='Create an account']")
    ]

    cancel_account_button_locators = [
        ("xpath", "//button[text()='Cancel']")
    ]

    download_complete_locator = [
        ("id", "dialog-message"),
    ]

    empty_recycle_bin_locator = [
        ("id", "dialog-message"),
    ]

    download_ok_button_locator = [
        ("xpath", "//button[text()='Ok']"),
    ]

    percentage_text_locator = [
        ("xpath", "//div[@id='dialog-message']/p[2]")
    ]

    confirmation_box_delete_all = [
        ("xpath", "//button[text()='Delete all items']"),
    ]

    confirmation_box_cancel = [
        ("xpath", "//button[text()='Cancel']"),
    ]
