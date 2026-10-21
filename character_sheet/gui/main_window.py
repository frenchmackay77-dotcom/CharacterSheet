import ttkbootstrap as ttk


class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")

        self.title("Character Sheet")
        self.geometry("1200x800")

        ttk.Label(
            self,
            text="Character Sheet",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=20)