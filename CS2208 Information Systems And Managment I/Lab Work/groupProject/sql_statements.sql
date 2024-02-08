#entities
CREATE TABLE locations (
	location_id INT PRIMARY KEY NOT NULL,
    postcode VARCHAR(7),
    floor INT,
    room INT
);

INSERT INTO locations (location_id, postcode, floor, room) VALUES (0, 'T12XF62', 1, 107);

CREATE TABLE plans (
	plan_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(30),
    description TEXT,
    price INT
);

INSERT INTO plans (plan_id, title, description, price) VALUES (0, 'Basic Plan', 'No extra features', 0);

CREATE TABLE accounts (
	username VARCHAR(100) PRIMARY KEY NOT NULL,
    password VARCHAR(45),
    email VARCHAR(45),
    location_id int,
    plan_id int,
    
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

CREATE TABLE job_seekers (
	username VARCHAR(100) PRIMARY KEY NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone_number VARCHAR(20),
    
    FOREIGN KEY (username) REFERENCES accounts(username)
);

CREATE TABLE company_branches (
	username VARCHAR(100) PRIMARY KEY NOT NULL,
    name VARCHAR(20),
    employee_count INT,
    description TEXT,
    
    FOREIGN KEY (username) REFERENCES accounts(username)
);

CREATE TABLE jobs (
	job_id INT PRIMARY KEY NOT NULL,
    salary INT,
    type VARCHAR(30),
    company_username VARCHAR(100),
    
    FOREIGN KEY (company_username) REFERENCES company_branches(username)
);

CREATE TABLE applications (
	application_id INT PRIMARY KEY NOT NULL,
    date_applied DATETIME,
    status TEXT,
    content TEXT,
    job_seeker_username VARCHAR(100),
    job_id INT,
    
    FOREIGN KEY (job_seeker_username) REFERENCES job_seekers(username),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

CREATE TABLE skills (
	skill_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(20),
    description TEXT
);

CREATE TABLE notifications (
	notification_id INT PRIMARY KEY NOT NULL,
    content TEXT,
    date_sent DATETIME,
    status VARCHAR(20),
    username VARCHAR(100),
    
    FOREIGN KEY (username) REFERENCES accounts(username)
);

CREATE TABLE company_reviews(
	review_id INT PRIMARY KEY NOT NULL,
    rating INT,
    content TEXT,
    date_reviewed DATETIME,
    company_username VARCHAR(100),
    
    FOREIGN KEY (company_username) REFERENCES company_branches(username)
);

CREATE TABLE industries(
	industry_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(20),
    description TEXT
);

## Many to Many relationships that require an extra table
CREATE TABLE job_seeker_skills (
	job_seeker_username VARCHAR(100),
    skill_id INT,
    
    FOREIGN KEY (job_seeker_username) REFERENCES job_seekers(username),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE jobs_require_skills(
	job_id INT,
    skill_id INT,
    
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE company_in_industries(
	industry_id INT,
    company_username VARCHAR(100),
    
    FOREIGN KEY (industry_id) REFERENCES industries(industry_id),
    FOREIGN KEY (company_username) REFERENCES company_branches(username)
);


## Insert dummy data




