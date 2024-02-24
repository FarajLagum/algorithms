def h_index(citations):
    h_index = 0

    for paper_id, citation_count in enumerate(citations):
        print(paper_id, citation_count)
        if citation_count >= paper_id + 1:
            h_index = paper_id + 1

    return h_index


# Example usage:
citations = [1, 4, 1, 4, 2, 1, 3, 5, 6]
# citations = [6, 5, 3, 1, 0]
# citations = [0]
h_index = h_index(citations)
print(f"The researcher's h-index is: {h_index}")
