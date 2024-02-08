import tkinter as tk

class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)


class Paint():

    canvas_height = 720
    canvas_width = 1080

    def __init__(self):
        self._window = tk.Tk()
        self._window.title("Paint")
        self._window.geometry("1280x720")
        self._window.resizable(False, False)

        # define variables
        self._colours = ['red', 'blue', 'yellow']
        self._selected_colour = self._colours[0]

        self._shapes = ['line', 'oval', 'rectangle']
        self._selected_shape = self._shapes[0]

        self._top_left = None
        self._bottom_right = None

        self._window.columnconfigure(0, weight=1)
        self._window.rowconfigure(1, weight=1)

        # create frames
        self._tool_bar_frame = tk.Frame(self._window, width=300, bg="gray")
        self._tool_bar_frame.grid(row=0, column=0, sticky="nsew", ipadx=10, ipady=10)

        self._canvas_frame = tk.Frame(self._window, bg="white")
        self._canvas_frame.grid(row=0, column=1, sticky="nsew")

        #tool bar widgets
        self._shape_label = tk.Label(self._tool_bar_frame, text="Shape", bg="gray")

        self._shape = tk.StringVar()   
        self._shape.set(self._shapes[0])
        self._shape_menu = tk.OptionMenu(self._tool_bar_frame, self._shape, *self._shapes, command=self.change_shape)
        self._shape_menu.config(bg="gray")
        self._shape_menu["menu"].config(bg="gray")

        self._colour_label = tk.Label(self._tool_bar_frame, text="Colour", bg="gray")

        self._colour = tk.StringVar()
        self._colour.set(self._colours[0])
        self._colour_menu = tk.OptionMenu(self._tool_bar_frame, self._colour, *self._colours, command=self.change_colour)
        self._colour_menu.config(bg="gray")
        self._colour_menu["menu"].config(bg="gray")

        self._top_left_label = tk.Label(self._tool_bar_frame, text="Top Left:", bg="gray")
        self._bottom_right_label = tk.Label(self._tool_bar_frame, text="Bottom Right:", bg="gray")

        self._top_left_value = tk.StringVar()
        self._top_left_value.set("None")

        self._bottom_right_value = tk.StringVar()
        self._bottom_right_value.set("None")

        self._top_left_value_label = tk.Label(self._tool_bar_frame, textvariable=self._top_left_value, bg="gray")
        self._bottom_right_value_label = tk.Label(self._tool_bar_frame, textvariable=self._bottom_right_value, bg="gray")

        # canvas widgets
        self._canvas = tk.Canvas(self._canvas_frame, width=self.canvas_width, height=self.canvas_height)
        self._canvas.bind("<Button-1>", self.mouse_down)

        # setup grid
        self._shape_label.grid(row=0, column=0)
        self._shape_menu.grid(row=0, column=1)
        self._colour_label.grid(row=1, column=0)
        self._colour_menu.grid(row=1, column=1)
        self._top_left_label.grid(row=2, column=0)
        self._top_left_value_label.grid(row=2, column=1)
        self._bottom_right_label.grid(row=3, column=0)
        self._bottom_right_value_label.grid(row=3, column=1)
        self._canvas.grid(row=0, column=0)

        tk.mainloop()

    def mouse_down(self, event):
        if not self._top_left and not self._bottom_right:
            self._top_left = Point(event.x, event.y)
            self._top_left_value.set("x: " + str(self._top_left.x) + " y: " + str(self._top_left.y))
            self._bottom_right_value.set("None")
        elif self._top_left and not self._bottom_right:
            self._bottom_right = Point(event.x, event.y)
            self._bottom_right_value.set("x: " + str(self._bottom_right.x) + " y: " + str(self._bottom_right.y))
            self.draw()

    def change_shape(self, shape):
        self._selected_shape = shape

    def change_colour(self, colour):
        self._selected_colour = colour

    def draw_oval(self):
        self._canvas.create_oval(self._top_left.x, self._top_left.y, self._bottom_right.x, self._bottom_right.y, fill=self._selected_colour)

    def draw_line(self):
        self._canvas.create_line(self._top_left.x, self._top_left.y, self._bottom_right.x, self._bottom_right.y, fill=self._selected_colour)

    def draw_rectangle(self):
        self._canvas.create_rectangle(self._top_left.x, self._top_left.y, self._bottom_right.x, self._bottom_right.y, fill=self._selected_colour)

    def draw(self):
        if self._top_left and self._bottom_right:
            if self._selected_shape == 'line':
                self.draw_line()
            elif self._selected_shape == 'oval':
                self.draw_oval()
            elif self._selected_shape == 'rectangle':
                self.draw_rectangle()
            else:
                raise ValueError("Invalid shape")

            self._top_left = None
            self._bottom_right = None
        else:
            raise ValueError("Not all points selected")
        
Paint()