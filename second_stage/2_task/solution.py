# -*- coding: utf-8 -*-
import socket
import math
# TODO: Допишите импорт библиотек, которые собираетесь использовать

def next_task(start_pos: tuple, msg: str) -> int:

    start_pos_x, start_pos_y = map(int, start_pos)
   
    msg_list = msg.split(",")
    dist_list = []

    for task_x_y in msg_list:
        x, y =  map(int, (task_x_y.split("."))[1:])
        
        dist = math.sqrt((x - start_pos_x)**2 + (y - start_pos_y)**2)
        dist_list.append(dist)
    id_min_dist = dist_list.index(min(dist_list))
    main_task = (msg_list[id_min_dist]).split(".")[0]
    print(id_min_dist, main_task)
    return id_min_dist, main_task
    


def setup_socket(ip_address, port):
    """ Функция инициализирует сокет.
        Входные параметры: ip-адрес и порт сервера
        Выходные параметры: инициализированный сокет

        Если вы не собираетесь использовать эту функцию, пусть возвращает None

        То, что вы вернёте из этой функции, будет передано первым аргументом в функцию communication_cycle
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip_address, port))
    return server
    # return None


def communication_cycle(conn: socket.socket, start_pos, start_equipment):
    """ Эта функция отвечает за обмен данными с информационным и сервисным центрами..
        Входные параметры: 
            conn - сокет из функции setup_socket, 
            start_pos - стартовая позиция беспилотного автомобиля (x, y),
            start_equipment - начальное снаряжение

    """
    conn.send('server,give_tasks|'.encode()) #говоришь что готов получить задание
    msg = ''
    while True:
        symbol = conn.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol    #клиент получает доступные задания в таком виде crash.189.48,medic_aid.104.158,fire.1.199;
                        #  надо определить айди ближайшего задания

    id_min_dist, main_task = next_task(start_pos, msg)
    
    conn.send(f"server,reserve_task,{id_min_dist}|".encode())#после того как нашли ближайшее задание везервируем его
    
    while True:
        symbol = conn.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol
    conn.send('hub,offload|'.encode())
    
    while True:
        symbol = conn.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol

    equipments = ["fire", "medic_aid", "crash"]
    n = equipments.index(main_task)+1
    
    conn.send(f"hub,give,{n}|".encode()) 

    while True:
        symbol = conn.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol
    conn.send('equip_ready|'.encode())

    while True:
        symbol = conn.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol
    conn.close()
