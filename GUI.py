# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Jan 18 15:19:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(318, 314)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setLayoutMode(QtGui.QListView.SinglePass)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.minPartLength = QtGui.QSpinBox(self.frame)
        self.minPartLength.setMinimum(1)
        self.minPartLength.setObjectName(_fromUtf8("minPartLength"))
        self.gridLayout_2.addWidget(self.minPartLength, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 2)
        self.epsilon = QtGui.QSpinBox(self.frame)
        self.epsilon.setMinimum(1)
        self.epsilon.setObjectName(_fromUtf8("epsilon"))
        self.gridLayout_2.addWidget(self.epsilon, 0, 2, 1, 1)
        self.Depth = QtGui.QSpinBox(self.frame)
        self.Depth.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.Depth.setSuffix(_fromUtf8(""))
        self.Depth.setPrefix(_fromUtf8(""))
        self.Depth.setMinimum(1)
        self.Depth.setObjectName(_fromUtf8("Depth"))
        self.gridLayout_2.addWidget(self.Depth, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        self.saveWeightVector = QtGui.QCheckBox(self.groupBox)
        self.saveWeightVector.setObjectName(_fromUtf8("saveWeightVector"))
        self.verticalLayout.addWidget(self.saveWeightVector)
        self.fileReminder = QtGui.QCheckBox(self.groupBox)
        self.fileReminder.setChecked(False)
        self.fileReminder.setObjectName(_fromUtf8("fileReminder"))
        self.verticalLayout.addWidget(self.fileReminder)
        self.NextLetter = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(9)
        self.NextLetter.setFont(font)
        self.NextLetter.setObjectName(_fromUtf8("NextLetter"))
        self.verticalLayout.addWidget(self.NextLetter)
        self.ResetLetter = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(9)
        self.ResetLetter.setFont(font)
        self.ResetLetter.setObjectName(_fromUtf8("ResetLetter"))
        self.verticalLayout.addWidget(self.ResetLetter)
        self.OK = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(9)
        self.OK.setFont(font)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.verticalLayout.addWidget(self.OK)
        self.gridLayout.addWidget(self.groupBox, 1, 2, 1, 1)
        self.GeneratedWord = QtGui.QLabel(Form)
        self.GeneratedWord.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Estrangelo Edessa"))
        font.setPointSize(14)
        self.GeneratedWord.setFont(font)
        self.GeneratedWord.setAutoFillBackground(False)
        self.GeneratedWord.setStyleSheet(_fromUtf8(""))
        self.GeneratedWord.setFrameShape(QtGui.QFrame.Box)
        self.GeneratedWord.setFrameShadow(QtGui.QFrame.Plain)
        self.GeneratedWord.setLineWidth(1)
        self.GeneratedWord.setMidLineWidth(0)
        self.GeneratedWord.setScaledContents(False)
        self.GeneratedWord.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GeneratedWord.setWordWrap(True)
        self.GeneratedWord.setMargin(2)
        self.GeneratedWord.setIndent(2)
        self.GeneratedWord.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.GeneratedWord.setObjectName(_fromUtf8("GeneratedWord"))
        self.gridLayout.addWidget(self.GeneratedWord, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Wortsport", None))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "wefwef", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("Form", "Menu", None))
        self.label_2.setText(_translate("Form", "Depth", None))
        self.label.setText(_translate("Form", "Min Partlength", None))
        self.label_3.setText(_translate("Form", "ε", None))
        self.saveWeightVector.setText(_translate("Form", "Save Weight Vector", None))
        self.fileReminder.setText(_translate("Form", "Remember Files", None))
        self.NextLetter.setText(_translate("Form", "Next Letter", None))
        self.ResetLetter.setText(_translate("Form", "Reset Letter", None))
        self.OK.setText(_translate("Form", "Exit", None))
        self.GeneratedWord.setText(_translate("Form", "TextLabel", None))
