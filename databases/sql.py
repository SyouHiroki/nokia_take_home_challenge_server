# SELECT `data` FROM `data` WHERE id=1
def selectByIDSql(id):
    return 'SELECT `data` FROM `data` WHERE id=' + str(id)


# UPDATE `data` SET `data`=JSON_REPLACE(data, '$.data', '{"data": [{"col": 0, "row": 0, "answer": "", "children": [], "question": "", "editable": true}]}')WHERE id =1
def updateByIDSql(data, id):
    return 'UPDATE `data` SET `data`=JSON_REPLACE(data,' + "'$.data'," + "'" + data + "'" + ')WHERE id =' + str(id)
