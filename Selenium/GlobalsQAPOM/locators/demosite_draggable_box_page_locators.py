class DemoDraggableBoxPageLocators():
    simple_drag_tab_locator = [
        ("id","Simple Drag"),
        ("xpath", "//li[normalize-space()='Simple Drag']")
    ]
    check_events_tab_locator = [
        ("id","Check Events"),
        ("xpath", "//li[normalize-space()='Check Events']")
    ]
    handle_tab_locator = [
        ("id","Handle"),
        ("xpath", "//li[normalize-space()='Handle']")
    ]
    constraints_tab_locator = [
        ("id","Constraints"),
        ("xpath", "//li[normalize-space()='Constraints']")
    ]
    simple_drag_iframe =  [
        ("xpath", "//div[@rel-title='Simple Drag']/p/iframe")
    ]

    constraints_iframe =  [
        ("xpath", "//div[@rel-title='Constraints']/p/iframe")
    ]

    check_events_iframe =  [
        ("xpath", "//div[@rel-title='Check Events']/p/iframe")
    ]

    handle_iframe =  [
        ("xpath", "//div[@rel-title='Handle']/p/iframe")
    ]
