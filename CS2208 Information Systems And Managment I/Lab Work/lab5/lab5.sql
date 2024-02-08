CREATE TABLE `roombookinglimit` (
`roomname` VARCHAR(45) NOT NULL,
`limit` INT NULL,
PRIMARY KEY (`roomname`));

CREATE TABLE `roombooking` (
`roomid` INT NULL,
`booker` VARCHAR(45) NULL,
`roomname` VARCHAR(45) NULL,
`guestnumber` INT NULL,
`event_date` VARCHAR(45) NULL);

INSERT INTO `roombookinglimit`(`roomname`, `limit`)
VALUES ('Double', 2),
('Triple', 3);

CALL book_room(101, 'HN', 'Double', 3, '2022-11-08', @R1);
SELECT @R1; -- 1

CALL book_room(101, 'HN', 'Triple', 3, '2022-11-08', @R2);
SELECT @R2; -- 0

SELECT * FROM roombooking;


CREATE TRIGGER `roombooking_before_insert`
BEFORE INSERT ON `roombooking` FOR EACH ROW
BEGIN
END
