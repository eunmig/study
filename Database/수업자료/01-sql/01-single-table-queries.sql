-- 01. Querying data
SELECT
    LastName
FROM
    employees;

SELECT
    LastName, FirstName
FROM
    employees;

SELECT
    *
FROM
    employees;

SELECT
    FirstName AS '이름'
FROM
    employees;

SELECT
    Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks;

-- 02. Sorting data
-- ASC : 오름차순 (기본값)
-- DESC : 내림차순

SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName DESC;

SELECT
    Country, City
FROM
    customers
ORDER BY
    Country DESC,
    City ASC;

-- ORDER BY 활용4
SELECT
    Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;


-- NULL 정렬 예시
-- NULL도 하나의 값 (값이 없음을 표시하는 값)
-- 오름차순 정렬시 NULL이 가장 먼저 출력
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;

-- 03. Filtering data

-- DISTINCT 활용1 + 2
SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;

-- WHERE 활용1 +2
SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    -- City 필드 값이 'Prague'인 데이터
    City = 'Prague';
    -- City 필드 값이 'Prague'가 아닌 데이터
    City != 'Prague';

-- WHERE 활용3
-- 필드값이 NULL이고 국가는 USA (조건 둘다 만족)
SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    -- 조회 안됌
    -- Company = 'NULL'
    Company IS NULL
    AND Country = 'USA';

-- WHERE 활용4
-- 필드값이 NULL이거나 국가는 USA (둘중하나 만족)

SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    -- 조회 안됌
    -- Company = 'NULL'
    Company IS NULL
    OR Country = 'USA';

-- WHERE 활용5
-- 필드값이 10000 이상 500000 이하의 데이터 조회
SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 10000 AND 500000;

-- WHERE 활용6
-- 필드값이 10000 이상 500000 이하의 데이터 오름차순 조회
SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 10000 AND 500000
ORDER BY Bytes;

-- WHERE 활용7 + 8
SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    -- # Country가 'Canda', 'Germany', 'France' 인
    Country IN ('Canda', 'Germany', 'France');
    -- # Country가 'Canda', 'Germany', 'France'가 아닌
    Country NOT IN ('Canda', 'Germany', 'France');

-- WHERE 활용9
SELECT
    LastName, FirstName
FROM
    customers
WHERE
    -- 필드값이 son으로 끝나는 데이터 조회
    -- 0개 이상의 문자열과 일치하는지 확인
    LastName LIKE '%son';

-- WHERE 활용10
SELECT
    LastName, FirstName
FROM
    customers
WHERE
    -- 필드값이 4자리이면서 a로 끝나느 데이터 조회
    -- 단일 문자와 일치하는지 확인
    FirstName LIKE '___a';

-- LIMIT 활용1
SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY Bytes DESC
LIMIT 7;

-- LIMIT 활용2
SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY Bytes DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3;

-- 04. Grouping data

-- GROUP BY 예시1 + 2
-- DISTINCT ORDER BY한 결과값이랑 같음
-- 단, GROUP BY는 COUNT 가능
SELECT
    Country, COUNT(*)
FROM
    customers
GROUP BY
    Country;

-- 그룹화하여 평균값 내림차순 조회
-- GROUP BY 활용1
SELECT
    Composer, AVG(Bytes)
    -- Composer, AVG(Bytes) AS avg0fBytes
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    AVG(Bytes) DESC;
    -- avg0fBytes DESC;

-- GROUP BY 활용2
-- 에러 Invalid use of group function
SELECT
    -- Composer, AVG(Milliseconds / 60000)
    Composer, AVG(Milliseconds / 60000) AS avg0fBytes
FROM
    tracks
WHERE
    avg0fBytes < 10
GROUP BY
    Composer;

-- 에러 해결
SELECT
    Composer, AVG(Milliseconds / 60000) AS avg0fBytes
FROM
    tracks
GROUP BY
    Composer
HAVING
    avg0fBytes < 10;