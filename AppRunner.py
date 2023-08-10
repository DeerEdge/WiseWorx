from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStatusBar



class ui_main_window(object):
    def setup_window(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1100, 800)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.resize(1100, 800)
        self.central_widget.setObjectName("display")

        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.resize(840, 800)
        self.tab_widget.move(260, 0)

        self.dash_tab = QtWidgets.QWidget()
        self.dash_tab.setObjectName("tab1")

        self.maps_tab = QtWidgets.QWidget()
        self.maps_tab.setObjectName("tab2")

        self.saved_tab = QtWidgets.QWidget()
        self.saved_tab.setObjectName("tab3")

        self.widget = QtWidgets.QWidget(self.dash_tab)

        self.tab_widget.addTab(self.dash_tab, "Dashboard")
        self.tab_widget.addTab(self.maps_tab, "Maps")
        self.tab_widget.addTab(self.saved_tab, "Saved")

        self.map_frame = QtWidgets.QVBoxLayout(self.central_widget)


        self.status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open("Styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    main_window = QtWidgets.QMainWindow()
    ui = ui_main_window()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())