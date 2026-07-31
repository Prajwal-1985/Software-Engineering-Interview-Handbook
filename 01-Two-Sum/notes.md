# 📝 Notes — Two Sum

## 📌 Problem Summary

The Two Sum problem requires finding two numbers in an array whose sum equals a given target value and returning their indices.

This problem is a classic interview question that introduces the concept of optimizing brute-force solutions using a hash map.

---

# 🎯 Key Concepts

- Arrays
- Hash Maps (Dictionary / Unordered Map)
- Complement Lookup
- Time Complexity Optimization

---

# 💡 Initial Thought

The first idea is to compare every pair of numbers.

Example:

```
for each element
    compare with every other element
```

Although simple, this approach checks many unnecessary pairs.

---

# 🚀 Optimized Idea

Instead of searching the entire array every time, store the numbers already visited in a hash map.

For every element:

```
Need = Target - Current Number
```

If the required number already exists in the hash map:

```
Answer Found ✅
```

Otherwise,

```
Store Current Number
Continue
```

---

# 📊 Complexity Analysis

### Brute Force

- Time Complexity: **O(n²)**
- Space Complexity: **O(1)**

### Hash Map

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

---

# 🔑 Important Observations

- A hash map provides average **O(1)** lookup time.
- Always check whether the complement exists **before** inserting the current element.
- Each array element should only be used once.

---

# ⚠ Common Mistakes

- Using the same element twice.
- Inserting the current value before checking for its complement.
- Returning values instead of indices.
- Forgetting to handle duplicate values correctly.

---

# 🧠 Interview Tips

If asked in an interview:

1. Explain the brute-force approach first.
2. Discuss its time complexity.
3. Identify why it is inefficient.
4. Introduce the hash map optimization.
5. Walk through a small example.
6. State the final time and space complexities.

---

# 🔄 Similar Problems

- Two Sum II
- 3Sum
- 4Sum
- Contains Duplicate
- Subarray Sum Equals K
- Two Sum in a BST

---

# 📚 What I Learned

- How hash maps reduce lookup time.
- The complement lookup technique.
- How to optimize from **O(n²)** to **O(n)**.
- The importance of choosing appropriate data structures.
- How to explain an optimized solution during interviews.

---

# 🎯 Interview Takeaway

Two Sum is one of the most frequently asked coding interview problems. Mastering this problem builds a strong foundation for solving many other array and hash map questions efficiently.
