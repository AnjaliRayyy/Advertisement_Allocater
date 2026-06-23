# 📺 Advertisement Slot Allocation System

A web-based application that helps media companies allocate advertisement slots across television or digital platforms to **maximize revenue**. The system compares multiple **DSA and optimization algorithms** to generate the most efficient allocation plan under slot time constraints.

Built using **Python** and :contentReference[oaicite:0]{index=0}.

---

## 🚀 Features

- Upload advertisement dataset (`.txt` / `.csv`)
- Configure multiple ad slots (Morning, PrimeTime, Evening)
- Generate optimized advertisement allocation plans
- Compare multiple algorithms based on performance
- Analyze:
  - Revenue Generated
  - Execution Time
  - Slot Utilization
- Export allocation report as CSV

---

## 🛠 Tech Stack

- Python  
- :contentReference[oaicite:1]{index=1}  
- Pandas  
- NumPy  
- Matplotlib  
- Plotly  

---

## 🧠 Algorithms Implemented

### 1. Greedy Algorithm
- Selects ads based on highest **Budget / Duration ratio**
- Fast but not always optimal  
- Complexity: **O(n log n)**  

### 2. Dynamic Programming (0/1 Knapsack)
- Finds mathematically optimal allocation  
- Maximizes revenue under slot constraints  
- Complexity: **O(nW)**  

### 3. Priority Queue Scheduling
- Prioritizes advertisers with higher priority scores  
- Uses **Heap / Priority Queue**  
- Complexity: **O(n log n)**  

### 4. Branch and Bound
- Explores combinations while pruning inefficient states  
- Produces optimal solution  
- Complexity: **O(2ⁿ)** worst case  

---

## 📂 Project Structure

```text
AdSlotAllocator/
│
├── app.py
│
├── algorithms/
│   ├── greedy.py
│   ├── priority_queue.py
│   ├── knapsack.py
│   └── branch_bound.py
│
├── utils/
│   ├── parser.py
│   ├── metrics.py
│   └── visualization.py
│
└── datasets/
```

---

## 📄 Dataset Format

```text
Ad_ID,Duration,Budget,Priority,Preferred_Slot
```

Example:

```text
AD001,30,5000,8,Morning
AD002,45,8500,9,PrimeTime
AD003,60,12000,7,Evening
```

---

## 📊 Performance Metrics

The system compares algorithms based on:

- Revenue Generated  
- Runtime Performance  
- Slot Utilization Percentage  

Visualizations include:

- Revenue Comparison Chart  
- Runtime Comparison Chart  
- Utilization Comparison Chart  

---

## ▶️ Installation

Clone repository:

```bash
git clone <repo_url>
cd AdSlotAllocator
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

## 📌 Concepts Used

- Data Structures  
- Dynamic Programming  
- Scheduling Algorithms  
- Optimization Techniques  
- Branch and Bound  
- File Handling  
- Data Visualization  

---

## 🔮 Future Improvements

- Multi-platform allocation (TV / OTT / Social Media)  
- Conflict-aware ad scheduling  
- Machine Learning based revenue prediction  
- Database integration and deployment  

---

## 👨‍💻 Project Purpose

A university project focused on applying **DSA and optimization algorithms** to solve real-world advertisement scheduling and revenue maximization problems.
