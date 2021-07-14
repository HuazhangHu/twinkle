mysql不区分大小写  
进入数据库：sudo mysql -u root -p;  
查看所有数据库：show databases;  
选择某个数据库：use table_name;  
显示所有表：show tables;  
显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等 SHOW COLUMNS FROM 数据表;  
显示数据表的详细索引信息（主键）SHOW INDEX FROM 数据表;  
输出Mysql数据库管理系统的性能及统计信息：SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern'] \G:  
   \# 加上 \G，查询结果按列打印  
创建数据库：CREATE DATABASE 数据库名;  
删除数据库:drop database <数据库名>;  
创建数据表：CREATE TABLE table_name (column_name column_type);  
删除数据表：DROP TABLE table_name;  
插入数据：INSERT INTO table_name ( field1, field2,...fieldN ) VALUES ( value1, value2,...valueN );  
UPDATE table_name SET field1=new-value1, field2=new-value2[WHERE Clause]  
删除某一列：DELETE FROM <表名> [WHERE 子句] [ORDER BY 子句] [LIMIT 子句]  

