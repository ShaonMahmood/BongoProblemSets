## Project Requirements

1. Ubuntu operating system
2. Python3(>=3.6)
3. git 
4. pytest module

 

## Setup Instructions
1. Open ubuntu terminal
1. Create a virtual environment and activate it.  [see here](https://docs.python.org/3/tutorial/venv.html)
2. Clone the project in your home folder. 
`git clone https://github.com/ShaonMahmood/BongoProblemSets.git`
3. cd into the cloned directory. `cd BongoProblemSets`
4. Install the requirements. `pip install -r requirements.txt`
5. Run the solutions scripts accordingly. for example, for the first problem run
`python bongo1.py`
6. To test run `pytest -v`

## Runtime
A decorator is added to every core function to measure the execution time of each solution.
to measure the time complexity we will use BigO notation. 
1. for problem 1, the solution provides a average time complexity of O(n) where n is the depth of a dictionary
2. for problem 2, average time complexity is O(n), n is depth of dictionary with object hierchy.
3. for problem 3, average time complexity is O(nlogn), n is the height of the tree