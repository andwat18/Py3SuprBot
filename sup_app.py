import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class SupremeApp(QWidget):

    def __init__(self):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        super(SupremeApp, self).__init__()
        horizbox = QHBoxLayout()
        vertbox = QVBoxLayout()

        #             buttons               #
        self.init_user_btn = QPushButton('Initialize User', self)
        self.connect(self.init_user_btn, SIGNAL('clicked()'),
                     lambda: self.createUserInfoModalWindow())
        self.cart_btn = QPushButton('Cart', self)
        self.sizing_btn = QPushButton('Sizing', self)
        self.bot_help_btn = QPushButton('Bot Help', self)
        self.start_btn = QPushButton('Start Bot', self)

        horizbox.addWidget(self.init_user_btn)
        horizbox.addWidget(self.cart_btn)
        horizbox.addWidget(self.sizing_btn)
        horizbox.addWidget(self.bot_help_btn)
        horizbox.addWidget(self.start_btn)

        #            items field            #
        self.field_layout = QGridLayout()

        self.create_table()

        area = QWidget()
        area.setLayout(self.field_layout)
        self.items_field = QScrollArea()
        self.items_field.setWidget(area)
        self.items_field.show()
        vertbox.addWidget(self.items_field)
        vertbox.addLayout(horizbox)

        #           main window           #
        self.setGeometry(2500, 100, 1186, 875)
        self.setLayout(vertbox)
        self.setFixedWidth(1186)
        self.setWindowTitle('PySupBot')

        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'supr.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show()

        self.setStyleSheet("""
            QPushButton:hover {
                background-color: red;
                color: white;
                outline: none
            }
        """)

    def createItemModalWindow(self, args):
        window_modal = ItemModalWindow(args)


    def createUserInfoModalWindow(self):
        window_modal = UserInfoModalWindow()


    def create_table(self):
        images_path = self.scriptDir + '/TempPNGS'
        for i in range(6):
            for j in range(5):
                img_name = str(i) + str(j) + '.png'
                if img_name in os.listdir(images_path):
                    btn = QPushButton()
                    btn.setIcon(QIcon('TempPNGS/' + img_name))
                    btn.setIconSize(QSize(200, 200))
                    self.field_layout.addWidget(btn, i, j)
                    # temp #
                    item_name = 'Supreme®/Comme des Garçons SHIRT® Split Box Logo Tee'
                    colorways = ['White', 'Black', 'Red']
                    descr = 'Description: All cotton crewneck with vertical seam at front and diagonal seam at lower back.'\
                            '\nPrinted logos on front and on back.'\
                            '\nMade exclusively for Supreme.'\
                            '\n\nPrice: 54doll, 48pounds, 54eur, 9720y'
                    image_num = str(i) + str(j)
                    argsz = [item_name, colorways, descr, image_num]
                    self.connect(btn,
                                 SIGNAL('clicked()'),
                                 lambda: self.createItemModalWindow(argsz))


