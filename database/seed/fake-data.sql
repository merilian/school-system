USE school;

INSERT INTO Student (id, first_name, last_name, email) VALUES (1, 'Q', 'W', 'qw@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (2, 'A', 'S', 'as@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (3, 'Z', 'X', 'zx@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (4, 'E', 'R', 'er@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (5, 'D', 'F', 'df@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (6, 'C', 'V', 'cv@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (7, 'T', 'Y', 'ty@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (8, 'G', 'H', 'gh@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (9, 'B', 'N', 'bn@mail');
INSERT INTO Student (id, first_name, last_name, email) VALUES (10, 'U', 'I', 'ui@mail');

INSERT INTO Teacher (id, first_name, last_name, email) VALUES (1, 'A', 'a', 'a@mail');
INSERT INTO Teacher (id, first_name, last_name, email) VALUES (2, 'B', 'b', 'b@mail');
INSERT INTO Teacher (id, first_name, last_name, email) VALUES (3, 'C', 'c', 'c@mail');

INSERT INTO Course (name, teacher_id) VALUES ('Course A', 1);
INSERT INTO Course (name, teacher_id) VALUES ('Course B', 2);
INSERT INTO Course (name, teacher_id) VALUES ('Course C', 3);

INSERT INTO StudentCourse (student_id, course_id) VALUES (1, 1);
INSERT INTO StudentCourse (student_id, course_id) VALUES (2, 1);
INSERT INTO StudentCourse (student_id, course_id) VALUES (3, 2);
INSERT INTO StudentCourse (student_id, course_id) VALUES (4, 2);
INSERT INTO StudentCourse (student_id, course_id) VALUES (5, 2);
INSERT INTO StudentCourse (student_id, course_id) VALUES (6, 3);
INSERT INTO StudentCourse (student_id, course_id) VALUES (7, 3);
INSERT INTO StudentCourse (student_id, course_id) VALUES (8, 3);
INSERT INTO StudentCourse (student_id, course_id) VALUES (9, 3);
INSERT INTO StudentCourse (student_id, course_id) VALUES (10, 3);