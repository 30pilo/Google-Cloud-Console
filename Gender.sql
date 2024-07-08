#1 select gender
SELECT
    Gender,
    COUNT(*) AS Total_Gender
FROM
    `student-detection-assignment.e51l1vcvzyv8.student`
GROUP BY
    Gender
ORDER BY
    Gender;
