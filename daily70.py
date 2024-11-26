class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Count incoming edges for each node
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1
        
        # Find champions (nodes with no incoming edges)
        champions = []
        for i, incoming_cnt in enumerate(incoming):
            if incoming_cnt == 0:
                champions.append(i)

        # Return champion if unique, otherwise return -1
        return champions[0] if len(champions) == 1 else -1


# Problem Description:
        # - You have n teams in a tournament, numbered from 0 to n-1
        # - The tournament is represented as a Directed Acyclic Graph (DAG)
        # - Each edge [ui, vi] means team ui is stronger than team vi
        
        # Goal: Find the champion team
        # Champion criteria:
        # - No other team is stronger than this team
        # - If multiple or no champions exist, return -1
        
        # Strategy: Count incoming edges for each team
        # - A champion will have 0 incoming edges (no team is stronger than it)
        
        # Initialize an array to track incoming edges for each team
