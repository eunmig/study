-- 1
SELECT first_name, country
FROM users
WHERE first_name = '건우' AND country ='경기도'

-- 2
SELECT first_name, country
FROM users
WHERE
    country not in ('경기도', '강원도')
    AND age BETWEEN 20 AND 30;