INSERT INTO employee (fname, lname, ssn, bdate, address, salary) VALUES
("John", "Smith", 12345678, "1965-01-09", "731 Western Road", 30000),
("Franklin", "Wong", 333444555, "1955-12-08", "638 Eastern Road", 40000),
("Alicia", "Zelaya", 999888777, "1968-07-19", "332 Southern Castle", 25000),
("Jennifer", "Wallce", 98765432, "1941-06-20", "291 Berry Road", 43000),
("Ramesh", "Narayan", 66688444, "1962-09-15", "975 Fire Oak", 38000),
("Joyce", "English", 17645673, "1972-07-31", "563 Rice Farm", 25000),
("Ahmad", "Jahbar", 987879878, "1969-03-29", "980 Eastern Gateway", 25000),
("James", "Borg", 23456754, "1937-11-10", "450 Good Stone", 55000);

ALTER TABLE employee MODIFY id INT(10) AUTO_INCREMENT;

INSERT INTO project (pnumber, pname) VALUES
("1", "ProductX"),
("2", "ProductY"),
("3", "ProductZ"),
("4", "core i9 14900k"),
("5", "rtx 5090");

INSERT INTO works_on (essn, pno, hours) VALUES
(23456754, 5, 21),
(23456754, 5, 21),
(23456754, 5, 21),
(23456754, 5, 21),
(12345678, 1, 2422),
(333444555, 1, 453);

#problem 2
SELECT hours FROM works_on JOIN employee ON ssn = essn WHERE fname = "John" AND lname = "Smith";#

#problem 3
SELECT SUM(salary), AVG(salary) FROM employee;

#problem 4
SELECT SUM(salary), AVG(salary) FROM project JOIN works_on JOIN employee ON ssn = essn AND pno = pnumber WHERE pname = "ProductX";

