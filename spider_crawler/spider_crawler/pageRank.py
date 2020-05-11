import networkx as nx

def pageRank(jsonArray):
    G=nx.DiGraph()
    for jsonObj in jsonArray:
        G.add_node(jsonObj['url'])
    
    #print(list(G.nodes))
    
    for jsonObj in jsonArray:
        for outLink in jsonObj['out_links']:
            if G.has_node(outLink):
                G.add_edge(jsonObj['url'],outLink)
    
    #print(G.edges.data())
    #print(G.number_of_edges())
    node_score={}
    for node in G.nodes():
        node_score[node]=(1/G.number_of_nodes())

    epislon=0.85

    i=0
    while(i<50):
        for node in G.nodes():
            outer_sum=0
            for neighbor in G.predecessors(node):
                numerator=node_score[neighbor]
                denominator=len(list(G.successors(neighbor)))
                final=(numerator/denominator)
                outer_sum+=final
                
            total=(1-epislon)*outer_sum
            total+=epislon/G.number_of_nodes()
            node_score[node]=total
            #print(total)
        i+=1
    
    #print("Node scores:")
    #print(node_score)
    return node_score

