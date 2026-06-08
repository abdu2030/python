# Classification Algorithms — Explained Simply
### Logistic Regression · Support Vector Machine · Naive Bayes

---

## Before We Start — The Key Difference From Linear Regression

You already understand Linear Regression. The formula is:

```
Price = (w1 × feature1) + (w2 × feature2) + ... + bias
```

It gives you a **number** — a house price, a temperature, a salary. Any number on the number line.

But here is the problem: what if you do not want a number? What if you want a **category**?

> *"Is this tweet Positive or Negative?"*

Linear Regression would give you answers like `0.73` or `1.2` or `-0.4`. Those are not categories. You cannot hand someone a prediction of `1.2` and say "that is positive." You need a decision: **yes or no, positive or negative, spam or not spam.**

This is what **Classification** solves. The three algorithms we use — Logistic Regression, SVM, and Naive Bayes — are all classification algorithms. They all take in features and output a category, but they each do it in a completely different way.

---

## Part 1 — Logistic Regression

### The Problem with Using Linear Regression for Classification

Imagine trying to classify tweets as positive (1) or negative (0) using Linear Regression.

The model might give you:
```
"I love this phone" → 0.9
"This is okay" → 0.5
"I hate this" → 0.1
```

That seems reasonable. But then it might also give you:
```
"I absolutely LOVE LOVE LOVE this product!!!" → 2.4
"This is literally the worst thing EVER!!!" → -1.7
```

Values above 1 or below 0 make no sense for classification. There is nothing that is "2.4 positive." You need to force the output to stay between 0 and 1 — and that is exactly what Logistic Regression does.

---

### The Sigmoid Function — The Core of Logistic Regression

Logistic Regression does the same calculation as Linear Regression:

```
z = (w1 × word1_score) + (w2 × word2_score) + ... + bias
```

But then it does one extra thing — it passes `z` through the **sigmoid function**:

```
probability = 1 / (1 + e^(-z))
```

This formula looks scary but the idea is simple. No matter what `z` is — whether it is `0.3`, `15`, or `-100` — the sigmoid squashes it into a number between 0 and 1.

If you plot it, it looks like an S-curve:

```
    1.0  |                           ─────────────
         |                      ────╯
    0.5  |              ──╳────╯
         |         ────╯
    0.0  |─────────
         └─────────────────────────────────
              very negative    0    very positive
              z values
```

- When `z` is very large (very positive text) → sigmoid output approaches 1.0
- When `z` is very small (very negative text) → sigmoid output approaches 0.0
- When `z` is exactly 0 → sigmoid output is exactly 0.5

The output is now a **probability**: *"I am 87% confident this tweet is positive."*

To make the final decision, you apply a threshold:
- If probability ≥ 0.5 → predict **Positive**
- If probability < 0.5 → predict **Negative**

---

### A Concrete Example

Take the tweet: *"This phone is amazing and I love it"*

After TF-IDF, the model might see the following key features:

| Word | TF-IDF Score | Weight learned | Contribution |
|---|---|---|---|
| `amazing` | 0.45 | +2.1 | +0.945 |
| `love` | 0.38 | +1.8 | +0.684 |
| `phone` | 0.20 | +0.2 | +0.040 |
| bias | — | -0.5 | -0.500 |

```
z = 0.945 + 0.684 + 0.040 - 0.500 = 1.169
probability = 1 / (1 + e^(-1.169)) = 0.76
```

Result: **76% confident → Positive ✅**

Now a negative tweet: *"This is the worst product I ever bought"*

| Word | TF-IDF Score | Weight learned | Contribution |
|---|---|---|---|
| `worst` | 0.51 | -2.4 | -1.224 |
| `ever` | 0.22 | -0.4 | -0.088 |
| bias | — | -0.5 | -0.500 |

```
z = -1.224 - 0.088 - 0.500 = -1.812
probability = 1 / (1 + e^(1.812)) = 0.14
```

Result: **14% positive → classified as Negative ✅**

---

### How Logistic Regression Learns

It uses the same core idea as Linear Regression — start with random weights, make a prediction, measure how wrong it was, adjust the weights. Repeat thousands of times.

The difference is what "how wrong it was" measures. Instead of mean squared error (used in regression), Logistic Regression uses **cross-entropy loss**:

```
If the correct answer is Positive (1):
    loss = -log(predicted_probability)

If the correct answer is Negative (0):
    loss = -log(1 - predicted_probability)
```

