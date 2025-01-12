# SNA-for-bus-companies-in-Turkey
University project for Social Network Analysis subject. 


# Aim and Related Research Questions 
1. Which bus company operating in Turkey offers the highest number of routes across the eight metropolitan cities in the country?
2. Based on the findings from the previous question, what are the underlying reasons for the popularity of this bus company, and how does its dominance affect the other components depicted in the graph?
3. Which bus company within this social network has the greatest access to other bus companies, and what are the underlying reasons  behind it?

# Explain of Sample:
The sample consists of intercity bus routes and the companies operating within eight metropolitan cities of Turkey. The focus is on how these companies interact by sharing the same routes, creating a social network of transportation providers. The sample focuses on the intercity bus routes and companies operating across eight major metropolitan cities in Turkey: İstanbul, Ankara, İzmir, Adana, Konya, Bursa, Gaziantep, and Kayseri. The aim is to study the connections and relationships formed by bus companies sharing these routes.
# Subjects: 
The 215 registered intercity bus companies travelling across 8 cities and the routes between these cities.

# Relationships: 
A relationship is formed when two companies operate on the same route. The weight of the relationship depends on the frequency of shared operations on that route.

# Implementation using Networkx and Matpotlib in Python 
All the graphs of the network are created using the NetworkX library in Python. Initially, a bipartite graph is created to represent the relationship between bus routes and the bus companies operating on these routes. This graph is visualized using Matplotlib.
Next, a one-mode projected graph of bus companies is created and visualized. Various centrality measures (degree centrality, betweenness centrality, and closeness centrality) and whole-network metrics (density and average path length) are applied to analyze the network.


