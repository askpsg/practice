class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        num_of_fruits = len(fruits)
        if num_of_fruits <= 2:
            return num_of_fruits
        
        valid_trees = {}
        st, en = 0, 0
        max_size_valid = 0
        while en < num_of_fruits:
            current_tree = fruits[en]
            if current_tree not in valid_trees:
                if len(valid_trees) == 2:
                    max_size_valid = max(max_size_valid, en - st)
                    while st < en:
                        remove_tree = fruits[st]
                        st += 1
                        valid_trees[remove_tree] -= 1
                        if valid_trees[remove_tree] == 0:
                            del valid_trees[remove_tree]
                            valid_trees[current_tree] = 1
                            break
                else:
                    valid_trees[current_tree] = 1
            else:
                valid_trees[current_tree] += 1
            en += 1

        return max(max_size_valid, en - st)
        