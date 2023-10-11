CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);



BEGIN;
  -- weight 열이 100보다 작은 동물 삭제
  DELETE FROM zoo
  WHERE weight < 100;
-- 트랜잭션 취소
-- 아무 레코드도 삭제되지않았음
ROLLBACK;

BEGIN;
  -- eat열이 omnivore인 레코드 삭제
  -- gorilla, dog, pig 레코드 삭제
  DELETE FROM zoo
  WHERE eat = 'omnivore';
-- 트랜잭션 커밋하여 변경 사항 저장
COMMIT;

-- 최종 tiger, elephant, panda의 레코드만 남아있음
SELECT COUNT(*)
FROM zoo;