The intuition: if the correct answer is Positive and the model said 0.99 probability of positive — the loss is tiny (good job). If the model said 0.02 probability of positive — the loss is huge (very wrong). The model adjusts its weights to reduce this loss.

---

### Why Is It Called "Regression" If It Classifies?

Historical quirk. It was invented as a variant of regression for situations where the output was binary. The word "regression" stuck. Internally it still does a linear combination of weights — it just squashes the final output through sigmoid to turn it into a probability. Think of it as **"regression that outputs a probability instead of a raw number."**

---

## Part 2 — Support Vector Machine (SVM)

### The Core Idea — Finding the Best Dividing Line

Imagine you have plotted tweets on a 2D graph. Green dots are positive tweets, red dots are negative. You want to draw a line that separates them.

```
                    green ●     green ●
                  green ●
                                        green ●
─────────── ?  ─────────────────────────────────
          red ●
       red ●       red ●
                          red ●
```

There are infinitely many lines you could draw that would separate the two groups. A logistic regression would pick one. An SVM asks a different question:

> *"Of all the possible lines, which one has the MAXIMUM distance to the nearest data points on each side?"*

That distance is called the **margin**. SVM finds the line with the widest margin.

```
                    green ●     green ●
         ┄ ┄ ┄ ┄ ┄ ─ ─ ─ ─ ─ ─  ← upper margin boundary
         ───────── DECISION LINE ─────────────
         ┄ ┄ ┄ ┄ ┄ ─ ─ ─ ─ ─ ─  ← lower margin boundary
          red ●
       red ●       red ●
```

The dotted lines are called the **margin boundaries**. The solid line in the middle is the **decision boundary**. SVM maximizes the gap between the two dotted lines.

---

### What Are Support Vectors?

Look at the diagram above. Most data points are far from the boundary lines — they do not influence where the line is drawn. Only the data points that are closest to each boundary matter. These closest points are called **support vectors**.

If you removed every other data point from the dataset and kept only the support vectors, the SVM would draw the exact same line. The entire model is defined by just those few critical points.

This is different from Logistic Regression, which considers every single data point in every update. SVM focuses only on the hardest cases — the ones right on the edge.

---

### Why Maximum Margin Is Better

Consider two possible lines that both correctly separate the data:

**Line A** (small margin): sits very close to some red dots
```
If a new tweet lands near those red dots → tiny perturbation → wrong side → wrong prediction
```

**Line B** (maximum margin): sits as far as possible from all dots
```
A new tweet has to be very far into the wrong territory before it gets misclassified
```

Maximum margin = maximum tolerance for new, unseen data = better generalization.

This is why SVM tends to outperform other classifiers on text data, where the training set never fully covers all possible ways someone could express a sentiment.

---

### Linear vs Non-Linear — The Kernel Trick

Sometimes data is not linearly separable. You cannot draw a straight line to separate the groups.

**Example in 2D (cannot separate with a line):**
```
    red ●    green ●   red ●
  green ●                   green ●
    red ●    green ●   red ●
```

SVM solves this with the **kernel trick**: it mathematically transforms the data into a higher-dimensional space where a straight line (hyperplane) CAN separate the groups.

Think of it like this. You have red and green marbles mixed on a table. You cannot draw a line to separate them. But if you pick the table up and tilt it, the marbles roll and separate by color. The "tilting" is the kernel — you changed the perspective until separation became possible.

For text classification with TF-IDF, a **linear kernel** almost always works because:
- TF-IDF creates 50,000 dimensions
- In very high-dimensional spaces, data is almost always linearly separable
- There is almost always some hyperplane that cleanly separates positive from negative tweets

This is why `LinearSVC` (linear kernel SVM) is the standard for text classification. Non-linear kernels add computation without adding benefit when you already have tens of thousands of dimensions.

---

### SVM in the Context of Our Model

In our stacking classifier, the SVM is the **final decision maker** — the meta-learner. It receives:
- All 50,000 TF-IDF features (raw word signals)
- The probability scores from Logistic Regression
- The probability scores from Naive Bayes

The SVM's decision boundary in this case is a hyperplane in a ~50,004-dimensional space. It finds the maximum-margin separator that uses all of that information simultaneously. No human can visualize this — but mathematically it works exactly like the 2D diagram above, just in many more dimensions.

---

## Part 3 — Naive Bayes

### Start With a Simple Question About Probability

Imagine you know the following from past data:

