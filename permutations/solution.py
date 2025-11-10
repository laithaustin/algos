# new idea: use swapping and fix the indexes as you traverse the array

def permute_word(word):

    result = []

    dfs(result, 0, word) 

    return result

    

def word_swap(word, i, j):

    ls = list(word)

    ls[i], ls[j] = ls[j], ls[i]

    return "".join(ls)



def dfs(result, current_index, word):

    if len(word) - 1 == current_index:

        result.append(word) 

        return

    

    for i in range(current_index, len(word)):

        # fix index at current char

        perm = word_swap(word, i, current_index)

        dfs(result, current_index + 1, perm)

            

# old solution: idea is just to wastefully use a set to check unique characters and then build

def permute_word_old(word):

    result = []

    dfs_old(result, "", word, set()) 

    return result



def dfs_old(result, current, word, used):

    if len(current) == len(word):

        result.append(current) 

        return

    

    for char in word:

        if char not in used:

            dfs(result, current + char, word, used | {char})
