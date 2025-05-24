from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QScrollArea, QSizePolicy, QFrame)
from PyQt6.QtCore import Qt
import os

class RileyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Riley-AI: Sentient Desktop Assistant")
        self.setMinimumSize(900, 500)
        self.setStyleSheet("background: transparent;")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.init_sidebar()
        self.init_chat_area()
        self.apply_styles()

    def init_sidebar(self):
        self.sidebar_widget = QWidget()
        self.sidebar_widget.setObjectName("SidebarWidget")
        self.sidebar_layout = QVBoxLayout(self.sidebar_widget)
        self.sidebar_layout.setContentsMargins(8, 16, 8, 16)
        self.sidebar_layout.setSpacing(12)
        self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sidebar_title = QLabel("Riley-AI")
        self.sidebar_title.setObjectName("SidebarTitle")
        self.sidebar_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.sidebar_layout.addWidget(self.sidebar_title)
        self.sidebar_buttons = []
        button_info = [
            ("Personality", self.on_personality),
            ("Voice", self.on_voice),
            ("Memory", self.on_memory),
            ("Ingest File", self.on_ingest_file),
            ("Wiki Search", self.on_wiki_search),
            ("Code Assist", self.on_code_assist),
            ("Settings", self.on_settings),
            ("Clear Chat", self.on_clear_chat),
            ("Exit", self.on_exit)
        ]
        for text, handler in button_info:
            btn = QPushButton(text)
            btn.setObjectName("SidebarButton")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setMinimumHeight(28)
            btn.clicked.connect(handler)
            self.sidebar_layout.addWidget(btn)
            self.sidebar_buttons.append(btn)
        self.sidebar_layout.addStretch(1)
        self.sidebar_scroll = QScrollArea()
        self.sidebar_scroll.setWidgetResizable(True)
        self.sidebar_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar_scroll.setWidget(self.sidebar_widget)
        self.sidebar_scroll.setMaximumWidth(320)
        self.layout.addWidget(self.sidebar_scroll)

    def init_chat_area(self):
        self.chat_container = QWidget()
        self.chat_container.setObjectName("ChatContainer")
        self.chat_container.setMaximumWidth(200)  # Limit chat area width
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setContentsMargins(18, 18, 18, 18)
        self.chat_layout.setSpacing(10)
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setObjectName("ChatDisplay")
        self.chat_display.setMinimumHeight(120)
        self.chat_display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.chat_layout.addWidget(self.chat_display, stretch=1)
        self.input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setObjectName("InputBox")
        self.input_box.setPlaceholderText("Type your message to Riley...")
        self.input_box.returnPressed.connect(self.on_send)
        self.input_layout.addWidget(self.input_box, stretch=1)
        self.send_btn = QPushButton("Send")
        self.send_btn.setObjectName("SendButton")
        self.send_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_btn.clicked.connect(self.on_send)
        self.input_layout.addWidget(self.send_btn)
        self.chat_layout.addLayout(self.input_layout)
        self.layout.addWidget(self.chat_container, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

    def apply_styles(self):
        with open(os.path.join(os.path.dirname(__file__), 'styles.qss'), 'r') as f:
            self.setStyleSheet(f.read())

    # --- Sidebar button actions ---
    def on_personality(self):
        self.append_chat("[Riley] Personality module coming soon.")
    def on_voice(self):
        self.append_chat("[Riley] Voice module coming soon.")
    def on_memory(self):
        self.append_chat("[Riley] Memory module coming soon.")
    def on_ingest_file(self):
        self.append_chat("[Riley] File ingestion coming soon.")
    def on_wiki_search(self):
        self.append_chat("[Riley] Wiki search coming soon.")
    def on_code_assist(self):
        self.append_chat("[Riley] Code assist coming soon.")
    def on_settings(self):
        self.append_chat("[Riley] Settings coming soon.")
    def on_clear_chat(self):
        self.chat_display.clear()
    def on_exit(self):
        QApplication.quit()
    def on_send(self):
        user_text = self.input_box.text().strip()
        if user_text:
            self.append_chat(f"[You] {user_text}")
            self.input_box.clear()
            # Placeholder for Riley's response
            self.append_chat("[Riley] ...thinking...")
    def append_chat(self, text):
        self.chat_display.append(text)

def main():
    app = QApplication([])
    window = RileyMainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()