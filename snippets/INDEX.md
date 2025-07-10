# Snippet Index

## Data Structures Snippets
### Dictionary Comprehension Guide
- **🧩 Basic dictionary comprehension**
- **🧩 From list of tuples**
- **🧩 From two lists (zip)**
- **🧩 Filter items by value**
- **🧩 Transform keys and values**
- **🧩 Conditional values**
- **🧩 Nested dictionary comprehension**
- **🧩 Flatten nested dict to single dict**
- **🧩 Enumerate with comprehension**
- **🧩 Default values with get()**
- **🧩 Comprehension with try/except (error handling)**
- **🧩 Dictionary comprehension from set**
- **🧩 Dictionary comprehension with filtering and transformation**
- **🧩 Large dict comprehensions (performance)**
- **🧩 Avoiding key collisions**
- **🧩 Edge cases: empty input, non-hashable keys**

### Dictionary with Default Values (Guide)
- **🧩 Using defaultdict for default values**
- **🧩 defaultdict with list (grouping)**
- **🧩 setdefault for default value**
- **🧩 defaultdict with custom factory**
- **🧩 defaultdict for counting (Counter)**
- **🧩 Nested defaultdict (auto-vivify)**
- **🧩 Custom dict with __missing__**
- **🧩 Handle missing keys with get()**
- **🧩 setdefault vs defaultdict**
- **🧩 Large defaultdicts (performance)**
- **🧩 Edge cases: missing keys, mutable defaults**

### Dictionary Subset Operations
- **🧩 Create subset by keys**
- **🧩 Create safe subset with defaults**
- **🧩 Filter by value type**
- **🧩 Filter by value conditions**
- **🧩 Filter by key patterns**
- **🧩 Nested dictionary subset**
- **🧩 Subset by value range**
- **🧩 Extract public data**
- **🧩 Filter sensitive data**
- **🧩 Handle empty dictionaries**
- **🧩 Performance optimization**
- **🧩 Configuration management**
- **🧩 Data analytics filtering**

### Convert Dictionary to List (Guide)
- **🧩 Get list of keys**
- **🧩 Get list of values**
- **🧩 Get list of (key, value) tuples**
- **🧩 Flatten nested dict to list of (outer, inner, value)**
- **🧩 List of keys/values/items with filtering**
- **🧩 List of sorted keys/values/items**
- **🧩 List of unique values**
- **🧩 List of keys/values/items with transformation**
- **🧩 List of dicts from list of keys/values**
- **🧩 Large dicts (performance)**
- **🧩 Edge cases: empty dict, non-hashable values**

### Group by Key (Dictionary Grouping Guide)
- **🧩 Group list of pairs by key (defaultdict)**
- **🧩 Manual grouping by key**
- **🧩 Group by value (invert one-to-many)**
- **🧩 Group by custom function (e.g., length)**
- **🧩 Group by multiple keys (tuple/grouping)**
- **🧩 Group and aggregate (sum, count, min, max)**
- **🧩 Group and flatten (single list of all values)**
- **🧩 Group by key with set (unique values)**
- **🧩 Group by key with order preserved (OrderedDict)**
- **🧩 Group by key with itertools.groupby (sorted input)**
- **🧩 Large groupings (performance)**
- **🧩 Edge cases: empty input, all unique keys**

### Invert Key-Value Pairs
- **🧩 Invert 1:1 dictionary (values unique)**
- **🧩 Invert with duplicate values (many-to-one)**
- **🧩 Invert to one-to-many (group keys by value)**
- **🧩 Invert with defaultdict**
- **🧩 Invert with non-hashable values (error handling)**
- **🧩 Invert nested dictionary (swap inner keys/values)**
- **🧩 Edge cases: empty dict, non-unique values**

### List to Dictionary (Guide)
- **🧩 From list of (key, value) tuples**
- **🧩 From two lists (zip)**
- **🧩 From list with enumerate (index as key)**
- **🧩 From list of keys with default value**
- **🧩 From list of dicts (merge by key)**
- **🧩 From list of pairs with duplicate keys (last wins)**
- **🧩 From list of pairs with aggregation (sum/count)**
- **🧩 From list of lists (flatten to dict)**
- **🧩 From list with transformation (comprehension)**
- **🧩 From list of tuples with error handling**
- **🧩 Large lists (performance)**
- **🧩 Edge cases: empty list, non-hashable keys**

### Merge Dictionaries
- **🧩 Merge with update()**
- **🧩 Merge with dict unpacking (Python 3.5+)**
- **🧩 Merge with | operator (Python 3.9+)**
- **🧩 Merge multiple dicts (reduce)**
- **🧩 Deep merge (recursive)**
- **🧩 Conflict resolution (custom merge)**
- **🧩 Edge cases: empty dicts, overlapping keys**

### Nested Dictionary Access (Guide)
- **🧩 Access nested value (direct)**
- **🧩 Safe access with get()**
- **🧩 Set default for nested key (setdefault)**
- **🧩 Deep get (recursive function)**
- **🧩 Deep set (recursive function)**
- **🧩 Flatten nested dict (to single-level dict)**
- **🧩 Update nested dict (deep update)**
- **🧩 Delete nested key (safe)**
- **🧩 Nested dict with defaultdict**
- **🧩 Large nested dicts (performance)**
- **🧩 Edge cases: missing keys, non-dict values**

### Sort Dictionary
- **🧩 Sort by key (ascending)**
- **🧩 Sort by value (ascending)**
- **🧩 Sort by key (descending)**
- **🧩 Sort by value (descending)**
- **🧩 Sort by custom key (length, function)**
- **🧩 Stable sort (preserve order for equal keys/values)**
- **🧩 Sort nested dictionary by inner value**
- **🧩 Edge cases: empty dict, all equal values**

### Graph with Adjacency List
- **🧩 Undirected graph with adjacency list (dict of sets)**
- **🧩 Directed graph with adjacency list (dict of lists)**
- **🧩 Add/remove nodes and edges (undirected)**
- **🧩 Add/remove edges (directed)**
- **🧩 Convert edge list to adjacency list**

### Graph Connected Components
- **🧩 Connected components with DFS**
- **🧩 Connected components with BFS**
- **🧩 Edge cases: empty graph, all isolated nodes**

### Graph Cycle Detection
- **🧩 Cycle detection in undirected graph (DFS)**
- **🧩 Cycle detection in directed graph (DFS, recursion stack)**
- **🧩 Edge cases: empty graph, isolated nodes**

