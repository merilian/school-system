CREATE TABLE Grade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grade INT NOT NULL,
    student_course_id INT NOT NULL,
    FOREIGN KEY (student_course_id) REFERENCES StudentCourse(id)
);