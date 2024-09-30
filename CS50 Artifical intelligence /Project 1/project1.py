import csv
from collections import deque

# Data structures to store information from the CSV files
names = {}  # Maps names to a set of corresponding ids
people = {}  # Maps person_id to a dictionary of: name, birth, movies (a set of movie_ids)
movies = {}  # Maps movie_id to a dictionary of: title, year, stars (a set of person_ids)


# Implementing the shortest path function, Disjktras Algorithm

def shortest_path(source, target):
    """
    Returns the shortest path from source to target using BFS.
    If no possible path, return None.
    """
    # Initialize frontier with the starting node
    start = (None, source)  # (movie_id, person_id)
    frontier = deque([start])
    explored = set()

    # BFS search
    while frontier:
        current_movie, current_person = frontier.popleft()

        # If we found the target, reconstruct the path
        if current_person == target:
            path = []
            while current_movie and current_person:
                path.append((current_movie, current_person))
                current_movie, current_person = explored[current_person]
            path.reverse()
            return path

        # Mark this person as explored
        explored.add(current_person)

        # Add neighbors to frontier
        for movie_id, person_id in neighbors_for_person(current_person):
            if person_id not in explored:
                frontier.append((movie_id, person_id))
                explored.add((current_movie, current_person))  # Track the path

    # If no path is found, return None
    return None