### Graph Node Degree
- **🧩 Degree in undirected graph**
- **🧩 In-degree and out-degree in directed graph**
- **🧩 Degree sequence for all nodes**
- **🧩 Edge cases: isolated node, empty graph**

### Graph Shortest Path
- **🧩 Shortest path (BFS, unweighted graph)**
- **🧩 Dijkstra's algorithm (weighted graph)**
- **🧩 Edge cases: disconnected, not found**

### Graph Topological Sort
- **🧩 Topological sort (DFS-based)**
- **🧩 Topological sort (Kahn's algorithm, BFS-based)**
- **🧩 Edge cases: empty graph, single node, cycle**

### Graph Traversal (DFS/BFS)
- **🧩 DFS (recursive, undirected graph)**
- **🧩 DFS (iterative, undirected graph)**
- **🧩 BFS (undirected graph)**
- **🧩 DFS/BFS for directed graph**
- **🧩 Path finding (DFS, undirected)**
- **🧩 Edge cases: disconnected, not found**

### Create Min-Heap with heapq
- **🧩 Heapify a list**
- **🧩 Push and pop from heap**
- **🧩 Peek at smallest element**
- **🧩 Heap sort (ascending)**

### n Largest and n Smallest with heapq
- **🧩 Find n largest elements**
- **🧩 Find n smallest elements**
- **🧩 nlargest/nsmallest with custom key**
- **🧩 Edge cases: n > len(list), n = 0**

### Push and Pop from Heap
- **🧩 Push and pop separately**
- **🧩 heappushpop: push then pop (efficient)**
- **🧩 heapreplace: pop then push (always replaces)**

### Chunk List
- **🧩 Split list into chunks**
- **🧩 Split list with generator**
- **🧩 Split list with fill value**
- **🧩 Split list with overlap**
- **🧩 Split list by condition**
- **🧩 Split list with maximum chunks**
- **🧩 Split list with custom chunking function**
- **🧩 Split list with balanced chunks**
- **🧩 Split list with performance monitoring**
- **🧩 Split list with error handling**

### Count Occurrences
- **🧩 Count occurrences in list**
- **🧩 Count all elements in list**
- **🧩 Count occurrences with condition**
- **🧩 Count occurrences in nested list**
- **🧩 Count occurrences with case insensitivity**
- **🧩 Count occurrences with partial matching**
- **🧩 Count occurrences with grouping**
- **🧩 Count occurrences with performance monitoring**
- **🧩 Count occurrences with error handling**
- **🧩 Count occurrences with memory optimization**

### Filter List
- **🧩 Filter list with condition**
- **🧩 Filter list with built-in filter**
- **🧩 Filter list with multiple conditions**
- **🧩 Filter list with any condition**
- **🧩 Filter list with custom logic**
- **🧩 Filter list by type**
- **🧩 Filter list with index**
- **🧩 Filter list with performance monitoring**
- **🧩 Filter list with error handling**
- **🧩 Filter list with memory optimization**
- **🧩 Filter list with transformation**

### Find Max Min
- **🧩 Find maximum value**
- **🧩 Find minimum value**
- **🧩 Find both max and min**
- **🧩 Find max/min with custom key function**
- **🧩 Find max/min with condition**
- **🧩 Find max/min with index**
- **🧩 Find max/min with multiple indices**
- **🧩 Find max/min in nested list**
- **🧩 Find max/min with performance monitoring**
- **🧩 Find max/min with error handling**
- **🧩 Find max/min with custom comparison**

### Flatten List
- **🧩 Flatten nested list**
- **🧩 Flatten list with list comprehension**
- **🧩 Flatten list with depth limit**
- **🧩 Flatten list with type filtering**
- **🧩 Flatten list with custom flattening rules**
- **🧩 Flatten list with position tracking**
- **🧩 Flatten list with memory optimization**
- **🧩 Flatten list with error handling**
- **🧩 Flatten list with performance monitoring**

### Map List
- **🧩 Map function over list**
- **🧩 Map with multiple functions**
- **🧩 Map with conditional logic**
- **🧩 Map with index awareness**
- **🧩 Map with multiple lists**
- **🧩 Map with generator optimization**
- **🧩 Map with performance monitoring**
- **🧩 Map with error handling**
- **🧩 Map with custom data structures**

### Merge Lists
- **🧩 Merge two lists**
- **🧩 Merge multiple lists**
- **🧩 Merge lists with deduplication**
- **🧩 Merge lists with custom merge function**
- **🧩 Merge lists with condition**
- **🧩 Merge lists with sorting**
- **🧩 Merge lists with interleaving**
- **🧩 Merge lists with priority**
- **🧩 Merge lists with performance monitoring**
- **🧩 Merge lists with error handling**
- **🧩 Merge lists with memory optimization**

### Reduce List
- **🧩 Reduce list to sum**
- **🧩 Reduce list with custom function**
- **🧩 Reduce list with conditional logic**
- **🧩 Reduce list with multiple values**
- **🧩 Reduce list with error handling**
- **🧩 Reduce list with generator optimization**
- **🧩 Reduce list with performance monitoring**
- **🧩 Reduce list with custom data structures**
- **🧩 Reduce list with advanced patterns**

### Remove Duplicates from List
- **🧩 Remove duplicates preserving order**
- **🧩 Remove duplicates using set**
- **🧩 Remove duplicates with custom key function**
- **🧩 Remove duplicates with case-insensitive comparison**
- **🧩 Remove duplicates from list of dictionaries**
- **🧩 Remove duplicates with frequency tracking**
- **🧩 Remove duplicates with custom comparison function**
- **🧩 Remove duplicates with memory optimization**
- **🧩 Remove duplicates with performance monitoring**
- **🧩 Remove duplicates with error handling**

### Reverse List
- **🧩 Reverse list in place**
- **🧩 Reverse list with new list**
- **🧩 Reverse list with custom step**
- **🧩 Reverse list partially**
- **🧩 Reverse list with condition**
- **🧩 Reverse list with grouping**
- **🧩 Reverse list with recursion**
- **🧩 Reverse list with generator**
- **🧩 Reverse list with performance monitoring**
- **🧩 Reverse list with error handling**

### Rotate List
- **🧩 Rotate list by n positions**
- **🧩 Rotate list left**
- **🧩 Rotate list in place**
- **🧩 Rotate list with custom direction**
- **🧩 Rotate list with multiple rotations**
- **🧩 Rotate list with condition**
- **🧩 Rotate list with circular buffer**
- **🧩 Rotate list with generator**
- **🧩 Rotate list with performance monitoring**
- **🧩 Rotate list with error handling**

### Sort List
- **🧩 Sort list in place**
- **🧩 Sort list with new list**
- **🧩 Sort list in reverse order**
- **🧩 Sort list with custom key function**
- **🧩 Sort list of dictionaries**
- **🧩 Sort list with multiple criteria**
- **🧩 Sort list with natural sorting**
- **🧩 Sort list with stability preservation**
- **🧩 Sort list with performance optimization**
- **🧩 Sort list with error handling**

### Sort List Custom
- **🧩 Sort list with custom key function**
- **🧩 Sort list by multiple keys**
- **🧩 Sort list with custom comparison function**
- **🧩 Sort list with natural ordering**
- **🧩 Sort list with locale awareness**
- **🧩 Sort list with stability preservation**
- **🧩 Sort list with performance monitoring**
- **🧩 Sort list with error handling**
- **🧩 Sort list with memory optimization**
- **🧩 Sort list with custom data structures**

### Transpose Matrix
- **🧩 Transpose 2D list**
- **🧩 Transpose matrix with list comprehension**
- **🧩 Transpose matrix with validation**
- **🧩 Transpose matrix with custom fill**
- **🧩 Transpose matrix in place**
- **🧩 Transpose matrix with generator**
- **🧩 Transpose matrix with performance monitoring**
- **🧩 Transpose matrix with error handling**
- **🧩 Transpose matrix with custom transformation**

### Zip Lists
- **🧩 Zip two lists**
- **🧩 Zip multiple lists**
- **🧩 Zip lists with different lengths**
- **🧩 Zip lists with custom pairing function**
- **🧩 Zip lists with condition**
- **🧩 Zip lists with index**
- **🧩 Zip lists with generator**
- **🧩 Zip lists with error handling**
- **🧩 Zip lists with performance monitoring**
- **🧩 Zip lists with custom aggregation**

### Priority Queue with heapq
- **🧩 Min-priority queue with heapq**
- **🧩 Max-priority queue with heapq**
- **🧩 Priority queue with custom objects**

### Use deque as Queue (FIFO)
- **🧩 Enqueue and dequeue with deque**
- **🧩 Peek at front and rear**
- **🧩 Queue with maxlen (bounded queue)**
- **🧩 Thread-safe queue with queue.Queue**

### Use List as Stack (LIFO)
- **🧩 Push and pop with list**
- **🧩 Peek at top of stack**
- **🧩 Stack with error handling**
- **🧩 Stack size and clear**

### Create Set
- **🧩 Create set from list**
- **🧩 Create set from string**
- **🧩 Create set from tuple or other iterable**
- **🧩 Create set with comprehension**
- **🧩 Immutable sets (frozenset)**

### Set Membership
- **🧩 Check if item is in set**
- **🧩 Not in set**
- **🧩 Set membership with custom objects**

### Set Operations
- **🧩 Union of sets**
- **🧩 Intersection of sets**
- **🧩 Difference of sets**
- **🧩 Symmetric difference of sets**
- **🧩 Multiple set operations**

### Add and Remove Items from Set
- **🧩 Add item to set**
- **🧩 Remove item from set**
- **🧩 Discard item from set**
- **🧩 Pop item from set**
- **🧩 Update set with multiple items**
- **🧩 Remove multiple items from set**

### Subset and Superset Relations
- **🧩 Check if set is subset**
- **🧩 Check if set is superset**
- **🧩 Proper subset and superset**

### Get Unique Elements from List
- **🧩 Unique elements with set**
- **🧩 Unique elements preserving order (Python 3.7+)**
- **🧩 Unique elements by key**

### Tree with Nested Dictionaries
- **🧩 Create a tree with nested dicts**
- **🧩 Add a child node**
- **🧩 Remove a node**
- **🧩 Traverse all nodes (preorder)**

### Tree Height / Depth
- **🧩 Height of general tree (nested dict, recursive)**
- **🧩 Height of binary tree (recursive)**
- **🧩 Height of general tree (iterative, BFS)**
- **🧩 Edge cases: empty tree, single node**

### Find All Leaf Nodes
- **🧩 Leaf nodes in general tree (recursive)**
- **🧩 Leaf nodes in binary tree (recursive)**
- **🧩 Leaf nodes in general tree (iterative, DFS)**
- **🧩 Edge cases: empty tree, single node**

### Tree Parent Lookup
- **🧩 Build parent map (general tree)**
- **🧩 Find parent of a node**
- **🧩 Build parent map (binary tree)**
- **🧩 Find ancestors of a node**

### Find Path to Node
- **🧩 Path to node (general tree, recursive)**
- **🧩 Path to node (binary tree, recursive)**
- **🧩 Path to node (general tree, iterative DFS)**
- **🧩 Edge cases: not found, root only**

### Pretty-Print Tree Structure
- **🧩 Pretty-print general tree (nested dict)**
- **🧩 Pretty-print binary tree (sideways)**
- **🧩 Print tree with node values/attributes**
- **🧩 Edge cases: empty tree, single node**

### Tree Traversal (DFS/BFS)
- **🧩 Preorder DFS (recursive, general tree)**
- **🧩 DFS (iterative, general tree)**
- **🧩 BFS (level-order, general tree)**
- **🧩 Preorder, Inorder, Postorder (binary tree, recursive)**
- **🧩 BFS (level-order, binary tree)**

### Named Tuple Usage
- **🧩 Create and use a namedtuple**
- **🧩 Access by index and unpacking**
- **🧩 Namedtuple with defaults (Python 3.7+)**
- **🧩 Namedtuple as dictionary (._asdict())**
- **🧩 Replace fields with ._replace()**
- **🧩 Nested namedtuples and practical usage**

### Create and Use Tuples
- **🧩 Create a tuple**
- **🧩 Tuple from iterable**
- **🧩 Tuple packing and unpacking**
- **🧩 Tuple immutability and usage**
- **🧩 Nested tuples and tuple of tuples**

### Tuple Unpacking
- **🧩 Basic tuple unpacking**
- **🧩 Unpacking in for loops**
- **🧩 Extended unpacking (Python 3+)**
- **🧩 Swapping variables with tuple unpacking**
- **🧩 Nested tuple unpacking**
- **🧩 Unpacking with * in function arguments**

## Files Snippets
### Append File
- **🧩 Append string to file**
- **🧩 Append with newline**
- **🧩 Append with timestamp**
- **🧩 Append with rotation**

### Change Directory
- **🧩 Change working directory**
- **🧩 Change directory safely**
- **🧩 Change directory with validation**
- **🧩 Change directory with context manager**

### Copy Directory
- **🧩 Copy directory tree**
- **🧩 Copy directory safely**
- **🧩 Copy directory with overwrite**
- **🧩 Copy directory with filtering**

### Copy File
- **🧩 Copy file with shutil**
- **🧩 Copy file with metadata**
- **🧩 Copy file with progress**
- **🧩 Copy file with verification**

### Create Directory
- **🧩 Create single directory**
- **🧩 Create directory safely**
- **🧩 Create directory if not exists**
- **🧩 Create directory with permissions**

### Create Nested Directories
- **🧩 Create nested directories**
- **🧩 Create nested directories safely**
- **🧩 Create nested directories if not exist**
- **🧩 Create nested directories with custom permissions**

### Create Temp File
- **🧩 Create temporary file**
- **🧩 Create temporary file with suffix**
- **🧩 Create temporary file with custom directory**
- **🧩 Create temporary file with cleanup**

### Delete Directory
- **🧩 Delete empty directory**
- **🧩 Delete empty directory safely**
- **🧩 Delete directory if empty**
- **🧩 Delete directory with confirmation**

### Delete Directory Recursive
- **🧩 Delete directory and contents with shutil**
- **🧩 Delete directory safely**
- **🧩 Delete directory with confirmation**
- **🧩 Delete directory with backup**

### Delete File
- **🧩 Delete a file**
- **🧩 Delete file safely**
- **🧩 Delete file with confirmation**
- **🧩 Delete multiple files**

### Directory Exists
- **🧩 Check if directory exists**
- **🧩 Check if path is a directory**
- **🧩 Check directory with detailed status**
- **🧩 Check directory with validation**

### File Checksum
- **🧩 Calculate MD5 checksum**
- **🧩 Calculate SHA-256 checksum**
- **🧩 Calculate checksum for large files**
- **🧩 Verify file integrity with checksum**

### File Exists
- **🧩 Check if file exists**
- **🧩 Check if file is a regular file**
- **🧩 Check file with multiple conditions**
- **🧩 Check file with permissions**

### Get Current Directory
- **🧩 Get current working directory**
- **🧩 Get current directory safely**
- **🧩 Get current directory with validation**
- **🧩 Get current directory with path analysis**

### Get File Modified Time
- **🧩 Get file modification time**
- **🧩 Get file modification time safely**
- **🧩 Get file modification time as datetime**
- **🧩 Get file age in human readable format**

### Get File Size
- **🧩 Get file size in bytes**
- **🧩 Get file size safely**
- **🧩 Get file size in human readable format**
- **🧩 Get directory size recursively**

### List Directory
- **🧩 List files in directory**
- **🧩 List files in specific directory**
- **🧩 List files with details**
- **🧩 List files with filtering**

### List Directory Recursive
- **🧩 List all files recursively**
- **🧩 List directories recursively**
- **🧩 List files with relative paths**
- **🧩 List files with depth limit**

### Move File
- **🧩 Move/rename file**
- **🧩 Move file with os.rename**
- **🧩 Move file with backup**
- **🧩 Move file with validation**

### Read Binary File
- **🧩 Read binary file**
- **🧩 Read binary file in chunks**
- **🧩 Read binary file with specific encoding**
- **🧩 Read binary file with structure parsing**

### Read File
- **🧩 Read entire file as string**
- **🧩 Read file with encoding**
- **🧩 Read file with error handling**
- **🧩 Read file in chunks**

### Read File Lines
- **🧩 Read file as list of lines**
- **🧩 Read lines without newlines**
- **🧩 Read lines with line numbers**
- **🧩 Read lines with filtering**

### Write Binary File
- **🧩 Write binary file**
- **🧩 Write binary file from string**
- **🧩 Write binary file with structured data**
- **🧩 Write binary file with checksum**

### Write File
- **🧩 Write string to file**
- **🧩 Write with encoding**
- **🧩 Write file with error handling**
- **🧩 Write file atomically**

### Write Lines
- **🧩 Write list of lines to file**
- **🧩 Write lines with newlines**
- **🧩 Write lines with numbering**
- **🧩 Write lines with filtering**

## Math Snippets
### Bit Operations
- **🧩 Basic bitwise operations**
- **🧩 Bit shifts and masks**
- **🧩 Bit counting and tests**
- **🧩 Bitwise rotation and reversal**
- **🧩 Bit field extraction and packing**
- **🧩 Handle edge cases in bit operations**
- **🧩 Performance comparison**
- **🧩 Permissions, flags, and encoding**

### Calculus
- **🧩 Numerical derivative (finite difference)**
- **🧩 Numerical integral (trapezoidal rule)**
- **🧩 Numerical limit (approaching a point)**
- **🧩 Higher-order derivatives**
- **🧩 Definite integral (Simpson's rule)**
- **🧩 Numerical partial derivatives (multivariate)**
- **🧩 Handle invalid functions and domains**
- **🧩 Performance comparison**
- **🧩 Physics and optimization**

### Number Clamping Operations
- **🧩 Clamp number to range**
- **🧩 Clamp to positive range**
- **🧩 Clamp to unit range**
- **🧩 Clamp with custom bounds**
- **🧩 Clamp with step increments**
- **🧩 Clamp with soft bounds**
- **🧩 Clamp with exponential decay**
- **🧩 Handle edge cases in clamping**
- **🧩 Performance optimization**
- **🧩 Color value clamping**
- **🧩 Audio level clamping**

### Complex Number Operations
- **🧩 Basic complex arithmetic**
- **🧩 Create and access complex numbers**
- **🧩 Absolute value, phase, and polar form**
- **🧩 Complex exponentials and logarithms**
- **🧩 Complex roots and powers**
- **🧩 Trigonometric and hyperbolic functions**
- **🧩 Handle edge cases in complex arithmetic**
- **🧩 Performance comparison**
- **🧩 Signal processing and engineering**

### Decimal Precision Operations
- **🧩 Basic decimal arithmetic**
- **🧩 Set global decimal precision**
- **🧩 Decimal rounding and quantization**
- **🧩 Decimal context management**
- **🧩 Decimal math functions**
- **🧩 Decimal comparisons and equality**
- **🧩 Handle edge cases in decimal arithmetic**
- **🧩 Performance comparison**
- **🧩 Financial calculations**

### Exponent Operations
- **🧩 Basic exponential functions**
- **🧩 Exponential properties and identities**
- **🧩 Exponential growth and decay**
- **🧩 Exponential equations and solving**
- **🧩 Exponential series and approximations**
- **🧩 Exponential interpolation and smoothing**
- **🧩 Handle edge cases in exponential calculations**
- **🧩 Performance comparison**
- **🧩 Financial and economic applications**
- **🧩 Scientific and engineering applications**

### Factorial Operations
- **🧩 Calculate factorial**
- **🧩 Calculate factorial recursively**
- **🧩 Calculate double factorial**
- **🧩 Calculate falling factorial**
- **🧩 Calculate subfactorial**
- **🧩 Calculate factorial with memoization**
- **🧩 Calculate factorial approximation**
- **🧩 Handle edge cases in factorial calculations**
- **🧩 Performance comparison**
- **🧩 Combinatorial calculations**
- **🧩 Probability calculations**

### Fibonacci Operations
- **🧩 Generate Fibonacci sequence**
- **🧩 Get nth Fibonacci number**
- **🧩 Generate Fibonacci recursively**
- **🧩 Generate Fibonacci with memoization**
- **🧩 Generate Fibonacci using matrix exponentiation**
- **🧩 Generate Fibonacci with Binet's formula**
- **🧩 Generate Fibonacci with different starting values**
- **🧩 Handle edge cases in Fibonacci calculations**
- **🧩 Performance comparison**
- **🧩 Fibonacci in nature and art**
- **🧩 Fibonacci in algorithms**

### Number Formatting Operations
- **🧩 Format with commas**
- **🧩 Format with decimal places**
- **🧩 Format as percentage**
- **🧩 Format with custom separators**
- **🧩 Format with scientific notation**
- **🧩 Format currency**
- **🧩 Format with units**
- **🧩 Handle edge cases in formatting**
- **🧩 Performance optimization**
- **🧩 Financial reporting**
- **🧩 Data visualization labels**

### Fraction Math Operations
- **🧩 Basic fraction arithmetic**
- **🧩 Create and simplify fractions**
- **🧩 Fraction to float and decimal**
- **🧩 Fraction comparison and equality**
- **🧩 Fraction reduction and expansion**
- **🧩 Fraction from float and decimal**
- **🧩 Handle edge cases in fraction arithmetic**
- **🧩 Performance comparison**
- **🧩 Ratio and proportion calculations**

### GCD and LCM Operations
- **🧩 Calculate GCD using Euclidean algorithm**
- **🧩 Calculate GCD recursively**
- **🧩 Calculate LCM**
- **🧩 Calculate GCD for multiple numbers**
- **🧩 Extended Euclidean algorithm**
- **🧩 Binary GCD algorithm**
- **🧩 GCD and LCM with prime factorization**
- **🧩 Handle edge cases in GCD/LCM calculations**
- **🧩 Performance comparison**
- **🧩 Fraction simplification**
- **🧩 Cryptography applications**

### Even/Odd Number Operations
- **🧩 Check if number is even**
- **🧩 Check if number is odd**
- **🧩 Get number parity**
- **🧩 Check even/odd with bitwise operations**
- **🧩 Check even/odd for floating point**
- **🧩 Check even/odd with tolerance**
- **🧩 Check even/odd for sequences**
- **🧩 Handle edge cases in even/odd checks**
- **🧩 Performance comparison**
- **🧩 Alternating pattern generation**
- **🧩 Mathematical operations**

### Prime Number Operations
- **🧩 Check if number is prime**
- **🧩 Get next prime number**
- **🧩 Check if number is composite**
- **🧩 Optimized prime checking**
- **🧩 Prime factorization**
- **🧩 Generate prime numbers**
- **🧩 Prime number properties**
- **🧩 Handle edge cases in prime checking**
- **🧩 Performance optimization**
- **🧩 Cryptographic applications**
- **🧩 Mathematical research**

### Linear Algebra Operations
- **🧩 Vector addition, subtraction, and scalar multiplication**
- **🧩 Dot product and cross product**
- **🧩 Vector norm, length, and normalization**
- **🧩 Matrix addition, subtraction, and scalar multiplication**
- **🧩 Matrix multiplication and transpose**
- **🧩 Identity, zero, and diagonal matrices**
- **🧩 Determinant and inverse (2x2, 3x3)**
- **🧩 Handle edge cases in linear algebra**
- **🧩 Performance comparison**
- **🧩 Solve system of linear equations (2x2)**

### Logarithm Operations
- **🧩 Basic logarithmic functions**
- **🧩 Logarithmic properties and identities**
- **🧩 Exponential functions**
- **🧩 Logarithmic equations and solving**
- **🧩 Logarithmic scales and transformations**
- **🧩 Logarithmic series and approximations**
- **🧩 Handle edge cases in logarithmic calculations**
- **🧩 Performance comparison**
- **🧩 Information theory and entropy**
- **🧩 Scientific and engineering applications**

### Matrices
- **🧩 Matrix creation and display**
- **🧩 Matrix addition and subtraction**
- **🧩 Matrix multiplication (dot product)**
- **🧩 Matrix transpose**
- **🧩 Identity, zero, and diagonal matrices**
- **🧩 Determinant (2x2, 3x3)**
- **🧩 Inverse (2x2)**
- **🧩 Handle invalid matrices**
- **🧩 Performance comparison**
- **🧩 Solving systems of equations (2x2)**

### Number Conversion
- **🧩 Integer to binary, octal, hexadecimal strings**
- **🧩 String to integer (any base)**
- **🧩 Integer to/from bytes**
- **🧩 Float to string and back**
- **🧩 Base conversion between arbitrary bases**
- **🧩 Type conversion: int, float, complex, fraction, decimal**
- **🧩 Handle invalid conversions**
- **🧩 Performance comparison**
- **🧩 Parsing user input and config**

### Percentage Operations
- **🧩 Calculate percentage**
- **🧩 Calculate percentage change**
- **🧩 Calculate percentage of number**
- **🧩 Calculate compound percentage**
- **🧩 Calculate weighted percentage**
- **🧩 Calculate percentage difference**
- **🧩 Calculate percentage points**
- **🧩 Handle edge cases in percentage calculations**
- **🧩 Performance optimization**
- **🧩 Grade calculation**
- **🧩 Sales analysis**

### Random Number Operations
- **🧩 Generate random number**
- **🧩 Generate random choice**
- **🧩 Shuffle list randomly**
- **🧩 Generate random with specific distributions**
- **🧩 Generate random with custom seed**
- **🧩 Generate random with constraints**
- **🧩 Generate random sequences and patterns**
- **🧩 Handle edge cases in random generation**
- **🧩 Performance optimization**
- **🧩 Simulation and modeling**
- **🧩 Game and entertainment**

### Roots
- **🧩 Square root**
- **🧩 Cube root**
- **🧩 Nth root**
- **🧩 Roots of negative numbers (complex)**
- **🧩 Integer roots and perfect powers**
- **🧩 Handle invalid roots**
- **🧩 Performance comparison**
- **🧩 Geometry and finance**

### Round Number Operations
- **🧩 Round to decimal places**
- **🧩 Round with different strategies**
- **🧩 Round to significant figures**
- **🧩 Round with custom rounding function**
- **🧩 Round currency amounts**
- **🧩 Round with precision control**
- **🧩 Round to nearest multiple**
- **🧩 Handle edge cases in rounding**
- **🧩 Performance comparison**
- **🧩 Financial calculations**
- **🧩 Scientific measurements**

### Advanced Statistics Operations
- **🧩 Calculate variance and standard deviation**
- **🧩 Calculate quantiles, percentiles, and IQR**
- **🧩 Calculate skewness and kurtosis (manual)**
- **🧩 Covariance and correlation**
- **🧩 Z-scores and standardization**
- **🧩 Moving average and rolling statistics**
- **🧩 Handle edge cases in advanced statistics**
- **🧩 Performance comparison**
- **🧩 Outlier detection and normalization**
- **🧩 Linear regression (simple)**

### Basic Statistics Operations
- **🧩 Calculate mean, median, and mode**
- **🧩 Calculate min, max, and range**
- **🧩 Calculate sum, count, and average**
- **🧩 Calculate weighted mean and harmonic mean**
- **🧩 Calculate geometric mean and midrange**
- **🧩 Frequency, unique values, and counts**
- **🧩 Handle edge cases in statistics**
- **🧩 Performance comparison**
- **🧩 Grade calculation and summary statistics**

### Trigonometry Operations
- **🧩 Basic trigonometric functions**
- **🧩 Inverse trigonometric functions**
- **🧩 Trigonometric identities**
- **🧩 Trigonometric equations and solving**
- **🧩 Trigonometric series and approximations**
- **🧩 Trigonometric interpolation and smoothing**
- **🧩 Handle edge cases in trigonometric calculations**
- **🧩 Performance comparison**
- **🧩 Geometry and physics applications**
- **🧩 Signal processing and waves**

### Vectors
- **🧩 Vector creation and display**
- **🧩 Vector addition, subtraction, scalar multiplication**
- **🧩 Dot product and cross product**
- **🧩 Vector norm and normalization**
- **🧩 Angle between vectors**
- **🧩 Projection and rejection**
- **🧩 Handle invalid vectors**
- **🧩 Performance comparison**
- **🧩 Physics and geometry**

## Strings Snippets
### Camel to Snake Case
- **🧩 Convert camelCase to snake_case**
- **🧩 Convert with underscore handling**
- **🧩 Convert with acronym handling**
- **🧩 Convert with custom separators**

### Capitalize Words
- **🧩 Capitalize first letter of each word**
- **🧩 Capitalize first letter only**
- **🧩 Capitalize words with custom exceptions**
- **🧩 Capitalize words with special handling**

### Center String in Width
- **🧩 Center string with spaces**
- **🧩 Center with custom character**
- **🧩 Center with truncation**
- **🧩 Center with custom alignment bias**
- **🧩 Center with multiple lines**
- **🧩 Center with word wrapping**
- **🧩 Center with color preservation**
- **🧩 Center with Unicode support**
- **🧩 Center with custom width calculation**

### Count Substring Occurrences
- **🧩 Count substring occurrences**
- **🧩 Count with case-insensitive matching**
- **🧩 Count overlapping substrings**
- **🧩 Count with word boundaries**
- **🧩 Count multiple substrings**
- **🧩 Count with position tracking**

### Check String Ends With
- **🧩 Check if string ends with suffix**
- **🧩 Check with case-insensitive matching**
- **🧩 Check multiple suffixes**
- **🧩 Check with position offset**
- **🧩 Check file extensions**
- **🧩 Check with regex pattern**
- **🧩 Check with custom function**
- **🧩 Check with multiple conditions**
- **🧩 Check with word boundaries**

### Find String
- **🧩 Find substring position**
- **🧩 Find from specific position**
- **🧩 Find with end limit**
- **🧩 Check if substring exists**
- **🧩 Find all occurrences**
- **🧩 Find with case-insensitive search**
- **🧩 Find with regex pattern**
- **🧩 Find with context**
- **🧩 Find with multiple patterns**

### Format String
- **🧩 Basic string formatting**
- **🧩 Named placeholders**
- **🧩 F-string formatting**
- **🧩 Number formatting**
- **🧩 Advanced number formatting**
- **🧩 Conditional formatting**
- **🧩 Template formatting**
- **🧩 Custom formatting functions**
- **🧩 Multi-line formatting**

### Check if String is Alphabetic
- **🧩 Check if string is alphabetic**
- **🧩 Check if string is alphabetic with spaces**
- **🧩 Check if string is alphabetic with custom characters**
- **🧩 Check if string starts with letter**
- **🧩 Check if string ends with letter**
- **🧩 Check if string contains only uppercase letters**
- **🧩 Check if string contains only lowercase letters**
- **🧩 Check if string is title case**
- **🧩 Check if string contains specific letters**
- **🧩 Check if string is alphabetic with minimum length**
- **🧩 Check if string is alphabetic with maximum length**
- **🧩 Check if string is alphabetic with length range**

### Check if String is Alphanumeric
- **🧩 Check if string is alphanumeric**
- **🧩 Check if string is alphanumeric with spaces**
- **🧩 Check if string is alphanumeric with custom characters**
- **🧩 Check if string contains at least one letter and one digit**
- **🧩 Check if string is alphanumeric with minimum length**
- **🧩 Check if string is alphanumeric with maximum length**
- **🧩 Check if string is alphanumeric with length range**
- **🧩 Check if string starts with alphanumeric**
- **🧩 Check if string ends with alphanumeric**
- **🧩 Check if string contains specific alphanumeric pattern**
- **🧩 Check if string is valid identifier**
- **🧩 Check if string is valid username**

### Check if Strings are Anagrams
- **🧩 Basic anagram check**
- **🧩 Anagram check with character counting**
- **🧩 Anagram check with punctuation removal**
- **🧩 Anagram check with custom character filtering**
- **🧩 Anagram check with word boundaries**
- **🧩 Anagram check with character frequency analysis**
- **🧩 Anagram check with minimum length requirement**
- **🧩 Anagram check with performance optimization**
- **🧩 Anagram check with Unicode support**
- **🧩 Anagram check with custom comparison**
- **🧩 Anagram check with multiple strings**

### Validate Email Address
- **🧩 Basic email validation**
- **🧩 Email validation with length check**
- **🧩 Comprehensive email validation**
- **🧩 Email validation with domain check**
- **🧩 Email validation with local part rules**
- **🧩 Email validation with TLD check**
- **🧩 Email validation with common patterns**
- **🧩 Email validation with length limits**
- **🧩 Email validation with case sensitivity**

### Check if String is Numeric
- **🧩 Check if string is numeric**
- **🧩 Check if string is decimal**
- **🧩 Check if string is integer**
- **🧩 Check if string is positive number**
- **🧩 Check if string is in range**
- **🧩 Check if string is hexadecimal**
- **🧩 Check if string is binary**
- **🧩 Check if string is octal**
- **🧩 Check if string is scientific notation**
- **🧩 Check if string is currency**
- **🧩 Check if string is percentage**

### Check if String is Palindrome
- **🧩 Basic palindrome check**
- **🧩 Case-insensitive palindrome check**
- **🧩 Palindrome check with punctuation removal**
- **🧩 Palindrome check with custom character filtering**
- **🧩 Palindrome check with word boundaries**
- **🧩 Palindrome check with position tracking**
- **🧩 Palindrome check with minimum length**
- **🧩 Palindrome check with character counting**
- **🧩 Palindrome check with custom comparison**
- **🧩 Palindrome check with Unicode support**
- **🧩 Palindrome check with performance optimization**

### Validate URL Format
- **🧩 Basic URL validation**
- **🧩 URL validation with protocol check**
- **🧩 Comprehensive URL validation**
- **🧩 URL validation with domain check**
- **🧩 URL validation with path check**
- **🧩 URL validation with port check**
- **🧩 URL validation with query parameters**
- **🧩 URL validation with fragment check**
- **🧩 URL validation with IP address support**
- **🧩 URL validation with length limits**

### Join Strings
- **🧩 Join list of strings**
- **🧩 Join with custom separator**
- **🧩 Join with newlines**
- **🧩 Join with conditional formatting**
- **🧩 Join with filtering**
- **🧩 Join with grouping**

### Justify Text Alignment
- **🧩 Left justify text**
- **🧩 Right justify text**
- **🧩 Center justify text**
- **🧩 Justify with custom alignment**
- **🧩 Justify multiline text**
- **🧩 Justify with word wrapping**
- **🧩 Justify with truncation**
- **🧩 Justify with custom width calculation**
- **🧩 Justify with alignment bias**
- **🧩 Justify with Unicode support**

### Normalize Whitespace
- **🧩 Normalize multiple spaces to single**
- **🧩 Normalize all whitespace**
- **🧩 Normalize whitespace with preservation**
- **🧩 Normalize whitespace with custom rules**

### Pad String to Width
- **🧩 Pad string with spaces**
- **🧩 Pad with custom character**
- **🧩 Pad with multiple characters**
- **🧩 Pad with truncation**
- **🧩 Pad with color codes**
- **🧩 Pad with Unicode characters**
- **🧩 Pad with custom alignment**
- **🧩 Pad with number formatting**

### Remove Whitespace
- **🧩 Remove all whitespace**
- **🧩 Remove leading and trailing whitespace**
- **🧩 Remove whitespace with custom characters**
- **🧩 Remove whitespace with normalization**
- **🧩 Check if string is empty**

### Replace String
- **🧩 Replace substring**
- **🧩 Replace multiple occurrences**
- **🧩 Replace with count limit**
- **🧩 Replace with case-insensitive matching**
- **🧩 Replace with custom function**
- **🧩 Replace with conditional logic**
- **🧩 Replace with context awareness**

### Reverse String
- **🧩 Reverse string with slicing**
- **🧩 Reverse string with reversed()**
- **🧩 Reverse string with word preservation**
- **🧩 Reverse string with custom characters**

### Snake to Camel Case
- **🧩 Convert snake_case to camelCase**
- **🧩 Convert with underscore cleaning**
- **🧩 Convert with acronym preservation**
- **🧩 Convert with custom options**

### Split String
- **🧩 Split string by delimiter**
- **🧩 Split string by whitespace**
- **🧩 Split string with max splits**
- **🧩 Split string with regex**

### Check String Starts With
- **🧩 Check if string starts with prefix**
- **🧩 Check with case-insensitive matching**
- **🧩 Check multiple prefixes**
- **🧩 Check with position offset**
- **🧩 Check with regex pattern**
- **🧩 Check with custom function**
- **🧩 Check with multiple conditions**

### Strip Characters from String
- **🧩 Strip whitespace from ends**
- **🧩 Strip specific characters**
- **🧩 Strip from left only**
- **🧩 Strip from right only**
- **🧩 Strip multiple character sets**
- **🧩 Strip with custom function**
- **🧩 Strip with regex pattern**
- **🧩 Strip with character classes**
- **🧩 Strip with position tracking**

### Title Case
- **🧩 Convert to title case**
- **🧩 Title case with custom separator**
- **🧩 Title case with minor word exceptions**
- **🧩 Title case with special character handling**

### Truncate String
- **🧩 Truncate string to length**
- **🧩 Truncate with ellipsis**
- **🧩 Truncate at word boundary**
- **🧩 Truncate with custom rules**
- **🧩 Validate string length**

### Validate Credit Card Number
- **🧩 Basic credit card validation**
- **🧩 Credit card validation with format check**
- **🧩 Credit card validation with card type detection**
- **🧩 Credit card validation with detailed error reporting**
- **🧩 Credit card validation with security features**
- **🧩 Credit card validation with country detection**
- **🧩 Credit card validation with expiration check**
- **🧩 Credit card validation with CVV check**
- **🧩 Credit card validation with batch processing**

### Validate Password Strength
- **🧩 Basic Password Validation**
- **🧩 Password Strength Checker**
- **🧩 Advanced Password Validation**
- **🧩 Password Entropy Calculator**
- **🧩 Password Policy Enforcer**

### Validate Phone Number
- **🧩 Basic Phone Validation**
- **🧩 US Phone Number Validation**
- **🧩 International Phone Validation**
- **🧩 Format International Phone Number**
- **🧩 Parse Phone Number with Extension**
- **🧩 Validate Phone Number Extension**
- **🧩 Normalize Phone Number**
- **🧩 Extract Phone Numbers from Text**

### Wrap Text
- **🧩 Wrap text to width**
- **🧩 Wrap text with fill**
- **🧩 Wrap text with custom options**
- **🧩 Wrap text with custom break function**

## Web Snippets
### Add Query Parameters to URL
- **🧩 Add new query parameters to URL**
- **🧩 Replace existing query parameters**
- **🧩 Add multiple values for a single key**
- **🧩 Add to URL with empty or no query string**

### Build URL
- **🧩 Build URL from components**
- **🧩 Add or replace query parameters in URL**
- **🧩 Join base and relative URLs**
- **🧩 Build URL with user, password, and port**
- **🧩 Build URL with fragment and params**
- **🧩 Build URL with missing parts and double slashes**

### Download File via HTTP
- **🧩 Simple file download**
- **🧩 Download file with progress bar**
- **🧩 Download with custom headers and error handling**
- **🧩 Download large file (streaming, low memory)**
- **🧩 Invalid URL and disk full**

### Extract Domain from URL
- **🧩 Extract netloc (host:port) from URL**
- **🧩 Extract host (domain) only (without port)**
- **🧩 Extract port from URL**
- **🧩 Extract registered domain (TLD split, basic)**
- **🧩 Extract domain from IPv6 URL**
- **🧩 Extract from URL with missing netloc or malformed URL**

### HTTP Basic Authentication
- **🧩 HTTP GET with Basic Auth**
- **🧩 HTTP POST with Basic Auth**
- **🧩 HTTP GET with Basic Auth using HTTPPasswordMgr**
- **🧩 Error handling and invalid credentials**
- **🧩 Missing or malformed Authorization header**

### HTTP DELETE Request
- **🧩 Simple HTTP DELETE request**
- **🧩 HTTP DELETE with custom headers**
- **🧩 HTTP DELETE with query parameters**
- **🧩 HTTP DELETE with authentication (Basic Auth)**
- **🧩 HTTP DELETE with error handling**
- **🧩 Invalid URL, unsupported method, missing authentication**

### HTTP GET Request
- **🧩 Simple HTTP GET request**
- **🧩 HTTP GET with custom headers**
- **🧩 HTTP GET with error handling**
- **🧩 HTTP GET streaming (binary data)**
- **🧩 HTTP GET with timeout and redirect handling**
- **🧩 HTTP GET with proxy support**
- **🧩 HTTP GET ignoring SSL certificate errors**

### Set Custom HTTP Headers
- **🧩 HTTP GET with custom headers**
- **🧩 HTTP POST with custom headers**
- **🧩 HTTP GET with Authorization header (Bearer token)**
- **🧩 HTTP GET with custom User-Agent and Accept headers**
- **🧩 Case-insensitivity and invalid headers**
- **🧩 Missing or None headers**

### HTTP POST Request
- **🧩 Simple HTTP POST request (form data)**
- **🧩 HTTP POST with custom headers**
- **🧩 HTTP POST with JSON body**
- **🧩 HTTP POST with error handling**
- **🧩 HTTP POST file upload (multipart/form-data)**
- **🧩 HTTP POST with timeout and proxy**

### HTTP PUT Request
- **🧩 Simple HTTP PUT request (string data)**
- **🧩 HTTP PUT with custom headers**
- **🧩 HTTP PUT with JSON body**
- **🧩 HTTP PUT file upload (binary data)**
- **🧩 HTTP PUT with error handling**
- **🧩 Invalid URL, large file, unsupported method**

### HTTP Redirects
- **🧩 Default redirect handling (automatic)**
- **🧩 Disable redirects (block all)**
- **🧩 Custom redirect handler (limit number of redirects)**
- **🧩 Capture redirect chain (history)**
- **🧩 POST/PUT/DELETE with redirects**
- **🧩 Redirect loop and too many redirects**

### HTTP Session (Persistent Cookies & Headers)
- **🧩 Simple HTTP session with cookies**
- **🧩 HTTP session with custom headers**
- **🧩 Simulate login and session persistence**
- **🧩 Error handling and edge cases**
- **🧩 Session reset and manual cookie management**

### HTTP Status Code Handling
- **🧩 Get status code from response**
- **🧩 Handle specific status codes (success, redirect, error)**
- **🧩 Custom error handling for 401, 403, 500**
- **🧩 Map status codes to messages**
- **🧩 Check for success/failure**
- **🧩 Non-standard codes and missing status**

### HTTP Request Timeout
- **🧩 HTTP GET with timeout**
- **🧩 HTTP POST with timeout**
- **🧩 Custom timeout and edge cases**

### Parse Query Parameters from URL
- **🧩 Extract all query parameters as a dictionary**
- **🧩 Extract single-value query parameters**
- **🧩 Handle repeated keys in query string**
- **🧩 Parse query string with missing values and encoded values**
- **🧩 Parse empty query string**

### Parse URL
- **🧩 Parse URL into components**
- **🧩 Extract individual URL components**
- **🧩 Parse query parameters from URL**
- **🧩 Handle missing scheme and relative URLs**
- **🧩 Parse non-standard ports and user info**
- **🧩 Parse URL with IPv6 address**

### Convert Relative URL to Absolute URL
- **🧩 Convert relative URL to absolute using base**
- **🧩 Convert with dot segments (.. and .)**
- **🧩 Convert already absolute URL**
- **🧩 Convert with empty base or malformed URLs**

### Remove Query Parameters from URL
- **🧩 Remove a single query parameter**
- **🧩 Remove multiple query parameters**
- **🧩 Remove all query parameters**
- **🧩 Remove non-existent or encoded keys, empty query**

### Upload File via HTTP (multipart/form-data)
- **🧩 Simple file upload (multipart/form-data)**
- **🧩 Upload file with custom headers and error handling**
- **🧩 Upload multiple files (multipart/form-data)**
- **🧩 Upload file with progress reporting**
- **🧩 Large/unsupported files and permission errors**

### URL Decode String
- **🧩 Decode query string parameters**
- **🧩 Decode path segment**
- **🧩 Decode form data from POST**
- **🧩 Decode with Unicode and reserved characters**
- **🧩 Double decoding and empty values**

### URL Encode String
- **🧩 Encode query string parameters**
- **🧩 Encode path segment**
- **🧩 Encode form data for POST**
- **🧩 Encode with Unicode and reserved characters**
- **🧩 Encode already-encoded strings and empty values**

### URL Join
- **🧩 Join base and relative URLs**
- **🧩 Join with dot segments (.. and .)**
- **🧩 Join with/without trailing slashes**
- **🧩 Join with query and fragment**
- **🧩 Join with absolute relative URL**
- **🧩 Join with empty base or malformed URLs**

### Validate URL
- **🧩 Check if URL has valid scheme and netloc**
- **🧩 Validate URL with regex (basic)**
- **🧩 Validate URL with reserved domains and invalid characters**
- **🧩 Validate missing scheme, empty, or malformed URLs**
