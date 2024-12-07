# Python-Assignment  
# Distributed System Simulation

## Overview
It contains project implementation on the distributed system that uses several SQLite databases to store related `Users`, `Orders`, and `Products`. The system makes concurrent inserts on databases using threading in order to achieve reality simulation.

## Characteristics
- **Concurrency**: It simulates three independent SQLite databases opened and simultaneously inserting multiple operations.
- **Three Models:**
U- **Users**: Stores user information like name and email.
- **Orders**: Provides views regarding orders placed by users for particular products.
Some products include; 
 Products information. This includes name and price.
- **Database:**
- `users.db`- storage for user data.
- `products.db` : Product data.
- `orders.db`: it stores order data.

## Prerequisites
To run this project you will need:
Install of **Python 3.x**.
- SQLite (SQLite is included with any Python installation. No installation is needed).
What is needed
Knowledge of threading and SQLite in Python.

## Setup

### 1. Clone the repository
END
git clone https://github.com/yourusername/DistributedSystemSimulation.git
cd DistributedSystemSimulation
END

### 2. Create and Activate a Virtual Environment
- On Windows:

python -m venv venv
.venv\Scripts\Activate
`

### 3. Install Required Dependencies

pip install sqlite3
End

(Note: 'sqlite3' comes standard with Python, but you can install it yourself if you need to.)

#### 4. Run the Setup Script
Execute the setup script to create SQLite databases and tables:
END
python database_setup.py
```

5. Run the Main Program
Execute the command below to execute the concurrent insert into the databases:
```bash
py main.py
:

This will come prepopulated with sample data in the `Users`, `Products`, and `Orders` tables with outcomes.

## File Structure
the
DistributedSystemSimulation/
END
├── database_setup.py  # Python script that creates the SQLite databases and tables
└── main.py             # concurrently inserts data into the databases
└── venv/               # Virtual environment directory
|   └── .
README.md            # Project description and getting started instructions
└── .
END

## Sample Output Running `main.py`, the output will look like this:

End
