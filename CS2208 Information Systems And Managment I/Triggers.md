- A trigger extends the idea of a stored procedure and uses many of the same features
- They automatically invoke (trigger) in response to a database event (insert, update or delete)

# Functions of triggers
- Checking data integrity
- Updating other tables based on changes to one table
- Supporting the automation of transactions

# Syntax
```
CREATE TRIGGER <trigger-name>
{BEFORE|AFTER} { INSERT | UPDATE | DELETE }
ON <table_name> FOR EACH ROW
trigger_body;
```

![[Pasted image 20231209194546.png]]

## Example
![[Pasted image 20231209184450.png]]

```
DELIMITER $$
CREATE TRIGGER 'studentresults_before_insert'
BEFORE INSERT ON 'studentresults' FOR EACH ROW
BEGIN
	SET NEW.total = NEW.mod1 + NEW.mod2 + NEW.mod3
	SET NEW.average = NEW.total/3
	IF NEW.average > 90 THEN
		SET NEW.grade = 'EXCELLENT!';
	ELSEIF NEW.average < 90 AND NEW.average >= 70 THEN
		SET NEW.grade = 'Very Good!';
	ELSEIF NEW.average < 70 AND NEW.average >= 55 THEN
		SET NEW.grade = 'Good';
	ELSEIF NEW.average < 55 AND NEW.average >= 40 THEN
		SET NEW.grade = 'Ok';
	ELSE
		SET NEW.grade = 'Oh dear!';
	END IF;
END $$
```