class AngularJSConsumptionCalculatorPageLocators():


    coffee_input = [
        ("xpath", "//label[text()='cups of coffee']/preceding-sibling::input")
    ]

    cigarettes_input = [
        ("xpath", "//label[text()='cigarettes']/preceding-sibling::input")
     ]

    caffeine_total = [
        ("xpath", "//form[.//label[b[text()='mg of caffeine.']]]//input[@name='total']")
    ]

    tar_total = [
        ("xpath", "//form[.//label[b[text()='mg of tar.']]]//input[@name='total']")
    ]

    caffeine_limit_warning = [
        ("xpath", "//form[.//label[text()='cups of coffee']]//p[@ng-show='isMaximumExceeded()']")
    ]

    tar_limit_warning = [
        ("xpath", "//form[.//label[text()='cigarettes']]//p[@ng-show='isMaximumExceeded()']")
    ]
