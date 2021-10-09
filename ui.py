import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, 
QMenuBar, QMenu, QToolBar, QAction, QVBoxLayout, QWidget, QHBoxLayout, QCheckBox, QTabWidget, QFormLayout, QGroupBox, QLineEdit)

import formLayout

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("eFuse Programming Current Measurement")
        self.resize(1200, 700)
        # self.centralWidget = QLabel("Hello, World")
        # self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(self.centralWidget)
        
        self.tdsCommandGroupBox()
        self.initUI()
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()
        self._createStatusBar()
 
        self.show()

    def initUI(self):
        widget = QWidget()

        vlayout_left = QVBoxLayout()
        vlayout_right = QVBoxLayout()
        hlayout = QHBoxLayout()

        a1 = QLabel('label1')
        a2 = QLabel('label2')

        tabs = QTabWidget()
        tabs.addTab(self.sourcemeterlTabUI(), "2400 SMU")
        tabs.addTab(self.oscilloscopeTabUI(), "TDS3000C OSC")
        tabs.addTab(self.pulseTabUI(), "HP81130A")

        vlayout_left.addWidget(tabs)
        vlayout_right.addWidget(a2)
        hlayout.addLayout(vlayout_left)
        hlayout.addLayout(vlayout_right)
        hlayout.addStretch()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)

    def sourcemeterlTabUI(self):
        """Create the Source Meter page UI."""
        sourcemeterTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("SMU Option 1"))
        layout.addWidget(QCheckBox("SMU Option 2"))
        layout.addStretch()

        sourcemeterTab.setLayout(layout)

        return sourcemeterTab

    def oscilloscopeTabUI(self):
        """Create the Oscilloscope page UI."""
        scopeTab = QWidget()
        layout = QVBoxLayout()

        channelTab = QTabWidget()
        channelTab.addTab(self.tdsCommandGroupBox(), "CH1")
        channelTab.addTab(self.tdsCommandGroupBox(), "CH2")
        channelTab.addTab(self.tdsCommandGroupBox(), "CH3")
        channelTab.addTab(self.tdsCommandGroupBox(), "CH4")

        layout.addWidget(channelTab)
        scopeTab.setLayout(layout)
        layout.addStretch()

        return scopeTab

    def tdsCommandGroupBox(self):
        widget = QWidget()
        vlayout = QVBoxLayout()
        # Vertical Commands
        verticalGroupBox = QGroupBox("Vertical Commands")
        verticalLayout = QFormLayout()
        verticalLayout.addRow(QLabel("Bandwidth:"), QLineEdit())
        verticalLayout.addRow(QLabel("Coupling:"), QLineEdit())
        verticalLayout.addRow(QLabel("Impedance:"), QLineEdit())
        verticalLayout.addRow(QLabel("Position:"), QLineEdit())
        verticalLayout.addRow(QLabel("Probe:"), QLineEdit())
        verticalLayout.addRow(QLabel("Scale:"), QLineEdit())
        verticalLayout.addRow(QLabel("Unit:"), QLineEdit())
        # Horizontal Commands
        horizontalGroupBox = QGroupBox("Horizontal Commands")
        horizontalLayout = QFormLayout()
        horizontalLayout.addRow(QLabel("Time per Division:"), QLineEdit())
        horizontalLayout.addRow(QLabel("Delay:"), QLineEdit())
        # Waveform Data Commands
        waveformGroupBox = QGroupBox("Waveform Data")
        waveformLayout = QFormLayout()
        waveformLayout.addRow(QLabel("Data Start:"), QLineEdit())
        waveformLayout.addRow(QLabel("Data Stop:"), QLineEdit())

        verticalGroupBox.setLayout(verticalLayout)
        horizontalGroupBox.setLayout(horizontalLayout)
        waveformGroupBox.setLayout(waveformLayout)
        vlayout.addWidget(verticalGroupBox)
        vlayout.addWidget(horizontalGroupBox)
        vlayout.addWidget(waveformGroupBox)
        widget.setLayout(vlayout)

        return widget

    def pulseTabUI(self):
        """Create the Pulse page UI."""
        pulseTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Pulse Option 1"))
        layout.addWidget(QCheckBox("Pulse Option 2"))
        layout.addStretch()

        pulseTab.setLayout(layout)

        return pulseTab

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
        # self.centralWidget.setText("<b>File > New</b> clicked")
        form = formLayout.FormDialog()
        form.exec()

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