- 500 tweets were positive, 500 were negative (1000 total)
- The word `"love"` appeared in 380 positive tweets and 20 negative tweets
- The word `"terrible"` appeared in 10 positive tweets and 350 negative tweets

Now you see a new tweet: *"I love this."*

You ask yourself: given that this tweet contains the word `"love"`, what is the probability it is positive?

```
P(Positive | tweet contains "love") = ?
```

This is what Naive Bayes calculates using **Bayes' Theorem**:

```
P(Positive | words in tweet) = P(words | Positive) × P(Positive) / P(words)
```

Let's break this down:

| Term | What it means | In our example |
|---|---|---|
| `P(Positive)` | Prior probability — how often are tweets positive overall? | 500/1000 = 0.5 |
| `P(words \| Positive)` | How often do these words appear in positive tweets? | |
| `P(Positive \| words)` | What we want — given these words, is it positive? | |

---

### Calculating Word Probabilities

For each word, Naive Bayes calculates:

```
P("love" | Positive)  = 380/500 = 0.76
P("love" | Negative)  = 20/500  = 0.04
```

This tells the model: the word `"love"` is 19× more likely to appear in a positive tweet than a negative one.

For a tweet with multiple words — say *"I love this product"* — Naive Bayes multiplies the probabilities of each word together:

```
P(Positive | "love", "product") 
    = P("love" | Positive) × P("product" | Positive) × P(Positive)
    = 0.76 × 0.45 × 0.5
    = 0.171

P(Negative | "love", "product") 
    = P("love" | Negative) × P("product" | Negative) × P(Negative)
    = 0.04 × 0.30 × 0.5
    = 0.006
```

Since `0.171 > 0.006`, the tweet is classified as **Positive**.

---

### The "Naive" Part — And Why It Still Works

The word "naive" refers to a simplifying assumption: **Naive Bayes treats every word as completely independent of every other word.**

In reality, words are not independent. If a tweet contains `"not"`, it completely changes the meaning of what follows. `"not good"` is very different from `"good"`. Naive Bayes does not model this — it treats `"not"` and `"good"` as separate, unrelated signals.

So why does it still work well enough to be useful?

Because when you have thousands of features (words), the overall signal is strong enough that small dependencies between individual words get washed out. Even if the model is slightly wrong about `"not good"`, the rest of the tweet usually provides enough correct signal to push toward the right class.

Naive Bayes is like a very fast estimator that is slightly wrong about the relationships between words but still captures the big picture correctly. That speed is actually useful — it trains almost instantly compared to SVM.

---

### The Log Trick — Preventing Very Small Numbers

Multiplying hundreds of small probabilities together creates an extremely tiny number:

```
0.76 × 0.45 × 0.22 × 0.18 × 0.33 × ... × 0.41 = 0.0000000001
```

Computers lose precision with numbers this small. The fix is to take the **logarithm** of all probabilities and add instead of multiply:

```
log(0.76) + log(0.45) + log(0.22) + ... = easier to handle number
```

This works because `log(a × b) = log(a) + log(b)`. It is mathematically identical, just more stable. This is why you will sometimes see Naive Bayes referred to as computing "log-probabilities."

---

## Part 4 — How All Three Are Different From Each Other

### The Fundamental Question Each Asks

| Algorithm | Question it asks | How it decides |
|---|---|---|
| **Logistic Regression** | "What is the probability this is positive?" | Applies sigmoid to a weighted sum of features |
| **SVM** | "Which side of the maximum-margin boundary is this on?" | Finds geometric position in feature space |
| **Naive Bayes** | "Which class makes these words most probable?" | Multiplies word probabilities together |

These are three completely different philosophies.

- Logistic Regression thinks in terms of **probability from weighted features**
- SVM thinks in terms of **geometry and distance from a boundary**
- Naive Bayes thinks in terms of **how likely these words are to come from each class**

---

### A Restaurant Analogy

Imagine classifying whether a restaurant review is good or bad.

**Logistic Regression** is like a food critic who has memorized how much each word typically predicts quality. She gives `"delicious"` a weight of +2.3 and `"bland"` a weight of -1.8, adds up all the weighted words, and calculates a confidence score.

**SVM** is like a health inspector who draws a line between "clearly good" and "clearly bad" restaurants and makes sure that line stays as far as possible from borderline cases. For any new restaurant, he just checks which side of the line it falls on.

**Naive Bayes** is like a statistician who has counted how often each word appeared in past good and bad reviews. For a new review, she looks up each word's historical frequency in each category and multiplies them together to decide.

