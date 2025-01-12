import networkx as nx
import matplotlib.pyplot as plt

filename = 'busroutes.txt'
data = []
route = None

with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line.startswith('#'):
            route = line[2:].strip()
        elif line.startswith('- [ ]') and route:
            company = line[5:].strip()
            data.append((route, company))
#Representing a Bipartite graph
B = nx.Graph()

routes = {route for route, company in data}
companies = {company for route, company in data}

B.add_nodes_from(routes, bipartite=0)
B.add_nodes_from(companies, bipartite=1)

B.add_edges_from(data)

plt.figure(figsize=(15, 10))
pos = nx.bipartite_layout(B, nodes=routes)

node_colors = ["lightblue" if node in routes else "lightgreen" for node in B.nodes()]
nx.draw_networkx_nodes(B, pos, node_color=node_colors, node_size=1000)
nx.draw_networkx_edges(B, pos, edge_color="gray", width=1, alpha=0.7)
nx.draw_networkx_labels(B, pos, font_size=10, font_weight="bold")
plt.title("Bipartite Graph of Bus Routes and Companies", fontsize=14)
plt.show()

#Creating one mode graph
company_graph = nx.Graph()
for route in routes:
    companies_on_route = [company for r, company in data if route == r]
    for i in range(len(companies_on_route)):
        for j in range(i + 1, len(companies_on_route)):
            company1, company2 = companies_on_route[i], companies_on_route[j]
            if company_graph.has_edge(company1, company2):
                company_graph[company1][company2]['weight'] += 1
            else:
                company_graph.add_edge(company1, company2, weight=1)

pos = nx.spring_layout(company_graph)

plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(company_graph, pos, node_color="lightgreen", node_size=3000)

edges = company_graph.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]
nx.draw_networkx_edges(company_graph, pos, edge_color="gray", width=2, alpha=0.7)

nx.draw_networkx_labels(company_graph, pos, font_size=10, font_weight="bold")

edge_labels = nx.get_edge_attributes(company_graph, 'weight')
nx.draw_networkx_edge_labels(company_graph, pos, edge_labels=edge_labels)

plt.title("Projected Graph of Bus Companies", fontsize=14)
plt.show()


def degree_centrality(graph, top_n=10):
    centralities = nx.degree_centrality(graph)
    top_centralities = sorted(centralities.items(), key=lambda item: item[1], reverse=True)[:top_n]
    return top_centralities
top_deg_companies = top_degree_centrality(company_graph, 10)
print("Top 10 companies with highest degree centrality:")
for company, centrality in top_deg_companies:
    print(f"{company}: {centrality}")


def betweenness_centrality(graph, top_n):
    centralities = nx.betweenness_centrality(graph)
    top_centralities = sorted(centralities.items(), key=lambda item: item[1], reverse=True)[:top_n]
    return top_centralities
top_bet_companies = betweenness_centrality(company_graph, 10)
print("Top 10 companies with highest betweenness centrality:")
for company, centrality in top_bet_companies:
    print(f"{company}: {centrality}")

def closeness_centrality(graph, top_n):
    centralities = nx.closeness_centrality(graph)
    top_centralities = sorted(centralities.items(), key=lambda item: item[1], reverse=True)[:top_n]
    return top_centralities
top_clos_companies = closeness_centrality(company_graph, 10)
print("Top 10 companies with highest closeness centrality:")
for company, centrality in top_bet_companies:
    print(f"{company}: {centrality}")

def density(graph):
    density = nx.density(graph)
    return density
print(f'The network density is {density(company_graph)}')

def average_path_length(graph):
    average_path_length = nx.average_shortest_path_length(graph)
    return average_path_length
print(f'The network average path length is {average_path_length(company_graph)}')
print(len(nx.nodes(company_graph)))
print(nx.degree_centrality(company_graph))
