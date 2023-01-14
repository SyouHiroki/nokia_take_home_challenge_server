from flask import Flask
from flask_socketio import SocketIO
from databases import connect
from utils import data

# Flask初始化
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

# 解决flaks_socketio 的跨域问题
sio = SocketIO(app, cors_allowed_origins='*')

# 事务
conn = connect.getConnect()
# 操作数据库的游标指针
cursor = conn.cursor()


def getData():  # 获取数据
    return data.selectByID(cursor)


def updateData(newData):  # 更新数据
    data.updateByID(cursor, newData)
    conn.commit()


@sio.on('connect')
def onConnect():  # 前台连接上要推送数据
    sio.emit('send-data-to-client', getData())


@sio.on('send-data-to-server')
def onSendDataToServer(payload):  # 前台发送过来的新的数据
    updateData(payload)
    sio.emit('send-data-to-client', getData())


if __name__ == '__main__':
    print('run')
    sio.run(app, host='localhost', port=5000)
