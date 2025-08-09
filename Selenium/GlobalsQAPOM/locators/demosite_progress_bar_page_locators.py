class DemoProgressBarPageLocators():
    demo_iframe =  [
        ("class_name", "demo-frame"),
    ]

    download_manager_demo_iframe =  [
        ("xpath", "//div[@rel-title='Download Manager']//iframe")
    ]

    random_progress_bar_demo_iframe =  [
        ("xpath", "//div[@rel-title='Random Progress Bar']//iframe")
    ]

    start_download_button_locator = [
        ("id", "downloadButton"),
        ("xpath", "//button[text()='Start Download']")
    ]

    downloading_button_locator = [
        ("xpath", "//button[text()='Downloading...']")
    ]

    downloading_dialog_locator = [
        ("id", "ui-id-1"),
        ("css", "span.ui-dialog-title")
    ]

    file_download_close_locator = [
        ("xpath", "//div[@class='ui-dialog-buttonset']/button[text()='Close']")
    ]

    close_download_button_locator = [
        ("xpath","//button[text()='Close']"),
        ("css",".ui-dialog-buttonpane .ui-button")
    ]

    cancel_download_button_locator = [
        ("xpath","//button[text()='Cancel']"),
        ("css",".ui-dialog-buttonpane .ui-button")
    ]

    progress_bar_locator = [
        ("css","#progressbar"),
        ("id","progressbar")
    ]

    random_value_determinate_button_locator = [
        ("id","numButton"),
        ("xpath","//button[text()='Random Value - Determinate']"),
    ]

    indeterminate_button_locator = [
        ("id","falseButton"),
        ("xpath","//button[text()='Indeterminate']"),
    ]

    random_color_button_locator = [
        ("id","colorButton"),
        ("xpath","//button[text()='Random Color']"),
    ]

    random_progress_bar_locator = [
        ("css","div.ui-progressbar-value")
    ]

    random_progress_bar_tab = [
        ("id","Random Progress Bar"),
        ("xpath", "//li[normalize-space()='Random Progress Bar']"),
    ]
