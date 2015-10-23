 CREATE TABLE person
    -> (person_id SMALLINT UNSIGNED,
    -> fname VARCHAR(20),
    -> lname VARCHAR(20),
    -> gender ENUM('M','F'),
    -> birth_date DATE,
    -> street VARCHAR(30),
    -> city VARCHAR(20),
    -> state VARCHAR(20),
    -> country VARCHAR(20),
    -> postal_code VARCHAR(20),
    -> CONSTRAINT pk_person PRIMARY KEY (person_id)
    -> );


15页第一行翻译有误，“输入源文件路径c:\temp\learningSQLExample.sql” 应该是“输入 source c:\temp\learningSQLExample.sql” 按照原文的方法，会返回错误。 从这也开始不敢往下看了，还是老老实实翻英文版吧，中文翻译太不靠谱了。害我在这问题上试了好一会儿。