import processor
import visualizer


FILENAME = './dataset/movie_actors.net'

def pipeline():
    graph = processor.get_graph_by_file(FILENAME)
    graph_positions = processor.get_graph_geometries(graph)
    edge_trace = visualizer.get_edge_trace(graph, graph_positions)
    node_labels = visualizer.get_node_labels(graph)
    _node_trace = visualizer.get_node_trace(graph, graph_positions)
    node_trace = visualizer.render_node_trace(graph, _node_trace, node_labels)
    graph_view = visualizer.visualizer_graph(edge_trace, node_trace)
    visualizer.save_html_visualizer(graph_view, FILENAME)


pipeline()
