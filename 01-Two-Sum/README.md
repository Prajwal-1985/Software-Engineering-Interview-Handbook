# 📌 01 — Two Sum

## Difficulty

🟢 Easy

---

## Companies

Amazon • Google • Microsoft • Meta • Apple • Adobe • Uber • Goldman Sachs

---

# 📖 Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to the target.

You may assume:

- Exactly one solution exists.
- The same element cannot be used twice.

---

# 🧩 Example

### Input

```text
nums = [2,7,11,15]

target = 9
```

### Output

```text
[0,1]
```

### Explanation

```
2 + 7 = 9
```

Therefore,

```
Indices = 0,1
```

---

# 🎯 Interview Goal

This problem evaluates your understanding of

- Arrays
- Hash Maps
- Time Complexity Optimization

---

# 💡 Approach 1

## Brute Force

Compare every possible pair.

### Complexity

Time

```
O(n²)
```

Space

```
O(1)
```

---

# 🚀 Approach 2

## Hash Map

Store previously visited numbers.

For every element

```
Need = Target − Current Number
```

If

```
Need
```

already exists,

return both indices.

---

# 🔍 Dry Run

```
Current = 2

Need = 7

Map = {}
```

Store

```
2 → Index 0
```

---

```
Current = 7

Need = 2
```

Found

```
Answer

0 1
```

---

# ⏱ Complexity

| Solution | Time | Space |
|----------|------|------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

---

# 💻 Languages

✅ C

✅ C++

✅ Java

✅ Python

---

# 📂 Files

```
README.md
notes.md
solution.c
solution.cpp
TwoSum.java
solution.py
```

---

# 📚 Key Takeaways

- Hash Maps provide constant-time lookup.
- Optimizing from O(n²) to O(n) significantly improves performance.
- This problem introduces the complement lookup pattern, which appears in many interview questions.

---

# 🔗 Related Problems

- Two Sum II
- 3Sum
- 4Sum
- Contains Duplicate
- Subarray Sum Equals K

---

# 📝 Personal Notes

Document your observations and learning points in `notes.md` after solving the problem yourself.
