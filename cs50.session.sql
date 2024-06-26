
-- creat db
--@block

CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS department (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS level(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_id INT,
    FOREIGN KEY(department_id) REFERENCES department(id)
);

CREATE TABLE IF NOT EXISTS class(
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_number INT NOT NULL,
    level_id INT,
    FOREIGN KEY(level_id) REFERENCES level(id)
);

CREATE TABLE IF NOT EXISTS teacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS student(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(50),
    class_id INT , -- edited to class_id
    FOREIGN KEY(class) REFERENCES class(id)
);


CREATE TABLE IF NOT EXISTS subject(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    level_id INT,
    coefs JSON,
    FOREIGN KEY(level_id) REFERENCES level(id)
);

CREATE TABLE IF NOT EXISTS level_subject(
    level_id INT,
    subject_id INT,
    coef INT,
    PRIMARY key(level_id, subject_id),
    FOREIGN KEY(level_id) REFERENCES level(id),
    FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE IF NOT EXISTS teacher_class_subject(
    teacher_id INT,
    class_id INT,
    subject_id INT,
    PRIMARY key(teacher_id, class_id, subject_id),
    FOREIGN KEY(teacher_id) REFERENCES teacher(id),
    FOREIGN KEY(class_id) REFERENCES class(id),
    FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE IF NOT EXISTS grade(
    id INT AUTO_INCREMENT PRIMARY KEY,
    grade float,
    exam float,
    tp float,
    td float,
    subject_id INT,
    student_id INT,
    FOREIGN KEY (subject_id) REFERENCES subject(id),
    FOREIGN key (student_id) REFERENCES student(id)
);


--initialization admin , department, level, class
-- @block

INSERT INTO admin(username, password) 
VALUES ('admin',
'scrypt:32768:8:1$YEdQoo1cPC1qoE0L$35a4227fb0c9042b49187505e3c19a25525eaf1fc32d562919372ed22f1c09889fedb7151d68a0c319924cc392895b9ef4f0058fc0fda6c0ccb9607f2483c24');

INSERT INTO department(name) VALUES ('Computer Science');

INSERT INTO level(name, department_id) VALUES ('L1', 1);
INSERT INTO level(name, department_id) VALUES ('L2', 1);
INSERT INTO level(name, department_id) VALUES ('L3', 1);

INSERT INTO class(class_number, level_id) VALUES (1, 1);
INSERT INTO class(class_number, level_id) VALUES (2, 1);
INSERT INTO class(class_number, level_id) VALUES (3, 1);

INSERT INTO class(class_number, level_id) VALUES (1, 2);
INSERT INTO class(class_number, level_id) VALUES (2, 2);
INSERT INTO class(class_number, level_id) VALUES (3, 2);

INSERT INTO class(class_number, level_id) VALUES (1, 3);
INSERT INTO class(class_number, level_id) VALUES (2, 3);
INSERT INTO class(class_number, level_id) VALUES (3, 3);



--@block
-- edit class to class_id in student tabel

ALTER TABLE student RENAME COLUMN class TO class_id;