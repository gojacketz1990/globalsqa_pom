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
