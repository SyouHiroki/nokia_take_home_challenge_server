# SELECT `data` FROM `data` WHERE id=1
def selectByIDSql(id):
    return 'SELECT `data` FROM `data` WHERE id=' + str(id)


# UPDATE `data` SET `data` = '{"data": [{"col": 0, "row": 0, "answer": "", "children": [], "question": "", "editable": true}]}'
def updateByIDSql(data):
    return 'UPDATE `data` SET `data`=' + "'" + data + "'"
