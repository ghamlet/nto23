film = 17; audio = 1
w = 1280;  h = 720
v = 25 ;   time = 20

v_video = (film - audio) * 1024 *1024 *1024 *8 
print(f"Обьем фильма {v_video} бит")

time = 20 * 60
frames = v * time
print(f"Количество кадров {frames}")

img = v_video / frames
print(f"Обьем кадра {img} бит")

i = int(img / (w * h))
print(f"Количество бит на один пиксель {i}") # 4.971026962962963

N = 2 ** i
print(f"Количество цветов {N}") #16