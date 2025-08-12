class DemoToolBarPageLocators():
    demo_iframe = [
        ("xpath", "//iframe[@src='../../demoSite/practice/controlgroup/splitbutton.html']"),
        ("class_name", "demo-frame"), # Keep this as a fallback if you like
    ]

    toolbar_demo_iframe =  [
        ("xpath", "//div[@rel-title='Toolbar']/p/iframe")
    ]

    splitbutton_demo_iframe =  [
        ("xpath", "//div[@rel-title='SplitButton']/p/iframe")
    ]


    click_tool_bar_locator = [
        ("id","Toolbar"),
        ("xpath", "//li[normalize-space()='Toolbar']")
    ]

    click_split_button_tab_locator = [
        ("id","SplitButton"),
        ("xpath", "//li[normalize-space()='SplitButton']")
    ]

    font_size_combobox_locator = [
        ("id","fontsize-button"),
    ]

    # New locator for the font size options
    font_size_options_locator = [
        ("xpath", "//ul[@id='fontsize-menu']//div[text()='{}']")
    ]
    # New dynamic locator for the nested <font> tag
    font_tag_locator = [
        ("xpath", ".//font[@size='{}']")
    ]
    document_locator = [
        ("id","page")
    ]

    run_last_option_button_locator = [
        ("xpath","//button[normalize-space()='Run last option']")
    ]

    drop_down_button_locator = [
        ("css","#ui-id-1-button")
    ]

    # New: Dynamic locator for the options within the "Open/Save/Delete" dropdown
    # The {} will be replaced by the option text (e.g., "Open...", "Save", "Delete")
    action_dropdown_option_locator = [
        ("xpath", "//ul[@id='ui-id-1-menu']//div[text()='{}']")
    ]

    output_list_items_locator = [
        ("xpath", "//ul[@class='output']/li"),
        ("css", "ul.output li")
    ]
