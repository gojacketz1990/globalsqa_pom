class DemoSortingPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    click_portlets_tab = [
        ("id","Portlets"),
        ("xpath", "//li[normalize-space()='Portlets']")
    ]

    click_multiple_lists_tab = [
        ("id","Multiple Lists"),
        ("xpath", "//li[normalize-space()='Multiple Lists']")
    ]

    click_simple_list_tab = [
        ("id","Simple List"),
        ("xpath", "//li[normalize-space()='Simple List']")
    ]

    click_grid_sorting_tab = [
        ("id","Grid Sorting"),
        ("xpath", "//li[normalize-space()='Grid Sorting']")
    ]

    all_portlet_headers_locator = [
        ("css","div.portlet-header")
    ]


    portlets_iframe_locator = [
        ("xpath", "//div[@rel-title='Portlets']//iframe")
    ]

    multiple_lists_iframe_locator = [
        ("xpath", "//div[@rel-title='Multiple Lists']//iframe")
    ]

    simple_list_iframe_locator = [
        ("xpath", "//div[@rel-title='Simple List']//iframe")
    ]

    grid_sorting_iframe_locator = [
        ("xpath", "//div[@rel-title='Grid Sorting']//iframe")
    ]

    # This locator finds the first list's container
    sortable1_list_locator = [("id", "sortable1")]

    # This locator finds any sortable item within the first list
    # The XPath uses '|' to check for both possible classes
    sortable1_items_locator = [("xpath", "//ul[@id='sortable1']/li[contains(@class, 'ui-state-default') or contains(@class, 'ui-state-highlight')]")]

    # This locator finds the second list's container
    sortable2_list_locator = [("id", "sortable2")]

    # This locator finds any sortable item within the second list
    # It also uses '|' to check for both classes
    sortable2_items_locator = [("xpath", "//ul[@id='sortable2']/li[contains(@class, 'ui-state-default') or contains(@class, 'ui-state-highlight')]")]

    # This is a general locator to find all sortable items across both lists.
    # It's useful when you want to drag an item from one list and drop it onto an element in the other.
    all_sortable_items_locator = [("xpath", "//ul[contains(@id, 'sortable')]/li[contains(@class, 'ui-sortable-handle')]")]

    # This is a general locator for the containers of both lists
    all_list_containers_locator = [("xpath", "//ul[contains(@id, 'sortable')]")]

        # A flexible locator that can find all list items within a specific list ID.
    def get_list_items_locator(self, list_id: str):
        return [("xpath", f"//ul[@id='{list_id}']/li")]

    # A flexible locator that can find a specific list item by text within a specific list ID.
    def get_list_item_locator_by_text(self, list_id: str, item_text: str):
        return [("xpath", f"//ul[@id='{list_id}']/li[contains(text(), '{item_text}')]")]

    #
    # simple_list_items_locator = [
    #     ("xpath", "//ul[@id='sortable']/li"),
    # ]
    #
    # simple_list_item_handle_locator = [
    #     ("css","span")
    # ]

    # Locator for the individual <li> elements in the simple list
    simple_list_items_locator = [("xpath", "//ul[@id='sortable']/li")]

    # NEW LOCATOR: Targets the inner <span> handle specifically
    simple_list_item_handle_locator = [("css", "span.ui-icon-arrowthick-2-n-s")]

    grid_sorting_items_locator = [
        ("xpath", "//ul[@id='sortable']/li"),
    ]



