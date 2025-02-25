class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        DEBUG = True
        tree = {}
        directed_tree_downwards = {}
        directed_tree_upwards = {}

        for j, i in edges:
            if i in tree:
                tree[i].append(j)
            else:
                tree[i] = [j]
            if j in tree:
                tree[j].append(i)
            else:
                tree[j] = [i]
        
        dq = deque()
        dq.append(0)
        while dq:
            node = dq.popleft()
            for i in tree[node]:
                if i not in directed_tree_downwards:
                    if node not in directed_tree_downwards:
                        directed_tree_downwards[node] = [i]
                    else:
                        directed_tree_downwards[node].append(i)
                    dq.append(i)
        
        for i in directed_tree_downwards:
            for j in directed_tree_downwards[i]:
                    directed_tree_upwards[j] = i
        
        bob_path = {}
        curr = bob
        bob_step = 0
        while curr != 0:
            bob_path[curr] = bob_step
            bob_step += 1
            curr = directed_tree_upwards[curr]
        bob_path[0] = bob_step
                
        directed_tree_upwards[0] = 0
        if DEBUG:
            print(directed_tree_downwards)
            for i in range(len(amount)):
                print(i, " => ", amount[i])
        def helper(alice: int, alice_inc: int, bob: int, step: int):
            if alice not in directed_tree_downwards:
                if alice not in bob_path:
                    if DEBUG:
                        print(alice, " : ", alice_inc + amount[alice], " : ", bob, "returned_unvisited")
                    return alice_inc + amount[alice]
                else:
                    if DEBUG:
                        print(alice, " : ", alice_inc, " : ", bob, "returned")
                    return alice_inc
            elif alice == bob:
                alice_inc += amount[alice]/2
            elif alice not in bob_path:
                alice_inc += amount[alice]
            elif alice in bob_path:
                if step < bob_path[alice]:
                    alice_inc += amount[alice]
            if DEBUG:
                print(alice, " : ", alice_inc, " : ", bob)
            return max((helper(i, alice_inc, directed_tree_upwards[bob], step + 1) for i in directed_tree_downwards[alice]))
        return int(helper(0, 0, bob, 0))
            
