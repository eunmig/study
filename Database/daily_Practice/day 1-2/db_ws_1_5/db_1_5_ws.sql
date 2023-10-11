SELECT
    first_name, last_name, age, country, phone, balance
FROM
    users
ORDER BY
    age
LIMIT
    20
OFFSET
    40;