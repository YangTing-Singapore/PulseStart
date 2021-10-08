import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, 
QMenuBar, QMenu, QToolBar, QAction, QVBoxLayout, QWidget, QHBoxLayout, QCheckBox, QTabWidget)

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("eFuse Programming Current Measurement")
        self.resize(800, 400)
        # self.centralWidget = QLabel("Hello, World")
        # self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(self.centralWidget)

        self.initUI()
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()
        self._createStatusBar()
################################################################
        # layout = QVBoxLayout()
        # self.testlabel_1 = QLabel("Hello, World!")
        # layout.addwidget(self.testlabel_1)

        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
######################################################################
        self.show()

    def initUI(self):
        widget = QWidget()

        # vlayout = QVBoxLayout(widget)
        # vlayout = QVBoxLayout()
        vlayout_left = QVBoxLayout()
        vlayout_right = QVBoxLayout()
        hlayout = QHBoxLayout()

        a1 = QLabel('label1')
        a2 = QLabel('label2')

        tabs = QTabWidget()
        tabs.addTab(self.sourcemeterlTabUI(), "2400 SMU")
        tabs.addTab(self.oscilloscopeTabUI(), "TDS3000C OSC")


        # hlayout.addWidget(a1)
        # hlayout.addWidget(tabs)
        # hlayout.addWidget(a2)
        # hlayout.addStretch()
        # vlayout.addLayout(hlayout)
        # vlayout.addStretch()
        # widget.setLayout(vlayout)

        vlayout_left.addWidget(tabs)
        vlayout_right.addWidget(a2)
        hlayout.addLayout(vlayout_left)
        hlayout.addLayout(vlayout_right)
        hlayout.addStretch()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)

    def sourcemeterlTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("General Option 1"))
        layout.addWidget(QCheckBox("General Option 2"))
        layout.addStretch()

        generalTab.setLayout(layout)

        return generalTab

    def oscilloscopeTabUI(self):
        """Create the Network page UI."""
        networkTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        networkTab.setLayout(layout)
        layout.addStretch()

        return networkTab

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Edit meun
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        # Find and Replace submenu in the Edit menu
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")
        # Help menu
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)

    def _createActions(self):
        self.newAction = QAction("&New", self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)

    def _connectActions(self):
        # Connect File actions
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        # Connect Help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

    def getWordCount(self):
        # Logic for computing the word count goes here...
        return 42

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusbar.showMessage("Welcome to eFuse Programming Current Measurement System", 3000)
        self.wcLabel = QLabel(f"{self.getWordCount()} Words")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def newFile(self):
        # Logic for creating a new file goes here...
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        # Logic for opening an existing file goes here...
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        # Logic for launching help goes here...
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())