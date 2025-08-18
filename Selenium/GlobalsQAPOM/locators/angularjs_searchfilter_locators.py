class AngularJSSearchFilterPageLocators():
    payee_search_box_locator =  [
        ("id", "input1")
    ]

    account_dropdown_locator =  [
        ("id", "input2")
    ]

    search_by_type_dropdown_locator =  [
        ("id", "input3")
    ]

    search_by_expenditure_payees_locator =  [
        ("id", "input4")
    ]

    search_results_table_locator = [
        ("css",".table.table-striped.table-bordered")
    ]
    results_table_rows = [("xpath", "./tr")]

    results_table_body = [("xpath", "//table[@class='table table-striped table-bordered']/tbody")]
    results_table_rows = [("xpath", "./tr")]
    results_table_cells = [("xpath", "./td")]
