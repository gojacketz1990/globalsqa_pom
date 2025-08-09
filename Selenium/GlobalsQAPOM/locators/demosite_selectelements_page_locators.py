class DemoSelectElementsPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    multiple_selection_tab_locator = [
        ("id","Multiple Selection"),
        ("xpath", "//li[normalize-space()='Multiple Selection']")
    ]

    grid_selection_tab_locator = [
        ("id","Grid Selection"),
        ("xpath", "//li[normalize-space()='Grid Selection']")
    ]

    serialize_tab_locator = [
        ("id","Serialize"),
        ("xpath", "//li[normalize-space()='Serialize']")
    ]

    multiple_selection_iframe_locator = [
        ("xpath", "//div[@rel-title='Multiple Selection']//iframe")
    ]

    grid_selection_iframe_locator = [
        ("xpath", "//div[@rel-title='Grid Selection']//iframe")
    ]

    serialize_iframe_locator = [
        ("xpath", "//div[@rel-title='Serialize']//iframe")
    ]

    multiple_selection_items_locator = [
        ("xpath", "//ol[@id='selectable']/li"),
    ]

    multiple_selected_items_locator = [
        ("css", "#selectable li.ui-selected")
    ]

    grid_selection_items_locator = [
        ("css", "#selectable li"),
    ]

    grid_selected_items_locator = [
        ("css", "#selectable li"),
    ]


    serialize_selection_items_locator = [
        ("css", "#selectable li"),
    ]

    serialize_selected_items_locator = [
        ("css", "selectable li.ui-selected"),
    ]

    serialize_selected_text_locator = [
        ("id","select-result"),
    ]


