class DemoDatePickerPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]
    #
    simple_date_picker_tab_locator = [
        ("id","Simple Date Picker"),
        ("xpath", "//li[normalize-space()='Simple Date Picker']")
    ]

    dropdown_datepicker_tab_locator = [
        ("id","DropDown DatePicker"),
        ("xpath", "//li[normalize-space()='DropDown DatePicker']")
    ]

    icon_trigger_tab_locator = [
        ("id","Icon Trigger"),
        ("xpath", "//li[normalize-space()='Icon Trigger']")
    ]

    simple_date_picker_demo_iframe =  [
        ("xpath", "//div[@rel-title='Simple Date Picker']//iframe")
    ]

    dropdown_datepicker_demo_iframe =  [
        ("xpath", "//div[@rel-title='DropDown DatePicker']//iframe")
    ]

    icon_trigger_demo_iframe =  [
        ("xpath", "//div[@rel-title='Icon Trigger']//iframe")
    ]

    date_field_locator = [
        ("id","datepicker"),
        ("class_name","hasDatePicker")
    ]

    simple_date_picker_calendar = [
        ("id","ui-datepicker-div"),
    ]
    #date_input_field = [("id", "datepicker")]
    datepicker_header = [("class_name", "ui-datepicker-header")]
    datepicker_month = [("class_name", "ui-datepicker-month")]
    datepicker_year = [("class_name", "ui-datepicker-year")]
    datepicker_prev_button = [("xpath", "//a[@title='Prev']")]
    datepicker_next_button = [("xpath", "//a[@title='Next']")]
    datepicker_calendar_days = [("xpath", "//div[@id='ui-datepicker-div']//td")]

    # Dynamic locator to find a specific day based on its number
    datepicker_day_by_number = [("xpath", "//div[@id='ui-datepicker-div']//a[text()='{}']")]

    datepicker_month_dropdown = [("class_name", "ui-datepicker-month")]
    datepicker_year_dropdown = [("class_name", "ui-datepicker-year")]

    icon_calendar_locator = [
        ("class_name","ui-datepicker-trigger")
    ]
