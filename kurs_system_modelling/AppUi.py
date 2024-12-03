import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from params import SIMULATIONS_COUNT

from DistributedSystem import DistributedSystem
from GenerateStatistic import GenerateStatistic


class GUI:
    def __init__(self, master):
        self.master = master
        self.system = None
        self.master.title("Моделирование распределенной системы")
        self.master.geometry("1200x900")

        self.simulations_count = SIMULATIONS_COUNT

        # Элементы интерфейса
        self.label = tk.Label(master, text="Моделирование распределенной системы", font=("Arial", 16))
        self.label.pack(pady=10)

        self.run_button = ttk.Button(
            master, text=f"Запустить моделирование ({self.simulations_count} симуляций(я))", command=self.run_simulation
        )
        self.run_button.pack(pady=10)

        self.analysis_res_text = None

        # Область для отображения графика
        self.canvas = None

        # Перехват события закрытия окна
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.simulations_statistic = []

    def on_closing(self):
        """Корректное завершение программы при закрытии окна."""
        self.master.destroy()
        exit()

    def clear_window(self):
        if self.analysis_res_text is not None:
            self.analysis_res_text.destroy()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

    def run_simulation(self):
        self.simulations_statistic = []

        for _ in range(self.simulations_count):
            self.system = DistributedSystem()
            self.system.mainloop()

            generatedStatistic = self.system.generate_statistics()
            analysis_result = generatedStatistic.analyze_results()
            self.simulations_statistic.append(analysis_result)

        avg_values = {
            "max_len_pc1_queue": 0,
            "max_len_pc2_queue": 0,
            "pc1_completed": 0,
            "pc2_completed": 0,
            "completed_requests": [],
        }

        for simulation in self.simulations_statistic:
            for field_name, value in simulation.items():
                if field_name == "completed_requests":
                    avg_values["completed_requests"].extend(value)
                    continue

                avg_values[field_name] += value

        for field_name, value in avg_values.items():
            if field_name == "completed_requests":
                continue

            avg_values[field_name] = round(avg_values[field_name] / self.simulations_count)

        self.clear_window()

        self.show_histograms(avg_values)

    def show_histograms(self, avg_values: dict):
        self.clear_window()

        formatted_text = (
            f"Всего симуляций: {self.simulations_count}\n\n"
            f"Максимальная очередь для ПК1: {avg_values['max_len_pc1_queue']}\n"
            f"Максимальная очередь для ПК2: {avg_values['max_len_pc2_queue']}\n\n"
            f"Заявки, завершенные ПК1: {avg_values['pc1_completed']}\n"
            f"Заявки, завершенные ПК2: {avg_values['pc2_completed']}\n"
        )

        self.analysis_res_text = ttk.Label(self.master, text=formatted_text)
        self.analysis_res_text.pack(pady=10)

        # Строим и показываем график
        fig = GenerateStatistic.plot_distribution_function(avg_values)
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
