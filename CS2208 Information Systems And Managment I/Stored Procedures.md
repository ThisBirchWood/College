- Most DBMS allow us to define both stored procedures and functions
	- We've already used some, such as SUM() and AVG()
- Example:
```
CREATE PROCEDURE `book_room`( 
	IN roomid int, 
	IN booker varchar(45), 
	IN roomname varchar(45), 
	IN guestnumber int, 
	IN eventdate varchar(45), 
	OUT result int) 
	
BEGIN 
	
	DECLARE roomlimit int; 
	SELECT roombookinglimit.limit into roomlimit FROM roombookinglimit WHERE roombookinglimit.roomname = roomname; 
	
	IF roomlimit >= guestnumber THEN 
		INSERT INTO roombooking values (roomid, booker, roomname, guestnumber, eventdate); 
		SET result = 0; 
	ELSE 
		SET result = 1; 
	END IF; 
	
END
```

**Usage**
```
-- Example 1: Booking a room within the limit 
CALL book_room(1, 'John Doe', 'Conference Room A', 10, '2023-01-01', @result); 
SELECT @result as Result; -- This should return 0 indicating successful booking. 

-- Example 2: Attempting to book a room beyond the limit 
CALL book_room(2, 'Jane Smith', 'Conference Room B', 15, '2023-02-01', @result); 
SELECT @result as Result; -- This should return 1 indicating that the booking failed.
```