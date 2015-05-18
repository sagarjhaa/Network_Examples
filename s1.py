import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import Tkinter as Tk
import networkx as nx
from tkMessageBox import showinfo

root = Tk.Tk()
root.wm_title("Animated Graph embedded in TK")
root.wm_protocol('WM_DELETE_WINDOW', root.quit())

f = plt.figure(figsize=(5,4))
a = f.add_subplot(111)
plt.axis('off')

# the networkx part
##G=nx.complete_graph(5)
##pos=nx.circular_layout(G)
##nx.draw_networkx(G,pos=pos,ax=a)


G=nx.star_graph(50)
pos=nx.spring_layout(G)
colors=range(50)
nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)

xlim=a.get_xlim()
ylim=a.get_ylim()


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()

canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)
##def next_graph():
##    if G.order():
##        a.cla()
##        G.remove_node(G.nodes()[-1])
##        nx.draw_networkx(G, pos, ax=a)
##        a.set_xlim(xlim)
##        a.set_ylim(ylim)
##        plt.axis('off')
##        canvas.draw()
##
##b = Tk.Button(root, text="next",command=next_graph)
##b.pack()

Tk.mainloop()
