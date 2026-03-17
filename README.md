# Pathwise

An interactive pathfinding algorithm visualiser built with Python and PyQt6.
Watch A*, Dijkstra, BFS and DFS explore a grid in real time — step by step.

![status](https://img.shields.io/badge/status-in%20progress-blue)
![python](https://img.shields.io/badge/python-3.14-blue)
![license](https://img.shields.io/badge/license-MIT-green)

---

## What it does

- Draw walls on a grid with your mouse
- Place a start and end node
- Pick an algorithm and watch it execute step by step
- Visited cells animate as the frontier expands
- The final path highlights in amber when found
- Speed slider and play/pause controls

---

## Algorithms

| Algorithm | Optimal? | Notes |
| --------- | -------- | ----- |
| A* | Yes | Heuristic search — fast and accurate |
| Dijkstra | Yes | Uniform cost — no heuristic |
| BFS | Yes (unweighted) | Breadth-first wave expansion |
| DFS | No | Depth-first — not for shortest path |
```