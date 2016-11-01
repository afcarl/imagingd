
from graph_tool.all import *
from CX import *

def render_from_file(filename):
  render_from_json(file(filename).read())

def render_from_json(json):
    network = Network(json)
    graph = new_graph(network)
    render(graph, 18, (200, 200), 'graph.png')

def graph_from_network(network):
  graph = Graph()
  nodes = { n.id:g.add_vertex for n in network.nodes }
  { edge.id:g.add_edge(nodes[edge.source_id], nodes[edge.target_id]) for edge in network.edges }
  return graph

def render(graph, font_size, image_size, filename):
    graph_draw(graph, vertex_text=g.vertex_index, vertex_font_size=font_size, output_size=image_size, output=filename)
