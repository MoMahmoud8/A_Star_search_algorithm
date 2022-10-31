

graph={
    'K' : [('T1',5),('T2',5),('T3',9)],
    'T1' : [('K',5),('T2',10),('T3',7),('T4',13)],
    'T2' : [('K',5),('T1',10),('T3',7)],
    'T3' : [('K',9),('T1',7),('T2',7),('T4',14)],
    'T4' : [('T1',13),('T3',14)]

}

H_table={
    'T1' : 17,
    'T2' : 13,
    'T3' : 15,
    'K' : 18,
    'T4' : 0
}

def path_f_cost(path):
    g_cost=0
    for(node,cost) in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=H_table[last_node]
    f_cost=g_cost+h_cost
    return f_cost,last_node


def a_star_search(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost) #sorting by f-cost
        path=queue.pop(0) #choosing least f-cost
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node ==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)    

solution=a_star_search(graph,'K','T4')
print("solution is-->",solution)
print("cost of solution is-->",path_f_cost(solution)[0])