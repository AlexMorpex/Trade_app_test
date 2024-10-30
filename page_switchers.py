def switch_centerMenu(ui, index):
    if ui.centerMenu.isHidden():
        ui.centerMenu.setVisible(True)
    else:
        if ui.stackedWidget.currentIndex() == index:
            ui.centerMenu.setHidden(True)
        else:
            ui.stackedWidget.setCurrentIndex(index)
    ui.stackedWidget.setCurrentIndex(index)
