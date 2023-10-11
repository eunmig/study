CREATE TABLE users(
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber NOT NULL,
    gender INTEGER,
    addresss NOTNULL DEFAULT 'no address'
);

-- phoneNumber 칼럼 이름을 number으로 변경
ALTER TABLE users
RENAME COLUMN phoneNumber TO number;

-- users 테이블을 데이터베이스에서 제거
DROP TABLE users;