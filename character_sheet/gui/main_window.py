import ttkbootstrap as ttk

from character_sheet.models.character import Character


class MainWindow(ttk.Window):

    def __init__(self):
        super().__init__(themename="darkly")

        self.title("Character Sheet")
        self.geometry("1200x800")

        self.character = Character()

        ttk.Label(
            self,
            text=self.character.name,
            font=("Segoe UI", 24, "bold")
        ).pack(pady=20)

        ttk.Label(
            self,
            text=f"Level {self.character.level}"
        ).pack()