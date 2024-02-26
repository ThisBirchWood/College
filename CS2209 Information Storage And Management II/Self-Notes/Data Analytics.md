- Data analytics is the use of 
	- Data
	- Information tech
	- Statistical analysis
	- Quantitative Methods
	- Computational Models
- to gain valuable information and insight about decisions and business operation, such that better decisions can be made with real evidence
- This can enhance sustainability and reduce risk as much as possible

# Types of Data Analytics
![[Pasted image 20240226182429.png]]
## Descriptive Analytics
- What happened?
- This stage of data processing creates a summary of historical data to yield insightful information and prepare the data for further analysis

## Diagnostic Analytics
- Why did it happen?
- This stage of analytics investigates the reason for certain trends in the data
- Encompasses various methods such as data mining, correlations and drill-down

## Predictive Analytics
- What will happen next?
- Based off of the information gathered in the previous two stages, this stage is about predicting future trends

## Prescriptive Analytics
- What should we do next?
- This stage takes all of the data gathered so far and tries to make a decision based off of it
- It tries to make the best decision possible based off of the data to mitigate risks and take advantage of future opportunities

# Decision Models

## What is a model?
- A model is an *abstraction of representation* of a real system, idea, or object
- In simple terms, is basically a very simple version of a real system
	- Imagine that when a building is being built, having a small miniature version of the building before the building is built.
- A model helps us understand how a system / program would work without dealing with all of the complexities that come with it
- Captures the most important features

## What is a decision model?
- A decision model is a model used to understand, analyse or facilitate decision making

### Example - 3-Day Moving Average in Sales SQL
![[Pasted image 20240226183713.png]]
```mysql
SELECT
	x.date
	x.sales
	ROUND((SELECT SUM(y.sales) / COUNT(y.sales)
		   FROM sales AS y
		   WHERE DATEDIFF(x.date, y.date) BETWEEN 0 AND 2
		   AND y.category = 'Drinks' AND y.branch = 'Cork'
		), 2) AS 'MovingAvg'

FROM sales AS x
WHERE x.category = 'Drinks' AND x.branch = 'Cork'
ORDER BY x.date;
```

