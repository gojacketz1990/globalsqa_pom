class AngularJSRegistrationLoginPageLocators():
    username_locator = [
        ("id","username"),
        ("name","username")
    ]
    password_locator = [
        ("id","password"),
        ("name","password")
    ]

    login_button_locator = [
        ("css","button[type='submit']")
    ]

    register_link_locator = [
        ("link_text","Register")
    ]

    #Register Fields:

    register_first_name_locator = [
        ("id","firstName"),
        ("name","firstName")
    ]

    register_last_name_locator = [
        ("id","lastName"),
        ("name","lastName")
    ]
    register_username_locator = [
        ("id","username"),
        ("name","username")
    ]
    register_password_locator = [
        ("id","password"),
        ("name","password")
    ]
    register_button_locator = [
        ("css","button[type='submit']"),
        ("xpath", "//button[text()='Register']")
    ]
    cancel_link_locator = [
        ("link_text","Cancel")
    ]

    successful_registration_locator = [
        ("xpath", "//div[@class='ng-binding ng-scope alert alert-success']")
    ]

    invalid_login_locator = [
        ("xpath","//div[@class='ng-binding ng-scope alert alert-danger']")
    ]
