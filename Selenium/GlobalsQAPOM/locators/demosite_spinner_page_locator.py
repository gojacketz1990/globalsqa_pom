class DemoSpinnerPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]
    #
    simple_spinner_iframe_locator   =  [
        ("xpath", "//div[@rel-title='Simple Spinner']//iframe")
    ]
    #
    # simple_spinner_iframe_locator   =  [
    #     ("xpath", "//div[@rel-title='Simple Spinner']//iframe")
    # ]

    click_currency_tab_locator = [
        ("id","Portlets"),
        ("xpath", "//li[normalize-space()='Currency']")
    ]

    click_simple_spinner_tab_locator = [
        ("id","Multiple Lists"),
        ("xpath", "//li[normalize-space()='Simple Spinner']")
    ]

    amount_spinner_locator = [
        ("id","spinner"),
        ("name","spinner"),
        ("class_name","ui-spinner-input"),
    ]

    up_amount_locator = [
        ("class_name","ui-spinner-up"),
        ("css","a.ui-spinner-up")
    ]


    down_amount_locator = [
        ("class_name","ui-spinner-down"),
        ("css","a.ui-spinner-down")
    ]

    currency_dropdown_locator = [
        ("css","#currency"),
        ("name","currency")
    ]

    toggle_button_locator = [
        ("id","disable"),
    ]

    toggle_widget_button_locator = [
        ("id","destroy"),
    ]

    get_value_button_locator = [
        ("id","getvalue"),
    ]

    set_value_to_5_button_locator = [
        ("id","setvalue"),
    ]

    # NEW LOCATOR: For the main spinner container when it's disabled
    spinner_container_disabled_locator = [("css", "span.ui-spinner-disabled")]

    # NEW LOCATOR: For the spinner input when it's disabled
    spinner_input_disabled_locator = [("css", "input#spinner[disabled]")]

    # NEW LOCATOR: For the spinner buttons when they are disabled
    spinner_button_disabled_locator = [("css", "a.ui-button-disabled")]