class ItemModalWindow(QDialog):
    def __init__(self, args):
        super(ItemModalWindow, self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.dialog_window = QDialog(self)
        self.horizbox = QHBoxLayout()

        self.item_image = QLabel()
        pixmap = QPixmap(self.scriptDir + '/NewJPGS/' + args[3] + '.jpg')
        self.item_image.setPixmap(pixmap)
        self.vertbox = QVBoxLayout()

        self.description = QLabel()
        self.description.setWordWrap(True)
        self.description.setFixedSize(300, 360)
        self.description.setText(args[2])
        self.color_combo = QComboBox()
        self.size_combo = QComboBox()
        self.add_to_cart = QPushButton()
        self.add_to_cart.setText("Add to Cart")

        #            temp options            #
        color_combo_opts = args[1]
        size_combo_opts = ['Small',
                           'Medium',
                           'Lagre',
                           'XLarge']
        self.size_combo.addItems(size_combo_opts)
        self.color_combo.addItems(color_combo_opts)

        self.horizbox.addWidget(self.item_image)
        self.horizbox.addLayout(self.vertbox)

        self.vertbox.addWidget(self.description)
        self.vertbox.addWidget(self.color_combo)
        self.vertbox.addWidget(self.size_combo)
        self.vertbox.addWidget(self.add_to_cart)

        self.dialog_window.setLayout(self.horizbox)

        self.dialog_window.setFixedSize(850, 550)
        self.dialog_window.setWindowTitle(args[0])
        self.dialog_window.setModal(True)
        self.dialog_window.exec_()


class UserInfoModalWindow(QDialog):
    def __init__(self):
        super(UserInfoModalWindow, self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.dialog_window = QDialog(self)
        self.grid = QGridLayout()

        #           user input fields            #
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.telephone_input = QLineEdit()
        self.address_input = QLineEdit()
        self.address2_input = QLineEdit()
        self.address3_input = QLineEdit()
        self.city_input = QLineEdit()
        self.postcode_input = QLineEdit()
        self.country_combo = QComboBox()
        self.card_type_combo = QComboBox()
        self.card_number_input = QLineEdit()
        self.card_month_combo = QComboBox()
        self.card_year_combo = QComboBox()
        self.card_cvv_input = QLineEdit()
        self.cancel_button = QPushButton()
        self.save_button = QPushButton()

        #         placing elements in a grid       #
        self.grid.addWidget(self.name_input,        0, 0, 1, 2)
        self.grid.addWidget(self.email_input,       1, 0, 1, 2)
        self.grid.addWidget(self.telephone_input,   2, 0, 1, 2)
        self.grid.addWidget(self.address_input,     3, 0, 1, 1)
        self.grid.addWidget(self.address2_input,    3, 1, 1, 1)
        self.grid.addWidget(self.address3_input,    4, 0, 1, 2)
        self.grid.addWidget(self.city_input,        5, 0, 1, 2)
        self.grid.addWidget(self.postcode_input,    6, 0, 1, 1)
        self.grid.addWidget(self.country_combo,     6, 1, 1, 1)
        self.grid.addWidget(self.card_type_combo,   0, 2, 1, 3)
        self.grid.addWidget(self.card_number_input, 1, 2, 1, 3)
        self.grid.addWidget(self.card_month_combo,  2, 2, 1, 1)
        self.grid.addWidget(self.card_year_combo,   2, 3, 1, 1)
        self.grid.addWidget(self.card_cvv_input,    2, 4, 1, 1)
        self.grid.addWidget(self.cancel_button,     6, 2, 1, 1)
        self.grid.addWidget(self.save_button,       6, 3, 1, 2)

        #        setting parameters for user inputs      #
        self.name_input.setPlaceholderText("Full name")
        self.email_input.setPlaceholderText("E-mail")
        self.telephone_input.setPlaceholderText("Telephone number")
        self.address_input.setPlaceholderText("Address")
        self.address2_input.setPlaceholderText("Address 2")
        self.address3_input.setPlaceholderText("Address 3")
        self.city_input.setPlaceholderText("City")
        self.postcode_input.setPlaceholderText("Postcode")
        self.card_number_input.setPlaceholderText("Card number")
        self.card_cvv_input.setPlaceholderText("CVV")

        self.country_combo.addItems(['GB', 'NB', 'AT', 'BY', 'BE', 'BG', 'HR', 'CZ', 'DK', 'EE', 'FI',
                                     'FR', 'DE', 'GR', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MC',
                                     'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR'])
        self.card_type_combo.addItems(['Visa', 'American Express', 'Mastercard', 'Solo', 'PayPal'])
        self.card_month_combo.addItems(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'])
        self.card_year_combo.addItems(['2018', '2019', '2020', '2021', '2022', '2023',
                                       '2024', '2025', '2026', '2027', '2028'])

        self.cancel_button.setText('Cancel')
        self.save_button.setText('Accept And Save')

        #           setting validators           #
        self.onlyInt = QIntValidator()
        self.onlyLong = QDoubleValidator()

        name_re = QRegExp("[a-zA-Z ]+")
        name_input_validator = QRegExpValidator(name_re, self.name_input)
        self.name_input.setValidator(name_input_validator)

        self.telephone_input.setValidator(self.onlyLong)

        city_re = QRegExp("[a-zA-Z, ]+")
        city_input_validator = QRegExpValidator(city_re, self.city_input)
        self.city_input.setValidator(city_input_validator)

        self.postcode_input.setValidator(self.onlyInt)

        card_number_re = QRegExp("[0-9]{,16}")
        card_number_validator = QRegExpValidator(card_number_re, self.card_cvv_input)
        self.card_number_input.setValidator(card_number_validator)

        card_cvv_re = QRegExp("[0-9]{,3}")
        card_cvv_validator = QRegExpValidator(card_cvv_re, self.card_cvv_input)
        self.card_cvv_input.setValidator(card_cvv_validator)

        #            connecting slots           #
        self.connect(self.cancel_button,
                     SIGNAL('clicked()'),
                     lambda: self.canceled())

        self.connect(self.save_button,
                     SIGNAL('clicked()'),
                     lambda: self.save_user_info())

        self.dialog_window.setLayout(self.grid)
        self.dialog_window.setFixedSize(656, 369)
        self.dialog_window.setWindowTitle("User billing information")
        self.dialog_window.setModal(True)
        self.dialog_window.exec_()


    def save_user_info(self):
        print("Here to save info")
        user = {}
        user['name'] = str(self.name_input.text())
        user['email'] = str(self.email_input.text())
        user['tel'] = str(self.telephone_input.text())
        user['address'] = str(self.address_input.text())
        user['address2'] = str(self.address2_input.text())
        user['address3'] = str(self.address3_input.text())
        user['city'] = str(self.city_input.text())
        user['postcode'] = str(self.postcode_input.text())
        user['country'] = str(self.country_combo.currentText())
        user['card_type'] = str(self.card_type_combo.currentText())
        user['card_number'] = str(self.card_number_input.text())
        user['card_month'] = str(self.card_month_combo.currentText())
        user['card_year'] = str(self.card_year_combo.currentText())
        user['card_cvv'] = str(self.card_cvv_input.text())

        dump_name = '_'.join(user['name'].split(' '))
        print(user)
        print(dump_name)


    def canceled(self):
        accept_dialog = AcceptDialogWindow()


    def quit(self):
        print("Here to close window")


class AcceptDialogWindow(UserInfoModalWindow):
    def __init__(self):
        super(UserInfoModalWindow, self).__init__()
        self.accept_dialog = QDialog()
        self.grid = QGridLayout()
        self.warning_text = QLabel()
        self.accept_button = QPushButton()
        self.cancel_button = QPushButton()

        self.grid.addWidget(self.warning_text, 0, 0, 1, 2)
        self.grid.addWidget(self.accept_button, 1, 1, 1, 1)
        self.grid.addWidget(self.cancel_button, 1, 0, 1, 1)

        self.warning_text.setText('Are you sure? \nInformation will be lost.')
        self.warning_text.setAlignment(Qt.AlignCenter)
        self.accept_button.setText('Accept')
        self.cancel_button.setText('Cancel')

        self.accept_dialog.setLayout(self.grid)
        self.accept_dialog.setFixedSize(250, 150)
        self.accept_dialog.setWindowTitle('Accept action')
        self.accept_dialog.setModal(True)

        self.connect(self.accept_button,
                     SIGNAL('clicked()'),
                     lambda: self.close_windows())
        self.connect(self.cancel_button,
                     SIGNAL('clicked()'),
                     self.accept_dialog.close)
        self.accept_dialog.exec_()


    def close_windows(self):
        self.accept_dialog.close()
        return super(AcceptDialogWindow, self).quit()


def mainApp():
    app = QApplication(sys.argv)
    GUI = SupremeApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mainApp()
