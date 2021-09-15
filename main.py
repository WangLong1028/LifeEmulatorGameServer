from socket import *
from pymysql import *
from constant import *
from threading import Thread

# 在线的客户端
online_clients = list()


def handle_client_request(client: socket):
    pass


def main():
    # 加载数据库
    database = connect(host='127.0.0.1', port=3306, user='root', database='LifeEmulator')

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', SERVER_PORT))
    server_socket.listen(128)

    g_conn_pool = []  # 连接池

    while True:
        client, addr = server_socket.accept()
        # 加入连接池
        g_conn_pool.append(client)
        # 创建线程


if __name__ == '__main__':
    main()
