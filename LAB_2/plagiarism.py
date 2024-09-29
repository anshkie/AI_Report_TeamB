import heapq
import numpy as np
import string

def edit_distance(s1, s2):
    """Compute the edit distance between two strings."""
    m, n = len(s1), len(s2)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def preprocess_text(doc):
    """Tokenize and normalize the document."""
    # Convert to lowercase and remove punctuation
    doc = doc.lower().translate(str.maketrans('', '', string.punctuation))
    # Treat the entire document as one string (since we're working on single strings for alignment)
    return doc

class State:
    def __init__(self, idx1, idx2, accumulated_cost, doc1, doc2):
        self.idx1 = idx1  # Current index in document 1
        self.idx2 = idx2  # Current index in document 2
        self.accumulated_cost = accumulated_cost
        self.doc1 = doc1
        self.doc2 = doc2
    
    def __lt__(self, other):
        return (self.accumulated_cost + self.heuristic()) < (other.accumulated_cost + other.heuristic())

    def heuristic(self):
        """Estimate the remaining cost (heuristic)."""
        # Simple heuristic: Difference in the number of remaining characters
        return abs(len(self.doc1) - self.idx1 - (len(self.doc2) - self.idx2))

def a_star_search(doc1, doc2):
    """Perform A* search to align characters of two strings."""
    start_state = State(0, 0, 0, doc1, doc2)
    open_set = []
    heapq.heappush(open_set, start_state)
    visited = set()
    
    while open_set:
        current_state = heapq.heappop(open_set)
        
        if (current_state.idx1, current_state.idx2) in visited:
            continue
        
        visited.add((current_state.idx1, current_state.idx2))
        
        # Check if goal state is reached (both indices have reached the end of both strings)
        if current_state.idx1 == len(doc1) and current_state.idx2 == len(doc2):
            return current_state.accumulated_cost
        
        # Generate successors
        if current_state.idx1 < len(doc1) and current_state.idx2 < len(doc2):
            # Align characters
            cost = 0 if doc1[current_state.idx1] == doc2[current_state.idx2] else 1
            new_state = State(current_state.idx1 + 1, current_state.idx2 + 1, current_state.accumulated_cost + cost, doc1, doc2)
            if (new_state.idx1, new_state.idx2) not in visited:
                heapq.heappush(open_set, new_state)
        
        if current_state.idx1 < len(doc1):
            # Skip character in doc2
            new_state = State(current_state.idx1 + 1, current_state.idx2, current_state.accumulated_cost + 1, doc1, doc2)
            if (new_state.idx1, new_state.idx2) not in visited:
                heapq.heappush(open_set, new_state)
        
        if current_state.idx2 < len(doc2):
            # Skip character in doc1
            new_state = State(current_state.idx1, current_state.idx2 + 1, current_state.accumulated_cost + 1, doc1, doc2)
            if (new_state.idx1, new_state.idx2) not in visited:
                heapq.heappush(open_set, new_state)

    return None

def detect_plagiarism(doc1, doc2):
    """Detect potential plagiarism by aligning two strings."""
    doc1_processed = preprocess_text(doc1)
    doc2_processed = preprocess_text(doc2)
    alignment_cost = a_star_search(doc1_processed, doc2_processed)
    
    if alignment_cost is not None:
        # The lower the alignment cost, the more similar the documents are
        print(f"Potential plagiarism detected with total alignment cost: {alignment_cost}")
    else:
        print("No potential plagiarism detected.")
        
# Example test cases
# doc1 = "remove him. he is not hardworking."
# doc2 = "remove him. he is not hardworking." 

# Example test cases
# doc1 = "replace him. he is hardworking."
# doc2 = "replace him. he is more hardworking."

# doc1 = "remove him. he is not hardworking."
# doc2 = "python is better. From my opinion c is the best."

doc1 = "I am student at IIITV. I am in 3rd year"
doc2 = "You are student at IIITV. You are in 3rd year"


print("doc1 : " + doc1)
print("doc2 : " + doc2)
detect_plagiarism(doc1, doc2)