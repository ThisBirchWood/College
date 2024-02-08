- Programs that take too long to finish are useless
- Don't waste time trying to design something that's impossible to make
	- An O(1) sorting algorithm

# Function Hierarchy
- O(c) < O(log n) < O(n) < O(n log n) ......... < O(n!)
- Polynomials are classified by their highest degree:
	- n^2 + 3n 5 is O(n^2)


# Big Omega
- Lower Bound (it's absolute best scenario)
- A function is never better than it's big omega

# Big Theta
- If we have a function f(n) and it's O(n) and it's Ω(n), then it's *Big Theta* is θ(n).
- Used to describe tight bounds, between the worst and best case (Big Oh and Big Omega respectively)

# Amortization
- Meaning: To gradually write off the cost over a period

## Python List append
- The true cost of appending to a Python list of size k (average of O(1), how?)
	- If there's space in the list, c units of time to assign a value to the next cell
	- If there is not space, then
		- *kc* units of time to copy *k* values across to a new list
		- *c* units of time to assign the value
- For *simple appends*
	- It will build up a profit
- For *complex appends*
	- We can spend that profit on these
- How much should we charge to never run at a loss?
- This value is known as the *amortized* complexity