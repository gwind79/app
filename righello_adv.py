import tkinter as tk

class RulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Righello Interattivo")

        # Stato dell'app
        self.orientation = 'horizontal'
        self.unit = 'pixel'
        self.length_pixels = 500

        # Canvas e bottoni
        self.canvas = tk.Canvas(root, width=310, height=60, bg="white")
        self.canvas.pack(pady=10)

        self.toggle_orientation_btn = tk.Button(root, text="Cambia Orientamento", command=self.toggle_orientation)
        self.toggle_orientation_btn.pack(pady=5)

        self.toggle_unit_btn = tk.Button(root, text="Cambia Unità (Pixel/MM)", command=self.toggle_unit)
        self.toggle_unit_btn.pack(pady=5)

        self.draw_ruler()

    def toggle_orientation(self):
        self.orientation = 'vertical' if self.orientation == 'horizontal' else 'horizontal'
        self.draw_ruler()

    def toggle_unit(self):
        self.unit = 'mm' if self.unit == 'pixel' else 'pixel'
        self.draw_ruler()

    def draw_ruler(self):
        self.canvas.delete("all")

        # Conversioni
        if self.unit == 'pixel':
            unit_label = "px"
            scale_factor = 1
            step = 10
            label_every = 50
        else:
            unit_label = "mm"
            scale_factor = 3.7795  # pixel per mm
            step = 5  # mm
            label_every = 10  # mm

        if self.orientation == 'horizontal':
            width = int(self.length_pixels + 10)
            height = 60
            self.canvas.config(width=width, height=height)

            i = 0
            while True:
                x = int(i * scale_factor) + 5
                if x > width - 10:
                    break
                height_line = 20 if i % label_every == 0 else 10
                self.canvas.create_line(x, 0, x, height_line, fill="black")
                if i % label_every == 0:
                    self.canvas.create_text(x, height_line + 10, text=f"{i} {unit_label}", anchor="n")
                i += step

        else:  # verticale
            height = int(self.length_pixels + 10)
            width = 60
            self.canvas.config(width=width, height=height)

            i = 0
            while True:
                y = int(i * scale_factor) + 5
                if y > height - 10:
                    break
                length_line = 20 if i % label_every == 0 else 10
                self.canvas.create_line(0, y, length_line, y, fill="black")
                if i % label_every == 0:
                    self.canvas.create_text(length_line + 5, y, text=f"{i} {unit_label}", anchor="w")
                i += step

if __name__ == "__main__":
    root = tk.Tk()
    app = RulerApp(root)
    root.mainloop()
