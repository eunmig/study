-- 1
ALTER TABLE
    animals
ADD COLUMN
    meal TEXT;

-- 2
ALTER TABLE
    animals
RENAME COLUMN
    animal_name TO name;

-- 3
ALTER TABLE
    animals    
RENAME TO
    zoo;

-- 4
DROP TABLE zoo;