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

    simple_drag_box_locator = [
        ("id","draggable"),
    ]


    check_events_box_locator  = [
        ("id","draggable"),
    ]

    # Event counters (targeting the span with the count)
    event_start_count = [
        ("xpath", "//li[@id='event-start']/span[@class='count']")
    ]
    event_drag_count = [
        ("xpath", "//li[@id='event-drag']/span[@class='count']")
    ]
    event_stop_count = [
        ("xpath", "//li[@id='event-stop']/span[@class='count']")
    ]

    # Main container element that should not be draggable
    draggable_container = [
        ("id", "draggable")
    ]
    # The specific handle element that *is* draggable
    draggable_handle = [
        ("css", "#draggable .ui-draggable-handle")
    ]

    #Constraints Tab

    vertical_drag_locator = [
        ("id", "draggable")
    ]

    horizontal_drag_locator = [
        ("id", "draggable2")
    ]

    box_contained_locator = [
        ("id", "draggable3")
    ]

    contained_in_box_locator = [
        ("id","draggable4")
    ]

    dom_container_locator = [
        ("id","containment-wrapper")
    ]


