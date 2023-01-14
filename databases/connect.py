import pymysql


def getConnect():
    # 数据库连接
    pymysql.install_as_MySQLdb()
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='nokia_take_home_challenge',
        charset='utf8'
    )

    # 返回指针
    return con
