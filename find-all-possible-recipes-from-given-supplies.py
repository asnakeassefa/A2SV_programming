class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        store = defaultdict(int)
        setedRecipes = set(recipes)
        supplies = set(supplies)
        for wanted in recipes:
            store[wanted] = 0
        
        for i,ingredient in enumerate(ingredients):
            for product in ingredient:
                if product in setedRecipes:
                    graph[product].append(recipes[i])
                    store[recipes[i]] += 1
                if product not in supplies and product not in setedRecipes:
                    store[recipes[i]] -= 200
        queue = deque()
        for key,val in store.items():
            if val == 0:
                queue.append(key)
        
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for recipe in graph[node]:
                store[recipe] -= 1
                if store[recipe] == 0:
                    queue.append(recipe)
        return ans