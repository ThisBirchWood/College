# problem 1
INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (1, "Tony", "Dan", "IT", 5000000);

INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (2, "Dylan", "White", "IT", 1);

INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (3, "mick", "looney", "HR", 20000);

INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (4, "Michael", "Martin", "Political", 100000000);

INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (5, "Leo", "Varadkar", "Political", 5000000);

INSERT INTO `employees`(`id`, `first_name`, `last_name`, `department`, `salary`)
VALUES (6, "Danjoe", "Varadkar", "Food", 500);

# problem 2
INSERT INTO `department`(`id`, `dept`, `building`)
VALUES (1, "IT", "Western Gateway");

INSERT INTO `department`(`id`, `dept`, `building`)
VALUES (2, "Medicine", "Western Gateway");

INSERT INTO `department`(`id`, `dept`, `building`)
VALUES (3, "Engineering", "Kane");

INSERT INTO `department`(`id`, `dept`, `building`)
VALUES (4, "Political", "Kane");

INSERT INTO `department`(`id`, `dept`, `building`)
VALUES (5, "Food", "BHSB");

#problem 3
SELECT * FROM employees;

#problem 4
SELECT DISTINCT dept FROM department;

#problem 5
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

#problem 6
SELECT avg(salary) FROM employees;

#problem 7
SELECT avg(salary), department FROM employees GROUP BY department;

#problem 8
SELECT first_name, last_name, building FROM employees JOIN department ON 
	employees.department = department.dept;
    
#problem 9
SELECT avg(salary), building FROM employees JOIN department ON 
	employees.department = department.dept GROUP BY building;
    
#problem 10
SELECT * FROM employees JOIN department;