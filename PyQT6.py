# basic_window.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 630, 640)
        self.setWindowTitle("Приветствие")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        hello_label = QLabel(self)
        hello_label.setText("Привет Мир!")
        hello_label.setFont(QFont("Times New Roman", 60, QFont.Weight.Bold))
        hello_label.setStyleSheet("color: white; background: transparent")
        hello_label.move(50,300)

        image = "привет.jpg"
        try:
            with open(image):
                label = QLabel(self)
                pixmap = QPixmap(image)

                # Масштабируем картинку под размер окна
                scaled_pixmap = pixmap.scaled(
                    self.size(),  # используем размер окна
                )
                # Устанавливаем масштабированное изображение
                label.setPixmap(scaled_pixmap)
                label.setGeometry(0, 0, self.width(), self.height())

                label.lower()  # фон под текстом
        except FileNotFoundError:
            print(f"Файл {image} не найден")


class MainWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 500, 800)
        self.setWindowTitle("Резюме")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Создаёт фон из второго изображения и размещает первое изображение поверх него."""
        # --- Второе изображение как фон ---
        bg_image = "стена.jpg"
        bg_pixmap = QPixmap(bg_image)
        if bg_pixmap.isNull():
            print(f"Не удалось загрузить {bg_image}")
        else:
            # Масштабируем под размер окна
            bg_scaled = bg_pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.bg_label = QLabel(self)
            self.bg_label.setPixmap(bg_scaled)
            self.bg_label.resize(self.width(), self.height())
            self.bg_label.move(0, 0)
            self.bg_label.lower()  # фон под всеми остальными виджетами

        # --- Первое изображение поверх фона ---
        fg_image = "фел.jpg"
        fg_pixmap = QPixmap(fg_image)
        if fg_pixmap.isNull():
            print(f"Не удалось загрузить {fg_image}")
        else:
            # Масштабируем первое изображение
            fg_scaled = fg_pixmap.scaled(
                300, 200,  # желаемый размер
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            fg_label = QLabel(self)
            fg_label.setPixmap(fg_scaled)
            fg_label.resize(fg_scaled.width(), fg_scaled.height())
            fg_label.move(170, 60)  # позиция на фоне

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText("Карамян Феликс")
        user_label.setFont(QFont("Times New Roman", 32,QFont.Weight.Thin))
        user_label.setStyleSheet("color: black;")
        user_label.move(83, 0)

        bio_label = QLabel(self)
        bio_label.setText("Биография:")
        bio_label.setFont(QFont("Times New Roman", 25))
        bio_label.setStyleSheet("color: black;")
        bio_label.move(10,260)

        about_label = QLabel(self)
        about_label.setText("Студент 2 курса МАИ, М3О-236БВ-24")
        about_label.setWordWrap(True)
        about_label.setFont(QFont("Times New Roman", 18))
        about_label.setStyleSheet("color: black;")
        about_label.move(180, 260)

        skills_label = QLabel(self)
        skills_label.setText("Умения:")
        skills_label.setFont(QFont("Times New Roman", 25))
        skills_label.setStyleSheet("color: black;")
        skills_label.move(10, 350)

        languages_label = QLabel(self)
        languages_label.setText("Красиво фотографирую ")
        languages_label.setFont(QFont("Times New Roman", 18))
        languages_label.setStyleSheet("color: black;")
        languages_label.move(135, 357)

        experience_label = QLabel(self)
        experience_label.setText("Опыт:")
        experience_label.setFont(QFont("Times New Roman", 25))
        experience_label.setStyleSheet("color: black;")
        experience_label.move(10, 400)

        developer_label = QLabel(self)
        developer_label.setText("Панорама")
        developer_label.setFont(QFont("Times New Roman", 18))
        developer_label.setStyleSheet("color: black;")
        developer_label.move(105, 407)


        driver_label = QLabel(self)
# Запустить программу
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window1 = MainWindow1()
    sys.exit(app.exec())

