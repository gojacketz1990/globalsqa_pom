class AngularJSBankingProjectPageLocators():
    home_button_locator = [
        ("css",".btn.home")
    ]
    customer_login_locator = [
        ("css","button[ng-click='customer()']")
    ]
    bank_manager_login_locator = [
        ("css","button[ng-click='manager()']")
    ]
    customer_name_dropdown_locator = [
        ("name","userSelect")
    ]

    login_button_locator = [
        ("css","button[type='submit']")
    ]

    welcome_name_locator = [("xpath", "//span[@class='fontBig ng-binding']")]

    account_number_locator = [("xpath", "//div[@class='center']/strong[1]")]
    balance_locator = [("xpath", "//div[@class='center']/strong[2]")]
    currency_locator = [("xpath", "//div[@class='center']/strong[3]")]

    transactions_button_locator = [("xpath", "//button[@ng-click='transactions()']]")]
    deposit_button_locator = [("xpath", "//button[@ng-click='deposit()']")]
    withdrawal_button_locator = [("xpath", "//button[@ng-click='withdrawl()']")]

    deposit_amount_locator = [
        ("css","input[placeholder='amount']")
    ]
    withdrawal_amount_locator = [
        ("css","input[placeholder='amount']")
    ]
    make_deposit_button_locator = [
        ("css","button[type='submit']")
    ]
    make_withdrawal_button_locator = [
        ("xpath","//button[normalize-space()='Withdraw']")
    ]

    withdraw_message_locator = [
        ("xpath", "//span[@ng-show='message']")
    ]

    #Manager Items

    add_customer_button_locator = [
        ("css","button[ng-click='addCust()']")
    ]

    add_customer_first_name_locator = [
        ("css","input[ng-model='fName']")
    ]

    add_customer_last_name_locator = [
        ("css","input[ng-model='lName']")
    ]

    add_customer_post_code_locator = [
        ("css","input[ng-model='postCd']")
    ]

    add_customer_submit_locator = [
        ("xpath","//button[@type='submit']")
    ]


    open_account_button_locator = [
        ("css","button[ng-click='openAccount()']")
    ]

    open_account_customer_dropdown_locator = [
        ("id","userSelect")
    ]

    process_new_account_button = [
        ("xpath","//button[@type='submit']")
    ]

    currency_dropdown_locator = [
        ("id","currency")
    ]

    customers_button_locator = [
        ("css","button[ng-click='showCust()']")
    ]

    customer_row = [("xpath", "//tr[td[text()='{0}'] and td[text()='{1}']]")]

    customer_and_account = [("xpath", "//tr[td[text()='{0}'] and td[text()='{1}'] and td/span]")]


    # Add this new locator for the account number spans
    account_number_spans = [("tag_name", "span")]
