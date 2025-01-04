
 # mybatis #

 ### 什么是mybatis
 
 <a href="https://mybatis.org/mybatis-3/zh/index.html" target="_blank">中文官方文档</a> 
https://mybatis.p2hp.com/index.html
 
![](./img/mybatis/1-mybatis.png)
 
### 快速入门

 ![](./img/mybatis/2-quickStart-01.png)
 ![](./img/mybatis/2-quickStart-02.png) 
 ![](./img/mybatis/2-quickStart-03.png)
 ![](./img/mybatis/2-quickStart-04.png)
 ![](./img/mybatis/2-quickStart-05.png)

### idea配置sql提示

 ![](./img/mybatis/3-edeaTootipSql-01.png)
 ![](./img/mybatis/3-edeaTootipSql-02.png) 
 
### JDBC
   #### 简介 #### 
 __DBC是sun公司提供的一套操作关系型数据库的API(规范)__
 ![](./img/mybatis/4-jDBCprofile-01.png) 

#### 使用示例 ####
 ![](./img/mybatis/5-jdbcExample-01.png) 
 ![](./img/mybatis/5-jdbcExample-02.png) 
 ![](./img/mybatis/5-jdbcExample-03.png) 

#### jdbc和mybatis对比 ####
 ![](./img/mybatis/6-JDBCAndMybatisCompare.png) 

### 连接池 ###
#### 连接池(德鲁伊)使用 ####
__德鲁伊<a href="https://github.com/alibaba/druid/tree/master/druid-spring-boot-starter" target="_blank">官方地址</a>__

加载启动类在pom.xml
```
 <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.2.16</version>
        </dependency>
```

![](./img/mybatis/7-druidConPool-01.png) 
![](./img/mybatis/7-druidConPool-02.png) 

#### 其他链接池及介绍 #### 

![](./img/mybatis/7-otherConPool-01.png) 
![](./img/mybatis/7-otherConPool-02.png) 
![](./img/mybatis/7-otherConPool-03.png) 

### sql日志输出控制台 ### 

![](./img/mybatis/9-3logOutPrint.png) 

### 预编译sql ### 
![](./img/mybatis/9-precompileSql-01.png) 
![](./img/mybatis/9-precompileSql-02.png) 
![](./img/mybatis/9-precompileSql-03.png) 
![](./img/mybatis/9-precompileSql-04.png) 

### 使用mybatis准备工作 ### 
![](./img/mybatis/9-mybatisPrepare-01.png) 
![](./img/mybatis/9-mybatisPrepare-02.png) 


### 增加操作 ### 

#### 普通新增操作 ### 
![](./img/mybatis/9-add-01.png) 

#### 新增同时主键返回 ### 
![](./img/mybatis/9-add-02.png) 
![](./img/mybatis/9-add-03.png)  

### 删除操作 ### 

![](./img/mybatis/9-delete.png)  

### 更新操作 ### 

![](./img/mybatis/9-update-01.png)  
![](./img/mybatis/9-update-02.png)  

### 查询操作 ###  
![](./img/mybatis/9-query-01.png)  
#### 数据库返回和对象字段不匹配 ####  
![](./img/mybatis/9-query-02.png)  
#### 没匹配不上的原因 ####  
![](./img/mybatis/9-query-03.png)  
#### 驼峰和下划线转化解决 ####  
![](./img/mybatis/9-query-04.png)  

#### 解决示例代码 ####  
![](./img/mybatis/9-query-05.png)  
#### 带有条件查询 ####  
![](./img/mybatis/9-query-06.png)  

#### 占位问题 ####  
如果根据名字会进行模糊查询，但是模糊查询不支持参数如name字段
![](./img/mybatis/9-query-06.png) 

#### concat解决占位问题 ####  
![](./img/mybatis/9-query-07.png) 

#### springboot版本1和2的对比 ####  
![](./img/mybatis/9-query-08.png) 
 

#### xml写sql的准备条件 ####  
-  ***XML映射文件的名称与Mapper接口名称一致，并且将XML映射文件和Mapper接口放置在相同包下(同包同名)***
-  ***XML映射文件的namespace属性为Mapper接口全限定名一致。***
-  ***XML映射文件中sql语句的id与Mapper接口中的方法名一致，并保持返回类型一致。***
![](./img/mybatis/9-query-09.png) 

#### xml写动态sql #### 
写动态sql的主要原因是，过滤条件的个数不确定,导致sql拼接错误，比如where，set，或者and关键字，是必须有条件的时候才有用。
##### if判断 ##### 
 if去判断是否有过滤条件 

![](./img/mybatis/9-query-10.png) 
##### where标签 ##### 
 where标签自动判断是否需要加and如果有条件就加没条件就不加

![](./img/mybatis/9-query-11.png) 
##### set标签 ##### 
set用法和where一样都是mybatis自动判断过滤条件是否存在，来改变sql语句

![](./img/mybatis/9-query-12.png) 

##### forEach标签 ##### 
当同时执行一个数组的条件时，比如同时删除多个，会有多个id数组传递过来。这时采用forEach遍历到sql的in中

![](./img/mybatis/9-query-13.png) 
![](./img/mybatis/9-query-14.png) 

##### sql和include配对标签 ##### 
当多个sql语句产生一样的片段时，可以把相同的sql片段单独提取出来，通过include方式导入

![](./img/mybatis/9-query-15.png)  

#### 动态sql总结 #### 

![](./img/mybatis/9-query-16.png)  

#### mybatis插件 #### 

![](./img/mybatis/10-mybatisPlus-01.png)
![](./img/mybatis/10-mybatisPlus-01.png)    