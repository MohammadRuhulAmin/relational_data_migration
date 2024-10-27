CREATE TABLE tableA(
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE
);

CREATE TABLE tableA_child(
   id INT(11) AUTO_INCREMENT PRIMARY KEY,
   table_a_id INT(11) UNIQUE,
   info VARCHAR(255) DEFAULT NULL

);

CREATE TABLE tableA_child_children(
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  table_a_child_children_id INT(11) UNIQUE,
  info VARCHAR(255) DEFAULT NULL
);