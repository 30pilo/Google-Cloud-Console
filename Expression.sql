#3 select expression
SELECT
    Expression,
    COUNT(*) AS Total_Expressions
FROM
    `student-detection-assignment.e51l1vcvzyv8.student`
GROUP BY
    Expression
ORDER BY
    Expression;