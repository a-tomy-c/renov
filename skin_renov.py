# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_renov.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSplitter, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Renov(object):
    def setupUi(self, Renov):
        if not Renov.objectName():
            Renov.setObjectName(u"Renov")
        Renov.resize(600, 380)
        self.verticalLayout_3 = QVBoxLayout(Renov)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(Renov)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_info = QPushButton(self.frame_3)
        self.bt_info.setObjectName(u"bt_info")
        self.bt_info.setMaximumSize(QSize(50, 26))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(8)
        self.bt_info.setFont(font)

        self.horizontalLayout.addWidget(self.bt_info)

        self.bt_reload_template = QPushButton(self.frame_3)
        self.bt_reload_template.setObjectName(u"bt_reload_template")
        self.bt_reload_template.setMaximumSize(QSize(30, 26))
        self.bt_reload_template.setFont(font)

        self.horizontalLayout.addWidget(self.bt_reload_template)

        self.le_template = QLineEdit(self.frame_3)
        self.le_template.setObjectName(u"le_template")
        self.le_template.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout.addWidget(self.le_template)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_tags = QLineEdit(self.frame_3)
        self.le_tags.setObjectName(u"le_tags")
        self.le_tags.setMaximumSize(QSize(16777215, 26))
        self.le_tags.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_tags)

        self.bt_reload_tags = QPushButton(self.frame_3)
        self.bt_reload_tags.setObjectName(u"bt_reload_tags")
        self.bt_reload_tags.setEnabled(True)
        self.bt_reload_tags.setMaximumSize(QSize(30, 26))
        self.bt_reload_tags.setFont(font)

        self.horizontalLayout_2.addWidget(self.bt_reload_tags)

        self.cmb_tags = QComboBox(self.frame_3)
        self.cmb_tags.setObjectName(u"cmb_tags")
        self.cmb_tags.setMinimumSize(QSize(125, 0))
        self.cmb_tags.setMaximumSize(QSize(16777215, 26))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(9)
        self.cmb_tags.setFont(font1)

        self.horizontalLayout_2.addWidget(self.cmb_tags)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.splitter = QSplitter(Renov)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.tree = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree.setHeaderItem(__qtreewidgetitem)
        self.tree.setObjectName(u"tree")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree.sizePolicy().hasHeightForWidth())
        self.tree.setSizePolicy(sizePolicy)
        self.tree.setMinimumSize(QSize(0, 40))
        self.tree.setBaseSize(QSize(0, 1))
        self.tree.setFrameShadow(QFrame.Shadow.Plain)
        self.tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.splitter.addWidget(self.tree)
        self.tree.header().setVisible(False)
        self.text_edit = QTextEdit(self.splitter)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setFrameShadow(QFrame.Shadow.Plain)
        self.splitter.addWidget(self.text_edit)

        self.verticalLayout_2.addWidget(self.splitter)

        self.frame = QFrame(Renov)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 2, -1, -1)
        self.bt_renamer = QPushButton(self.frame)
        self.bt_renamer.setObjectName(u"bt_renamer")
        self.bt_renamer.setMaximumSize(QSize(16777215, 26))
        self.bt_renamer.setFont(font)

        self.horizontalLayout_4.addWidget(self.bt_renamer)

        self.le_newname = QLineEdit(self.frame)
        self.le_newname.setObjectName(u"le_newname")
        self.le_newname.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_4.addWidget(self.le_newname)

        self.bt_preview = QPushButton(self.frame)
        self.bt_preview.setObjectName(u"bt_preview")
        self.bt_preview.setMaximumSize(QSize(16777215, 26))
        self.bt_preview.setFont(font)

        self.horizontalLayout_4.addWidget(self.bt_preview)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Renov)

        QMetaObject.connectSlotsByName(Renov)
    # setupUi

    def retranslateUi(self, Renov):
        Renov.setWindowTitle(QCoreApplication.translate("Renov", u"Form", None))
        self.bt_info.setText(QCoreApplication.translate("Renov", u"INFO", None))
        self.bt_reload_template.setText(QCoreApplication.translate("Renov", u"RT", None))
        self.bt_reload_tags.setText(QCoreApplication.translate("Renov", u"R", None))
        self.bt_renamer.setText(QCoreApplication.translate("Renov", u"RENAMER", None))
        self.bt_preview.setText(QCoreApplication.translate("Renov", u"PREVIEW", None))
    # retranslateUi

