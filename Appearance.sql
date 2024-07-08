#2 select appearance
SELECT
    Appearance,
    COUNT(*) AS Total_Appearances
FROM
    `student-detection-assignment.e51l1vcvzyv8.student`
GROUP BY
    Appearance
ORDER BY
    Appearance;
