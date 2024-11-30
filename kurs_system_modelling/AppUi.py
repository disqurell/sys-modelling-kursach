import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from DistributedSystem import DistributedSystem


class GUI:
    def __init__(self, master):
        self.master = master
        self.system = None
        self.master.title("Моделирование распределенной системы")
        self.master.geometry("1200x900")

        # Элементы интерфейса
        self.label = tk.Label(master, text="Моделирование распределенной системы", font=("Arial", 16))
        self.label.pack(pady=10)

        self.run_button = ttk.Button(master, text="Запустить моделирование", command=self.run_simulation)
        self.run_button.pack(pady=10)

        self.analysis_res_text = None

        # Область для отображения графика
        self.canvas = None

        # Перехват события закрытия окна
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """Корректное завершение программы при закрытии окна."""
        # if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        self.master.destroy()
        exit()

    def clear_window(self):
        if self.analysis_res_text is not None:
            self.analysis_res_text.destroy()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

    def run_simulation(self):
        self.system = DistributedSystem()
        self.system.mainloop()

        self.clear_window()

        self.show_histograms()

    def show_histograms(self):
        self.clear_window()
        # Получаем статистику
        statistics = self.system.generate_statistics()

        # Показываем анализ результатов
        analysis_result = statistics.analyze_results()

        self.analysis_res_text = ttk.Label(self.master, text=analysis_result)
        self.analysis_res_text.pack(pady=10)

        # Строим и показываем график
        fig = statistics.plot_distribution_function()
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
