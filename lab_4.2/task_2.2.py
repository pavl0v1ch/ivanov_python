import numpy as np
from datetime import datetime, timedelta

# Входные данные
lengths_str = "12 15 13 16 17 14"
speeds_str = "60 55 70 60 75 65"
entry_segment = 2
exit_segment = 5
entry_time_str = "13:30"

# Преобразование строк в массивы
lengths = np.array(list(map(float, lengths_str.split())))
speeds = np.array(list(map(float, speeds_str.split())))

# Индексы участков (нумерация с 1 → индексы с 0)
start = entry_segment - 1
end = exit_segment

# Выбор нужных участков
selected_lengths = lengths[start:end]
selected_speeds = speeds[start:end]

# Расчёт времени на каждом участке (в часах)
segment_times = selected_lengths / selected_speeds

# Общие значения
total_distance = np.sum(selected_lengths)
total_time_hours = np.sum(segment_times)
total_time_minutes = int(round(total_time_hours * 60))
average_speed = total_distance / total_time_hours

# Время въезда и выезда
entry_time = datetime.strptime(entry_time_str, "%H:%M")
exit_time = entry_time + timedelta(minutes=total_time_minutes)

# Вывод
print(f"{int(total_distance)} км")
print(f"{total_time_minutes} мин")
print(f"{round(average_speed, 1)} км/ч")
