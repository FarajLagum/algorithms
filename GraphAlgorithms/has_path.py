# Path finding: is there a path from the source " " to the destination " "


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}  # asyclic directed graph


#

def has_path(graph, src, dest):
    if src == dest:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest):
            return True
    return False


if __name__ == "__main__":
    flag = has_path(graph, "f", "k")
    print(flag)
