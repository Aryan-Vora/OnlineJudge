# Online Judge Problems

This repository contains a bunch of problems I've solved.

## Structure

Each problem is stored in its own directory with the following structure:

```
problem-number/
├── main.py
├── input.txt
└── p[problem-number].pdf
```

- `main.py` - The Python script containing the solution for the problem.
- `input.txt` - The input file containing test cases.
- `p[problem-number].pdf` - The PDF file containing the problem statement.

## Running the Code

To run the code for a problem, navigate to the problem's directory and use the following commands based on your operating system and terminal:

### Windows (PowerShell)

```powershell
Get-Content input.txt | python main.py
```

### Linux / macOS (Bash)

```bash
cat input.txt | python3 main.py
```
