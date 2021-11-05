from graphs import GraphAdjList, randint


if __name__ == "__main__":
    times = []
    for i in range(1):
        n, m = randint(0, 10), randint(0, 30)
        graph = GraphAdjList(n, m, False)
        times.append((m,graph.generate()))
        # graph.to_img(f"graph-{i}.png", dir="images")
    


