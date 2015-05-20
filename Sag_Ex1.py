from nodebox.graphics import *
from nodebox.graphics.physics import Node, Edge, Graph
import random
class GUI():
    
    """Draw and interact with the damn thing. 
    """
    def __init__(self):
        """rawgraph is an instance of the RawGraph class
        The GUI allows to interact with it, i.e. view it and change it. 
        """
        #Layer.__init__(self) # unknown thing, might be necessary.
        #Buttons
        self.EXPLORE_F = "Explore Further"
        self.EXPLORE_D = "Explore Deeper"
        self.DELETE = "Delete"
        self.CLOSE = "CLOSE"
        self.BUTTONS = False #Are buttons showing?
        self.CBUTTON = False #Is Close button showing?


        self.nodes = []


        self.g = Graph()
        self.dragged =None
        self.clicked = None



    def add_node(self, name, root = False):
        self.nodes.append(name)
        self.g.add_node(id=name, radius = 5, root = root)


    def add_edge(self,n1,n2,*args,**kwargs):
        self.g.add_edge(n1, n2, *args,**kwargs)


    def explore_further(self,node_name):
        """action of explore further button
        """
        pass
    def explore_deeper(self,node_name):
        """action of explore deeper button
        """
        pass
    def delete_node(self,node_name):
        """action of delete button
        """
        pass

    def close_canvas(self):
        """Close the canvas
        """
        canvas.clear()
        canvas.stop()

    def add_close(self):
        """Add close button
        """
        self.g.add_node(self.CLOSE, radius = 10, fill=(1,0,0,0.2))
        self.g.add_edge(self.rawg.root, self.CLOSE, length=0.6)
        self.CBUTTON=True

    def remove_close(self):
        """Remove the close button 
        """
        try:
            self.g.remove(self.g.node(self.CLOSE))

        except:
            pass
        self.CBUTTON=False

    def add_buttons(self,node_name):
        """Add the buttons to change the graph
        """
        self.g.add_node(self.EXPLORE_F, radius = 6, fill=(0,1,0,0.5))
        self.g.add_node(self.EXPLORE_D, radius = 6, fill=(0,0,1,0.5))
        self.g.add_node(self.DELETE,radius=6, fill=(1,0,0,0.5))
        self.g.add_edge(node_name, self.EXPLORE_F, length=0.2)
        self.g.add_edge(node_name, self.EXPLORE_D, length=0.2)
        self.g.add_edge(node_name, self.DELETE, length=0.2)
        self.BUTTONS = True

    def remove_buttons(self):
        """Remove the buttons to change the graph
        """
        try:
            self.g.remove(self.g.node(self.DELETE))
            self.g.remove(self.g.node(self.EXPLORE_D))
            self.g.remove(self.g.node(self.EXPLORE_F))
        except:
            pass
        self.BUTTONS=False


    def draw(self):

        canvas.clear()
        background(1)
        translate(500, 500)

        # With directed=True, edges have an arrowhead indicating the direction of the connection.
        # With weighted=True, Node.centrality is indicated by a shadow under high-traffic nodes.
        # With weighted=0.0-1.0, indicates nodes whose centrality > the given threshold.
        # This requires some extra calculations.
        self.g.draw(weighted=0.5, directed=False)
        self.g.update(iterations=10)

        # Make it interactive!
        # When the mouse is pressed, remember on which node.
        # Drag this node around when the mouse is moved.
        dx = canvas.mouse.x - 500 # Undo translate().
        dy = canvas.mouse.y - 500
        #global dragged
        if canvas.mouse.pressed and not self.dragged:
            self.dragged = self.g.node_at(dx, dy)
            old_clicked = self.clicked
            try:
                self.clicked = self.dragged.id
            except: 
                self.clicked = None


            if self.clicked != None:   
                if self.clicked == self.DELETE:
                    if old_clicked != None:
                        self.delete_node(old_clicked)
                        self.remove_buttons()
                elif self.clicked == self.EXPLORE_D:
                    if old_clicked != None:
                        self.explore_deeper(old_clicked)
                        self.remove_buttons()
                elif self.clicked == self.EXPLORE_F:
                    if old_clicked != None:
                        self.explore_further(old_clicked)
                        self.remove_buttons()
                elif self.clicked == self.CLOSE:
                    self.remove_buttons()
                    self.remove_close()
                    self.close_canvas()
                else:
                    self.remove_buttons()
                    self.remove_close()
                    self.add_buttons(self.clicked)

            else:
                if self.BUTTONS:
                    self.remove_buttons()
                elif self.CBUTTON:
                    self.remove_close()
                else:
                    self.remove_buttons()
                    self.add_close()



        if not canvas.mouse.pressed:
            self.dragged = None
        if self.dragged:
            self.dragged.x = dx
            self.dragged.y = dy


    def start(self, distance = 30, force = 0.01, repulsion_radius=30):
        """Starts the GUI
        """
        #self.g.prune(depth=0)          # Remove orphaned nodes with no connections.
        self.g.distance         = distance   # Overall spacing between nodes.
        self.g.layout.force     = force # Strength of the attractive & repulsive force.
        self.g.layout.repulsion = repulsion_radius   # Repulsion radius.
        canvas.draw = self.draw
        #canvas.size = 1000, 700
        canvas.fullscreen = True
        canvas.run()

if __name__ == '__main__':
    gui = GUI()
    Nlist = [x for x in range(200)]
    for i in range(len(Nlist)):
        gui.add_node(i)
        gui.add_edge(i,random.randrange(5))
    #gui.add_node("a")
    #gui.add_node("b")
    #gui.add_edge("a","b")

    gui.start(distance=10, repulsion_radius=30)
