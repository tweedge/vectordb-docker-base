from vectordb import Memory
import sys

model = sys.argv[1]

# Memory is where all content you want to store/search goes.
memory = Memory(embeddings=model)

memory.save(
    [  # save your text content. for long text we will automatically chunk it
        "apples are green",
        "oranges are orange",
    ],
    [  # associate any kind of metadata with it (optional)
        {"url": "https://apples.com"},
        {"url": "https://oranges.com"},
    ],
)

# By this point we'll have definitely gathered the relevant models from the web
print("INITIALIZED; RUNNING BRIEF SELF-TEST")

# Search for top n relevant results, automatically using embeddings
query = "green"
results = memory.search(query, top_n=1)

# Validate that everything worked as expected
print(results)

if len(results) != 1:
    print("TEST FAILED: bad number of results, requested 1")
    exit(1)

result = results[0]
if not "chunk" in result.keys() or not "metadata" in result.keys():
    print("TEST FAILED: not all required keys were present in the result")
    exit(1)

if not "chunk" in result.keys():
    print("TEST FAILED: metadata not present")
    exit(1)

if result["chunk"] != "apples are green":
    print("TEST FAILED: wrong chunk returned")
    exit(1)

print("INITIALIZED AND PASSED SELF-TEST")
