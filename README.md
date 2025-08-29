🖥️ Architecture Simulator

Simulates instruction-level execution of a simplified CPU architecture.

🚀 Overview

This project is a Python-based simulator for exploring computer architecture concepts like instruction execution, registers, memory access, and pipelines. Useful for students and engineers working on hardware-software co-design.

🛠 Tech Stack

Python 3.x

NumPy (for memory arrays)

Matplotlib (for visualizations)

✨ Features

Instruction set definition (load, store, add, branch)

Memory/register simulation

Cycle-by-cycle pipeline visualization

Detects hazards (data/control)

⚙️ Setup

Clone the repo

git clone https://github.com/<your-username>/architecture-simulator.git


Install dependencies

pip install -r requirements.txt

▶️ Usage
python simulator.py --program examples/fib.asm


Loads program file

Simulates execution

Prints cycle-by-cycle trace

🔮 Future Work

Support superscalar pipelines

Cache & branch predictor simulation

GUI visualization
