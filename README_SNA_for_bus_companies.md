# Social Network Analysis of Intercity Bus Companies in Turkey

A university project applying **Social Network Analysis (SNA)** to explore relationships between intercity bus companies operating across eight major metropolitan cities in Turkey.

The project models how bus companies are connected through shared routes and uses network analysis metrics to investigate route coverage, connectivity, and the structural position of companies within the transportation network.

## 🎯 Research Questions

This project investigates three main questions:

1. **Route coverage:** Which bus company operates across the greatest number of routes among the eight selected metropolitan cities?
2. **Network dominance:** What factors may explain the prominence of the most route-connected company, and how does its position relate to the rest of the network?
3. **Network access:** Which bus company has the greatest access to other companies in the network, and what does its position reveal about its connectivity?

## 🗺️ Study Scope

The dataset covers **215 registered intercity bus companies** and routes connecting eight metropolitan cities in Turkey:

- İstanbul
- Ankara
- İzmir
- Adana
- Konya
- Bursa
- Gaziantep
- Kayseri

### Network entities

- **Companies:** Intercity bus operators included in the dataset.
- **Routes:** Connections between the selected cities.

### Relationship definition

Two bus companies are connected when they operate on the same route. The relationship weight reflects the frequency with which they share routes or operations, as represented in the available dataset.

This approach makes it possible to study the structure of the intercity bus-company network rather than analyzing each operator in isolation.

## 🧠 Methodology

### 1. Bipartite Network Modeling

A bipartite graph represents the relationships between bus companies and routes. One node set represents companies, while the other represents routes. An edge indicates that a company operates on a particular route.

### 2. One-Mode Network Projection

The bipartite graph is projected onto a company-only network. In this projection, companies are connected when they share routes. Edge weights can represent the extent of route overlap, depending on how the source data encodes shared operations.

### 3. Network Visualization

Network graphs are created with **NetworkX** and visualized using **Matplotlib** to make patterns of connectivity and company positioning easier to examine.

### 4. Network Analysis Metrics

The project applies centrality measures and whole-network metrics:

| Metric | What it helps investigate |
|---|---|
| Degree centrality | How directly connected a company is to other companies in the projected network |
| Betweenness centrality | How often a company lies on shortest paths between other companies, indicating a potential bridging position |
| Closeness centrality | How near a company is to other reachable companies in terms of shortest-path distance |
| Network density | The proportion of possible connections that are present in the network |
| Average path length | The average shortest-path distance between reachable node pairs |

These metrics provide complementary perspectives on company connectivity and network structure. They should be interpreted in the context of the network construction and edge-weight definitions.

## 🛠️ Technologies

- **Python**
- **NetworkX** — graph construction, projection, and network metrics
- **Matplotlib** — network visualization

## 📁 Repository

The repository contains the project materials in the `SNA for bus companies` directory, along with this README.

## 🚀 Getting Started

The analysis is implemented in Python. To explore or reproduce it, clone the repository and inspect the project files:

```bash
git clone https://github.com/nigina254/SNA-for-bus-companies-in-Turkey.git
cd SNA-for-bus-companies-in-Turkey
```

Install the main Python libraries in your environment if they are not already available:

```bash
python -m pip install networkx matplotlib
```

Then open and run the analysis files in the project directory using the Python environment appropriate to those files. Input-data paths and any additional dependencies may need to be configured according to the project files.

## 📌 Interpretation and Limitations

- The analysis reflects the companies, routes, cities, and time period represented in the dataset.
- Shared routes are used as a proxy for relationships between companies; they do not necessarily imply formal partnerships or business cooperation.
- Centrality scores depend on how the graph is constructed, including whether it is directed or undirected and how edge weights are defined.
- Network position alone does not establish why a company is popular or prove that network dominance causes particular market outcomes.
- Findings should be interpreted as structural observations about the modeled network, not as a complete assessment of the Turkish intercity transportation market.

## 👥 Authors

- **Nigina Abdukhalimova** — [@nigina254](https://github.com/nigina254)
- **Gülsah Atıcı** — [@gulsahatici](https://github.com/gulsahatici)

## 📚 Project Context

Developed as a university project for a **Social Network Analysis** course.
