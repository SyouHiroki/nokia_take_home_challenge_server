from databases import sql


def selectByID(cursor, id=1):
    cursor.execute(sql.selectByIDSql(id))
    return cursor.fetchall()


def updateByID(cursor, data):
    cursor.execute(sql.updateByIDSql(data))
