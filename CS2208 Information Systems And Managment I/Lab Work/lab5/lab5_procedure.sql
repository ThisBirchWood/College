CREATE DEFINER=`ddf3`@`%` PROCEDURE `book_room`(
IN roomid int,
IN booker varchar(45),
IN roomname varchar(45),
IN guestnumber int,
IN eventdate varchar(45),
OUT result int)
BEGIN

DECLARE roomlimit INT;
SELECT roombookinglimit.limit into roomlimit
FROM roombookinglimit
WHERE roombookinglimit.roomname = roomname;

IF roomlimit >= guestnumber THEN
	INSERT INTO roombooking (roomid, booker, roomname, guestnumber, event_date) VALUES
		(roomid, booker, roomname, guestnumber, eventdate);
	SET result = 0;
ELSE
	SET result = 1;
END IF;

END