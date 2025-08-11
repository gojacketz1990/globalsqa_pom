class DemoDragDropPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    click_photo_manager_tab_locator = [
        ("id","Photo Manager"),
        ("xpath", "//li[normalize-space()='Photo Manager']")
    ]

    click_accepted_elements_tab_locator = [
        ("id","Acccepted Elements"),
        ("xpath", "//li[normalize-space()='Accepted Elements']")
    ]

    click_propagation_tab_locator = [
        ("id","Propagation"),
        ("xpath", "//li[normalize-space()='Propagation']")
    ]

    photo_manager_demo_iframe =  [
        ("xpath", "//div[@rel-title='Photo Manager']/p/iframe")
    ]

    accepted_elements_demo_iframe =  [
        ("xpath", "//div[@rel-title='Accepted Elements']//iframe")
    ]

    propagation_demo_iframe =  [
        ("xpath", "//div[@rel-title='Propagation']//iframe")
    ]

    multiple_photos_list_locator = [
        ("xpath","//ul[@id='gallery'/li")
    ]

    gallery_item_by_name = [
        ("xpath", "//ul[@id='gallery']/li[./h5[text()='{}']]")
    ]
    # Dynamic locator for an item within the trash container
    trash_item_by_name = [
        ("xpath", "//div[@id='trash']//h5[text()='{}']/parent::li")
    ]


    trash_locator = [
        ("id","trash")
    ]

    #Accepted Elements stuff

    draggable_not_droppable_locator = [
        ("id","draggable-nonvalid")
    ]

    draggable_and_droppable_locator = [
        ("id","draggable")
    ]

    droppable_area_locator = [
        ("id","droppable")
    ]

    droppable_text_locator = [
        ("xpath", "//div[@id='droppable']/p")
    ]

    #Propagation locators

    draggable_prop_locator = [
        ("id","draggable")
    ]


    outer_not_greedy_droppable = [
        ("xpath", "//div[@id='droppable']/p")
    ]

    inner_not_greedy_droppable = [
        ("id","droppable-inner")
    ]

    outer_greedy_droppable = [
        ("xpath", "//div[@id='droppable2']/p")
    ]

    inner_greedy_droppable = [
        ("id","droppable2-inner")
    ]
