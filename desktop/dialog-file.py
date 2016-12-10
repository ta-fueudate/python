import tkinter.filedialog as fd

path = fd.askopenfilename(
    title="set your file",
    filetypes=[('HTML','.html')])

print(path)
