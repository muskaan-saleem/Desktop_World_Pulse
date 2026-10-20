from __future__ import annotations

import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .data import PublicDataClient


class Page(QWidget):
    """Base page that provides a consistent title and description."""

    def __init__(self, title: str, description: str) -> None:
        super().__init__()
        layout = QVBoxLayout(self)
        heading = QLabel(title)
        heading.setStyleSheet("font-size: 24px; font-weight: bold;")
        copy = QLabel(description)
        copy.setWordWrap(True)
        layout.addWidget(heading)
        layout.addWidget(copy)
        layout.addStretch()


class OverviewPage(Page):
    def __init__(self, client: PublicDataClient) -> None:
        super().__init__(
            "Overview",
            "Your global intelligence workspace starts here.",
        )
        self.client = client


class CountriesPage(Page):
    def __init__(self, client: PublicDataClient) -> None:
        super().__init__(
            "Countries",
            "Search and explore countries from one workspace.",
        )
        self.client = client


class MarketsPage(Page):
    def __init__(self, client: PublicDataClient) -> None:
        super().__init__(
            "Markets",
            "View exchange rates, metals, fuel, and market freshness.",
        )
        self.client = client


class SettingsPage(Page):
    def __init__(self, client: PublicDataClient) -> None:
        super().__init__(
            "Settings",
            "Configure location, currency, and provider preferences.",
        )
        self.client = client


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("World Pulse")
        self.resize(1200, 760)

        self.client = PublicDataClient()
        self.navigation = QListWidget()
        self.pages = QStackedWidget()

        page_definitions = [
            ("Overview", OverviewPage(self.client)),
            ("Countries", CountriesPage(self.client)),
            ("Markets", MarketsPage(self.client)),
            ("Settings", SettingsPage(self.client)),
        ]

        for name, page in page_definitions:
            self.navigation.addItem(name)
            self.pages.addWidget(page)

        self.navigation.setAccessibleName("Main navigation")
        self.navigation.setMinimumWidth(180)
        self.navigation.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.navigation.setCurrentRow(0)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)

        title = QLabel("WORLD PULSE")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(self.navigation)
        content_layout.addWidget(self.pages, 1)
        layout.addWidget(content, 1)

        self.setCentralWidget(central)


def run() -> None:
    application = QApplication.instance() or QApplication(sys.argv)
    application.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(application.exec())
