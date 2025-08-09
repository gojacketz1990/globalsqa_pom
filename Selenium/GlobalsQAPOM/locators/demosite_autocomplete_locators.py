class DemoAutocompletePageLocators():

    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    categories_tab = [
        ("id","Categories"),
        ("xpath", "//li[normalize-space()='Categories']"),
    ]

    combobox_tab = [
        ("id","ComboBox"),
        ("xpath", "//li[normalize-space()='ComboBox']"),
    ]

    categories_demo_iframe =  [
        ("xpath", "//div[@rel-title='Categories']//iframe")
    ]

    combobox_demo_iframe =  [
        ("xpath", "//div[@rel-title='ComboBox']//iframe")
    ]

    search_box_locator = [
        ("id","search"),
    ]

    autocomplete_suggestions_locator = [
        ("css","ul#ui-id-1 li.ui-menu-item div.ui-menu-item-wrapper"),

    ]

    combobox_search_locator = [
        ("css","input.custom-combobox-input"),
        ("xpath","//input[contains(@class, 'custom-combobox-input')]")
    ]

    combobox_autosuggestions_locator = [
        ("css",".ui-autocomplete li"),
        ("xpath","ui-autocomplete')]//li")
    ]
