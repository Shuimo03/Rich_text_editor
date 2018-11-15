from sqlalchemy import create_engine
#连接数据库，这里是本地测试连接的数据库
the_engine =  create_engine("mysql+pymysql://root:WULIANG1998102@127.0.0.1:3306/richtext?charset=utf8mb4")
