# INSA Folder - Python Projects

This folder contains two independent Python projects demonstrating different algorithmic and data structure concepts.

---

## 1. convert.py - Geez to Arabic Numeral Converter

**Purpose**: Converts Geez numerals (Ethiopian numeral system) to Arabic numerals.

### Overview
Geez is an ancient script used in Ethiopia and Eritrea. This script has its own numeral system that is quite different from the Arabic/Western numeral system. This program translates Geez numerals into their Arabic (1-9, 0-9...) equivalents.

### Features
- Supports single digits: ፩ (1) through ፱ (9)
- Supports tens: ፲ (10), ፳ (20), ፴ (30), ..., ፺ (90)
- Supports hundreds: ፻ (100)
- Supports ten-thousands: ፼ (10,000)
- Handles complex combinations of Geez numerals

### Geez Numeral System
| Geez | Arabic | Geez | Arabic |
|------|--------|------|--------|
| ፩   | 1      | ፲   | 10     |
| ፪   | 2      | ፳   | 20     |
| ፫   | 3      | ፴   | 30     |
| ፬   | 4      | ፵   | 40     |
| ፭   | 5      | ፶   | 50     |
| ፮   | 6      | ፷   | 60     |
| ፯   | 7      | ፸   | 70     |
| ፰   | 8      | ፹   | 80     |
| ፱   | 9      | ፺   | 90     |
|     |        | ፻   | 100    |
|     |        | ፼   | 10,000 |

### Example Usage
```python
from convert import geez_to_arabic

print(geez_to_arabic("፲፫"))        # Output: 13
print(geez_to_arabic("፪፯"))        # Output: 27
print(geez_to_arabic("፳፭"))        # Output: 25
print(geez_to_arabic("፻፳፭"))       # Output: 125
print(geez_to_arabic("፪፻፶"))       # Output: 250
print(geez_to_arabic("፲፪፼፫፻፵፭"))   # Output: 120345
```

### How It Works
The function maintains two variables:
- `group`: Accumulates values of digits and tens until a 100 or 10,000 multiplier is encountered
- `total`: Accumulates the final results after multiplying by 100 or 10,000

---

## 2. survive.py - The Josephus Problem Solver

**Purpose**: Solves the classic Josephus problem using a circular linked list.

### Overview
The Josephus problem is a theoretical problem in mathematics and computer science where n people stand in a circle. Starting from a designated position, the group counts off k people and eliminates every k-th person. This continues until only one person remains—the "survivor" at the safe position.

### Problem Background
According to legend, during the Jewish-Roman War, Josephus and his companions were cornered by Roman soldiers. To escape capture, they agreed to stand in a circle and eliminate every k-th person. Josephus supposedly calculated the safe position where he would be the last survivor.

### Features
- **CircularLinkedList**: A custom data structure representing people in a circle
  - `insert_end(data)`: Adds a new person to the end of the circle
  - `josephus(k)`: Simulates the elimination process and returns the safe position
- Supports any number of people (n) and any elimination step (k)

### How It Works
1. Creates a circular linked list with nodes numbered 1 to n (representing people)
2. Starting from the first person, counts k positions
3. Removes the person at the k-th position
4. Continues from the next person and repeats until only one remains
5. Returns the position of the survivor

### Example Usage
```python
from survive import CircularLinkedList

cll = CircularLinkedList()

n = int(input("Enter number of people: "))      # Example: 7
k = int(input("Enter step: "))                  # Example: 3

for i in range(1, n + 1):
    cll.insert_end(i)

winner = cll.josephus(k)
print("Safe position is:", winner)
```

### Example Scenario
- 7 people stand in a circle: 1, 2, 3, 4, 5, 6, 7
- Every 3rd person is eliminated
- Elimination order: 3, 6, 2, 7, 5, 1
- **Survivor (safe position): 4**

### Time Complexity
- Building the list: O(n)
- Josephus elimination: O(n²) in worst case (each elimination requires traversal)

### Alternative Implementation
The file includes a commented-out alternative solution using the mathematical formula:
```python
def safe_position(n, k):
    safe = 0
    for i in range(1, n + 1):
        safe = (safe + k) % i
    return safe + 1
```

---

## Running the Programs

### For convert.py
```bash
python convert.py
```
This will execute the test cases and display the conversions from Geez to Arabic numerals.

### For survive.py
```bash
python survive.py
```
This will prompt you to enter:
- Number of people in the circle
- The elimination step (every k-th person)

Then it will display the safe position.

---

## Use Cases

### convert.py
- Learning about different numeral systems
- Processing Ethiopian texts that use Geez numerals
- Cultural and linguistic computing applications

### survive.py
- Understanding circular data structures
- Learning algorithmic problem-solving
- Applications in scheduling, elimination tournaments, or simulation scenarios

---

## Author Notes
Both programs demonstrate fundamental computer science concepts:
- **convert.py**: String parsing, dictionary mapping, and numeral system logic
- **survive.py**: Linked lists, circular data structures, and algorithmic elimination logic

