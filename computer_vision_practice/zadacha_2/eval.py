import cv2
import numpy as np

class Node:
    def __init__(self, name=None):
        self.name = name
        self.connections = []

    def add_connection(self, node: 'Node',con_len:int):
        self.connections.append((node, con_len))
        
    def __str__(self):
        return str(self.name)

class Way:
    def __init__(self, start_node: Node):
        self.start_node = start_node

        self.nodes = [start_node]
        self.len = 0

    @property
    def last_node(self):
        return self.nodes[-1]

    def add_node(self, node: Node, length: int):
        self.nodes.append(node)
        self.len += length

    def copy(self) -> 'Way':
        new_way = Way(self.start_node)
        new_way.nodes = self.nodes.copy()
        new_way.len = self.len
        return new_way
    def __str__(self):
        return ' -> '.join(map(str, self.nodes))

 # CROSS #1
cross1_r_in = Node(1)
cross1_b_in = Node(1)
cross1_l_in = Node(1)

cross1_r_out = Node('cross1_r_out')
cross1_b_out = Node('cross1_b_out')
cross1_l_out = Node('cross1_l_out')

cross1_r_in.add_connection(cross1_b_out, 14)
cross1_r_in.add_connection(cross1_l_out, 13)

cross1_l_in.add_connection(cross1_b_out, 9)
cross1_l_in.add_connection(cross1_r_out, 13)

cross1_b_in.add_connection(cross1_r_out, 9)
cross1_b_in.add_connection(cross1_l_out, 14)

# CROSS #2
cross2_r_in = Node(2)
cross2_b_in = Node(2)
cross2_t_in = Node(2)

cross2_r_out = Node('cross2_r_out')
cross2_b_out = Node('cross2_b_out')
cross2_t_out = Node('cross2_t_out')

cross2_r_in.add_connection(cross2_b_out, 14)
cross2_r_in.add_connection(cross2_t_out, 9)

cross2_b_in.add_connection(cross2_t_out, 13)
cross2_b_in.add_connection(cross2_r_out, 9)

cross2_t_in.add_connection(cross2_b_out, 13)
cross2_t_in.add_connection(cross2_r_out, 14)

# CROSS #3
cross3_l_in = Node(3)
cross3_r_in = Node(3)
cross3_b_in = Node(3)
cross3_t_in = Node(3)

cross3_l_out= Node('cross3_l_out')
cross3_r_out = Node('cross3_r_out')
cross3_b_out= Node('cross3_b_out')
cross3_t_out= Node('cross3_t_out')

cross3_l_in.add_connection(cross3_r_out, 13)
cross3_l_in.add_connection(cross3_t_out,14)
cross3_l_in.add_connection(cross3_b_out,9)

cross3_r_in.add_connection(cross3_l_out, 13)
cross3_r_in.add_connection(cross3_t_out,9)
cross3_r_in.add_connection(cross3_b_out,14 )

cross3_b_in.add_connection(cross3_r_out,9)
cross3_b_in.add_connection(cross3_t_out,13)
cross3_b_in.add_connection(cross3_l_out, 14)

cross3_t_in.add_connection(cross3_r_out, 14)
cross3_t_in.add_connection(cross3_l_out, 9)
cross3_t_in.add_connection(cross3_b_out,13)


 # CROSS #4
cross4_l_in= Node(4)
cross4_b_in= Node(4)
cross4_t_in= Node(4)

cross4_l_out= Node('cross4_l_out')
cross4_b_out= Node('cross4_b_out')
cross4_t_out= Node('cross4_t_out')

cross4_l_in.add_connection(cross4_b_out,9)
cross4_l_in.add_connection(cross4_t_out, 14)

cross4_b_in.add_connection(cross4_t_out, 13)
cross4_b_in.add_connection(cross4_l_out, 14)

cross4_t_in.add_connection(cross4_b_out, 13)
cross4_t_in.add_connection(cross4_l_out,9)

 # CROSS #5
cross5_l_in= Node(5)
cross5_r_in= Node(5)
cross5_t_in= Node(5)

cross5_l_out= Node('cross5_l_out')
cross5_r_out= Node('cross5_r_out')
cross5_t_out= Node('cross5_t_out')

cross5_l_in.add_connection(cross5_r_out, 13)
cross5_l_in.add_connection(cross5_t_out, 14)

cross5_r_in.add_connection(cross5_l_out, 13)
cross5_r_in.add_connection(cross5_t_out,9)

cross5_t_in.add_connection(cross5_r_out, 14)
cross5_t_in.add_connection(cross5_l_out,9)

 # CONNECTIONS BETWEEN CROSSES

