from graphviz import Digraph

dot = Digraph()
dot.node('A', 'Hello')
dot.node('B', 'World')
dot.edge('A', 'B')
dot.render('test-output', format='png', view=True)
