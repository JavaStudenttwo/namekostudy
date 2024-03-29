# coding:utf-8

from MySqlConn import Mysql
from _sqlite3 import Row

# 申请资源
mysql = Mysql()

sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
result = mysql.getAll(sqlAll)
if result:
    print()
    'get all'
    for row in result:
        print()
        "%s\t%s" % (row["uid"], row["goodsname"])
sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
result = mysql.getMany(sqlAll, 2)
if result:
    print
    "get many"
    for row in result:
        print
        "%s\t%s" % (row["uid"], row["goodsname"])

result = mysql.getOne(sqlAll)
print
"get one"
print
"%s\t%s" % (result["uid"], result["goodsname"])

# 释放资源
mysql.dispose()