All three would probably classify the same reviews correctly — they just think about the problem differently.

---

### Which One Is Best for Text?

The short answer: **it depends on the dataset**, but SVM wins most often on text:

| Property | Logistic Regression | SVM | Naive Bayes |
|---|---|---|---|
| Training speed | Fast | Medium | Very fast |
| Performance on text | Very good | Best | Good |
| Handles high dimensions | Well | Excellent | Well |
| Handles noisy data | Okay | Very well | Okay |
| Needs probability output | Yes | No (by default) | Yes |
| Interpretability | High | Medium | High |

SVM wins on text classification because:
1. High-dimensional TF-IDF space suits it perfectly
2. Maximum margin makes it robust to the noise in social media text
3. It does not need to estimate probabilities — it just needs to find the right side

Naive Bayes wins when:
- You need something fast with very little data
- You need a simple baseline to compare against

Logistic Regression is a strong middle ground — almost as good as SVM on text, faster to train, and gives probability outputs.

---

## Part 5 — How All Three Differ From Linear Regression

| Property | Linear Regression | Logistic Regression | SVM | Naive Bayes |
|---|---|---|---|---|
| **Task type** | Predicts a number | Predicts a class | Predicts a class | Predicts a class |
| **Output** | Any number | Probability (0 to 1) | Class label | Class label |
| **Decision** | No decision, just a value | Use 0.5 threshold | Which side of hyperplane | Higher probability class |
| **Example output** | "$245,000" | "87% positive" | "Positive" | "Positive" |
| **Y axis in graph** | The prediction itself | Not a separate axis | Not a separate axis | Not a separate axis |
| **What the "line" does** | Fits through the data | Separates the classes | Separates with max margin | No explicit line |
| **When things go wrong** | Predicts wrong number | Classifies wrong class | Classifies wrong class | Classifies wrong class |

The most important conceptual difference:

> **Linear Regression**: the line passes THROUGH the data points, trying to be close to all of them
>
> **Classification algorithms**: the line passes BETWEEN the data groups, trying to separate them

They solve completely different problems with partially similar math.

---

## Part 6 — How the Three Work Together in Our Model (Stacking)

In our sentiment analysis system, we use all three in a hierarchy:

```
TF-IDF Features (50,000 dimensions)
        │
   ┌────┴────┐
   │         │
   ▼         ▼
  LR        NB          ← These two are base models
   │         │            They each make their own prediction
   └────┬────┘            and output confidence scores
        │
        + original TF-IDF features (passthrough=True)
        │
        ▼
      SVM                ← The final decision maker
        │                  It sees everything: TF-IDF + LR score + NB score
        ▼
   POSITIVE / NEGATIVE
```

**Why this combination works better than any single model:**

1. **LR** is good at capturing the overall weighted signal across all 50,000 words
2. **NB** is good at capturing how statistically unusual certain words are for each class
3. **SVM** sees both of their predictions alongside the raw features and learns when to trust LR more, when to trust NB more, and what the raw features alone tell it that neither base model captured

For example, on a sarcastic tweet like *"Oh great, another delay 🙄"*:
- LR might see "great" and lean positive
- NB might see "delay" and lean negative
- SVM sees the conflict between them + the emoji features and makes the final call

No single algorithm would handle all cases as well as the combination.

---

## Part 7 — Quick Reference Summary

### What Each Algorithm Actually Does, In One Sentence

**Linear Regression**: Find the best straight line through data and read off a predicted value.

**Logistic Regression**: Do the same weighted sum as linear regression, but squash the output into a probability using the sigmoid function and classify based on that probability.

**SVM**: Find the dividing line between classes that has the maximum gap from the nearest data points on either side.

**Naive Bayes**: Count how often each word appeared in positive vs negative examples, then for a new input, multiply together the likelihood of each word and pick the class with the higher total probability.

---

### The Three Core Concepts to Remember for the Presentation

**1. They all learn from labeled examples:**
All three algorithms see thousands of labeled tweets ("positive" or "negative") during training and adjust their internal parameters to minimize mistakes.

**2. They all produce a class label, not a number:**
Unlike linear regression which outputs a raw price, all three output a category. The math that produces that category is different for each.

**3. SVM is the strongest for our task because of geometry:**
Our TF-IDF features create 50,000 dimensions. In that high-dimensional space, the classes are almost always separable with a flat surface. SVM finds that surface and maximizes the gap around it — making it the most robust classifier for noisy, high-dimensional text.
