# Destination City

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        outgoing_cities = set()
        destination_city = ""

        # Store all outgoing cities in a set
        for path in paths:
            outgoing_cities.add(path[0])

        # Find the destination city
        for path in paths:
            if path[1] not in outgoing_cities:
                destination_city = path[1]
                break

        return destination_city

# Test the function
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
s = Solution()
result = s.destCity(paths)
print(result)