cross1_l_out.add_connection(cross2_t_in, 33)
cross1_r_out.add_connection(cross4_t_in, 28)
cross1_b_out.add_connection(cross3_t_in, 10)

cross2_t_out.add_connection(cross1_l_in, 28)
cross2_r_out.add_connection(cross3_l_in, 12)
cross2_b_out.add_connection(cross5_l_in, 33)

cross3_l_out.add_connection(cross2_r_in, 12)
cross3_r_out.add_connection(cross4_l_in, 12)
cross3_b_out.add_connection(cross5_t_in, 10)
cross3_t_out.add_connection(cross1_b_in, 10)

cross4_l_out.add_connection(cross3_r_in, 12)
cross4_t_out.add_connection(cross1_r_in, 33)
cross4_b_out.add_connection(cross5_r_in, 28)

cross5_l_out.add_connection(cross2_b_in, 28)
cross5_r_out.add_connection(cross4_b_in, 33)
cross5_t_out.add_connection(cross3_b_in, 10)

road_radius = 27

vertical_roads = {
 'top_left': [44, 106, 215],
 'top_middle': [307, 106, 215],
 'top_right': [570, 106, 215],
 'bottom_left': [44, 350, 459],
 'bottom_middle': [307, 350, 459],
 'bottom_right': [570, 350, 459]
 }

horizontal_roads = {
 'left_top': [39, 111, 240],
 'left_middle': [283, 111, 240],
 'left_bottom': [526, 111, 240],
 'right_top': [39, 375, 503],
 'right_middle': [283, 375, 503],
 'right_bottom': [526, 375, 503]
 }


def get_start_point_coordinates(img):
    blue = cv2.inRange(img, (50, 0, 0), (255, 0, 0))

    x = np.nonzero(np.argmax(blue, axis=0))[0]
    y = np.nonzero(np.argmax(blue, axis=1))[0]
    start_x = int(sum(x) / len(x))
    start_y = int(sum(y) / len(y))

    return start_x, start_y


def get_end_point_coordinates(img):
    red = cv2.inRange(img, (0, 0, 50), (0, 0, 255))

    x = np.nonzero(np.argmax(red, axis=0))[0]
    y = np.nonzero(np.argmax(red, axis=1))[0]
    end_x = int(sum(x) / len(x))
    end_y = int(sum(y) / len(y))


    return end_x, end_y


def check_on_the_same_road(start_road_name, end_road_name, start_direction, end_direction, start_x, start_y, end_x, end_y, start_road_type, end_road_type):
   
 # check if on the same road pointing the same direction
    if start_road_name == end_road_name and start_direction == end_direction:
        if start_road_type == 'vertical':
            if start_direction == 'up':
                if start_y > end_y: # start point should be downer
                    print('No need to move to cross')
                    return True
            else:
                if start_y < end_y: # start point should be upper
                    print('No need to move to cross')
                    return True
        else:
            if start_direction == 'right':
                if start_x < end_x:
                    print('No need to move to cross')
                    return True
            else:
                if start_x > end_x:
                    print('No need to move to cross')
                    return True

 # check if points on the turn
    conditions = []
    # TOP LEFT TURN
    conditions.append(all([start_road_name == 'left_top',
    start_direction == 'left',
    end_road_name == 'top_left',
    end_direction == 'down']))
    conditions.append(all([start_road_name == 'top_left',
    start_direction == 'up',
    end_road_name == 'left_top',
    end_direction == 'right']))

    # TOP RIGHT TURN
    conditions.append(all([start_road_name == 'right_top',
    start_direction == 'right',
    end_road_name == 'top_right',
    end_direction == 'down']))
    conditions.append(all([start_road_name == 'top_right',
    start_direction == 'up',
    end_road_name == 'right_top',
    end_direction == 'left']))

    # BOTTOM LEFT TURN
    conditions.append(all([start_road_name == 'left_bottom',
    start_direction == 'left',
    end_road_name == 'bottom_left',
    end_direction == 'up']))
    conditions.append(all([start_road_name == 'bottom_left',
    start_direction == 'down',
    end_road_name == 'left_bottom',
    end_direction == 'right']))


    # BOTTOM RIGHT TURN
    conditions.append(all([start_road_name == 'right_bottom',
    start_direction == 'right',
    end_road_name == 'bottom_right',
    end_direction == 'up']))
    conditions.append(all([start_road_name == 'bottom_right',
    start_direction == 'down',
    end_road_name == 'right_bottom',
    end_direction == 'left']))

    if any(conditions):
        print('No need for CROSS!')
        return True

    return False


