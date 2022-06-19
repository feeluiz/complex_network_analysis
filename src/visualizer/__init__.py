import plotly.graph_objects as go
import datetime


def get_edge_trace(G, positions):
    """compute edge_trace.

    @param: G: NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    @param: positions: : dict
        A dictionary of positions keyed by node
    Returns
    -------
    edge_trace : all Edges positions in plotly lib format
    """
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = positions[edge[0]]
        x1, y1 = positions[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
    return go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')


def get_node_trace(G, positions):
    """compute node_trace.

    @param: G: NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    @param: positions: : dict
        A dictionary of positions keyed by node
    Returns
    -------
    node_trace : all node positions in plotly lib format
    """
    node_x = []
    node_y = []
    node_label = []
    for node in G.nodes():
        x, y = positions[node]
        node_x.append(x)
        node_y.append(y)
        node_label.append(node)

    return go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))


def get_node_labels(G):
    """compute node_labels.

    @param: G: NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    Returns
    -------
    node_labels : all node labels in plotly lib format
    """
    node_label = []
    for node in G.nodes():
        node_label.append(node)
    return node_label


def render_node_trace(G, node_trace, node_label):
    """ render_node_trace with adjacencies count and labels be each node

    @param: G: NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    @param: node_trace : all node positions in plotly lib format
    @param: node_labels : all node labels in plotly lib format
    Returns
    -------
    node_trace : all node positions in plotly lib format with adjacencies/labels
    """
    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: ' + str(len(adjacencies[1])) + ' - ' + node_label[node])

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text
    return node_trace


def visualizer_graph(edge_trace, node_trace):
    """ generate_ploty_graph
    @param: edge_trace : all edge positions in plotly lib format
    @param: node_trace : all node positions in plotly lib format
    Returns
    -------
    return visualizer_graph
    """
    return go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
        title='Grafo de conexão de Atores',
        titlefont_size=16,
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        annotations=[dict(
            text="by Nós: <a href=''> </a>",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.005, y=-0.002)],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
    )


def save_html_visualizer(visualizer_graph, filename):
    """ save visualizer_graph to html
    @param: visualizer_graph : generated visualizer_graph
    @param: filename: the 
    void
    -------
    saves a file on output dir
    """
    visualizer_graph.write_html(
        filename +
        '_output' +
        datetime.datetime.now().strftime("%f") +
        '.html'
    )
