"""
    a crash course in tkinter widgets.
    created with the tutorial at: https://tkdocs.com/tutorial/firstexample.html
"""

from tkinter import *
from tkinter import ttk


class FeetToMeters():

    def __init__(self, root):
        root.title("Feet to Meters")

        # create a content frame.
        main_frame = ttk.Frame(root, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # create the entry widget.
        self.feet = StringVar()
        feet_entry = ttk.Entry(main_frame, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        # create the remaining widgets.
        self.meters = StringVar()
        ttk.Label(main_frame, textvariable=self.meters).grid(column=2,
                                                             row=2,
                                                             sticky=(W, E))

        ttk.Button(main_frame, text="Calculate",
                   command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(main_frame, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(main_frame, text="is equivalent to").grid(column=1,
                                                            row=2,
                                                            sticky=E)
        ttk.Label(main_frame, text="meters").grid(column=3, row=2, sticky=W)

        # add some polish.
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    # perform the feet to meters calculation.
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except:
            pass


# setup main app window.
root = Tk()
FeetToMeters(root)

# start the event loop.
root.mainloop()