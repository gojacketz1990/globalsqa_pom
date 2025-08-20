class AngularJSSearchFilterPageLocators():
    a_input_locator =  [
        ("xpath", "//input[@ng-model='a']")
    ]
    b_input_locator =  [
        ("xpath", "//input[@ng-model='b']")
    ]
    a_plus_1_locator  =  [
        ("xpath", "//button[@ng-click='inca()']")
    ]
    a_minus_1_locator  =  [
        ("xpath", "//button[@ng-click='deca()']")
    ]
    b_plus_1_locator  =  [
        ("xpath", "//button[@ng-click='incb()']")
    ]
    b_minus_1_locator  =  [
        ("xpath", "//button[@ng-click='decb()']")
    ]
    operation_dropdown = [
        ("xpath","//select[@ng-model='operation']")
    ]

    calculation_result = [
        ("xpath", "//b[@class='result ng-binding']")
    ]