def find_the_shortest_way(image) -> list:
    """
    Функция для нахождения кратчайшего маршрута из точки A (синяя точка) в точку B
    ,→ (красная точка).

    Входные данные: изображение (bgr), прочитано cv2.imread
    Выходные данные: список из пройденных перекрестков:
    [1, 2, 3, 4, 5], где 1, 2, 3, 4, 5 - перекрёстки, которые необходимо
    ,→ преодолеть
    Всего есть 5 перекрёстков, которые можно проехать.

    Примеры вывода:
    [4, 5, 3] - проехать через перекрестки 4, 5, 3

    [4] - преодолеть перекресток 4

    [] - перекрёстки пересекать не требуется
    """
        # Алгоритм проверки будет вызывать функцию find_the_shortest_way,
        # остальные функции должны вызываться из неё.

    start_x, start_y = get_start_point_coordinates(image)
    end_x, end_y = get_end_point_coordinates(image)

    cv2.circle(image, (start_x, start_y), 20, (0, 255, 0), 1)
    cv2.circle(image, (end_x, end_y), 20, (0, 255, 0), 1)

    print(start_x, start_y)
    print(end_x, end_y)

    for road_name, (road_x, road_start, road_end) in vertical_roads.items():
        cv2.rectangle(image, (road_x-road_radius, road_start), (road_x+road_radius, road_end), (255, 0, 0), 2)

        if road_x - road_radius <= start_x <= road_x + road_radius and road_start <= start_y <= road_end:
            start_road_type = 'vertical'
            start_road_name = road_name
            if start_x > road_x:
                start_direction = 'up'
            else:
                start_direction = 'down'


        if road_x - road_radius <= end_x <= road_x + road_radius and road_start <= end_y <= road_end:
            end_road_type = 'vertical'
            end_road_name = road_name
            if end_x > road_x:
                end_direction = 'up'
            else:
                end_direction = 'down'

    # cv2.imshow('img', img)
    # cv2.waitKey(0)

    for road_name, (road_y, road_start, road_end) in horizontal_roads.items():
    # cv2.rectangle(img, (road_start, road_y-road_radius), (road_end, road_y+road_radius), (255, 0, 0), 2)

        if road_y - road_radius <= start_y <= road_y + road_radius and road_start <= start_x <= road_end:
            start_road_type = 'horizontal'
            start_road_name = road_name
            if start_y > road_y:
                start_direction = 'right'
            else:
                start_direction = 'left'

        if road_y - road_radius <= end_y <= road_y + road_radius and road_start <= end_x <= road_end:
            end_road_type = 'horizontal'
            end_road_name = road_name
            if end_y > road_y:
                end_direction = 'right'
            else:
                end_direction = 'left'

    print(f"[START] Start point {start_x, start_y} is on {start_road_type} {start_road_name} road pointing {start_direction}")
    print(f"[END] End point {end_x, end_y} is on{end_road_type} {end_road_name} road pointing {end_direction}")

    if check_on_the_same_road(start_road_name, end_road_name, start_direction, end_direction, start_x, start_y, end_x,
    end_y, start_road_type, end_road_type):
        return []

    # CREATE START NODE
    start_node = Node("START")
    # vertical roads
    if start_road_name == 'top_left':
        if start_direction == 'up':
            start_node.add_connection(cross1_l_in, 23)
        else:
            start_node.add_connection(cross2_t_in, 5)

    elif start_road_name == 'top_middle':
        if start_direction == 'up':
            start_node.add_connection(cross1_b_in, 5)
        else:
            start_node.add_connection(cross3_t_in, 5)


    elif start_road_name == 'top_right':
        if start_direction == 'up':
            start_node.add_connection(cross1_r_in, 28)
        else:
            start_node.add_connection(cross4_t_in, 5)

    elif start_road_name == 'bottom_left':
        if start_direction == 'up':
            start_node.add_connection(cross2_b_in, 5)
        else:
            start_node.add_connection(cross5_l_in, 28)

    elif start_road_name == 'bottom_middle':
        if start_direction == 'up':
            start_node.add_connection(cross3_b_in, 5)
        else:
            start_node.add_connection(cross5_t_in, 5)

    elif start_road_name == 'bottom_right':
        if start_direction == 'up':
            start_node.add_connection(cross4_b_in, 5)
        else:
            start_node.add_connection(cross5_r_in, 23)

    # horizontal roads
    elif start_road_name == 'left_top':
        if start_direction == 'right':
            start_node.add_connection(cross1_l_in, 5)
        else:
            start_node.add_connection(cross2_t_in, 28)

    elif start_road_name == 'left_middle':
        if start_direction == 'right':
            start_node.add_connection(cross3_l_in, 5)
        else:
            start_node.add_connection(cross2_r_in, 5)

    elif start_road_name == 'left_bottom':
        if start_direction == 'right':
            start_node.add_connection(cross5_l_in, 5)
        else:
            start_node.add_connection(cross2_b_in, 23)

    elif start_road_name == 'right_top':
        if start_direction == 'right':
            start_node.add_connection(cross4_t_in, 23)
        else:
            start_node.add_connection(cross1_r_in, 5)

    elif start_road_name == 'right_middle':
        if start_direction == 'right':
            start_node.add_connection(cross4_l_in, 5)
        else:
            start_node.add_connection(cross3_r_in, 5)

    elif start_road_name == 'right_bottom':
        if start_direction == 'right':
            start_node.add_connection(cross4_b_in, 28)
        else:
            start_node.add_connection(cross5_r_in, 5)


    # CREATE END NODE
    end_node = Node("END")
    # VERTICAL
    if end_road_name == 'top_left':
        if end_direction == 'up':
            cross2_t_out.add_connection(end_node, 5)
        else:
            cross1_l_out.add_connection(end_node, 28)

    elif end_road_name == 'top_middle':
        if end_direction == 'up':
            cross3_t_out.add_connection(end_node, 5)
        else:
            cross1_b_out.add_connection(end_node, 5)

    elif end_road_name == 'top_right':
        if end_direction == 'up':
            cross4_t_out.add_connection(end_node, 5)
        else:
            cross1_r_out.add_connection(end_node, 23)

    elif end_road_name == 'bottom_left':
        if end_direction == 'down':
            cross2_b_out.add_connection(end_node, 5)
        else:
            cross5_l_out.add_connection(end_node, 23)

    elif end_road_name == 'bottom_middle':
        if end_direction == 'down':
            cross3_b_out.add_connection(end_node, 5)
        else:
                cross5_t_out.add_connection(end_node, 5)

    elif end_road_name == 'bottom_right':
        if end_direction == 'down':
            cross4_b_out.add_connection(end_node, 5)
        else:
            cross5_r_out.add_connection(end_node, 28)

    # HORIZONTAL
    elif end_road_name == 'left_top':
        if end_direction == 'right':
            cross2_t_out.add_connection(end_node, 23)
        else:
            cross1_l_out.add_connection(end_node, 5)

    elif end_road_name == 'left_middle':
        if end_direction == 'right':
            cross2_r_out.add_connection(end_node, 5)
        else:
            cross3_l_out.add_connection(end_node, 5)

    elif end_road_name == 'left_bottom':
        if end_direction == 'right':
            cross2_b_out.add_connection(end_node, 28)
        else:
            cross5_l_out.add_connection(end_node, 5)

    elif end_road_name == 'right_top':

        if end_direction == 'right':
            cross1_r_out.add_connection(end_node, 5)
        else:
            cross4_t_out.add_connection(end_node, 28)

    elif end_road_name == 'right_middle':
        if end_direction == 'right':
            cross3_r_out.add_connection(end_node, 5)
        else:
            cross4_l_out.add_connection(end_node, 5)
    
    elif end_road_name == 'right_bottom':
        if end_direction == 'right':
            cross5_r_out.add_connection(end_node, 5)
        else:
            cross4_b_out.add_connection(end_node, 23)
        
    ways = [Way(start_node)]
    best_way = None
    best_way_len = 0

    run = True

    while run:
        new_ways = []
        shorter_ways = False
        shorter_ways_lst = []
        for way in ways:
            for next_node, length in way.last_node.connections:
                if next_node == end_node:
                    if best_way:
                        way.add_node(next_node, length)
                        if way.len == best_way.len:
                            print('EQUAL WAYS!!!!')
                            print("[best_way]", best_way.len, best_way)
                            print("[cur_way]", way.len, way)
                            open('equal_ways.txt', 'w').close()

                        if way.len < best_way.len:
                            best_way = way
                            best_way_len = way.len
                            print("[New BEST!]", way.len, way)
                    else:
                        way.add_node(next_node, length)
                        best_way = way
                        best_way_len = way.len
                        shorter_ways = True
                    print("[Reach the End!]", way.len, way)
                else:
                    way_copy = way.copy()
                    way_copy.add_node(next_node, length)
                    new_ways.append(way_copy)
                    if best_way:
                        if way_copy.len < best_way_len:
                            shorter_ways = True
                            shorter_ways_lst.append(way)

        if best_way:
            print("[BEST NODE]", best_way.len, best_way)
            print('shorter ways =', shorter_ways)
            for way in shorter_ways_lst:
                print(way.len, way)

                print("-" * 60)

        if best_way and not shorter_ways:
            break
        ways = new_ways.copy()

    print(best_way, best_way.len)
    ans = []
    for node in best_way.nodes:
        if node.name in (1, 2, 3, 4, 5):
            ans.append(node.name)

    return ans
