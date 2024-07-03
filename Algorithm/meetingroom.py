import sys

n, m = map(int, input().split())

room_list = [input() for _ in range(n)]
room_list.sort()

time_list = [[0]*9 for _ in range(n)]

for _ in range(m):
    room_name, s_time, e_time = input().split()
    s_time = int(s_time) - 9
    e_time = int(e_time) - 9

    if s_time != e_time:
        for i in range(n):

            # room_list의 이름과 room_name이 같으면
            if room_list[i] == room_name:
                # 예약 표시
                for time in range(s_time, e_time):
                    if time_list[i][time] == 0:
                        # 예약이 되면 1로 카운트
                        time_list[i][time] = 1

# 예약가능한 시간 카운트
cnt_time = []

for time in range(n):
    # 예약가능한 시간 저장 리스트
    reservation = []

    times = time_list[time]
    cnt = 0

    # 9시는 카운트가 안됌
    if times[0] == 0:
        reservation.append('09')
    # 9시랑 18시 제외 탐색
    for t in range(1, 9):
        if times[t-1] == 0 and times[t] == 1:
            reservation.append(t+9)
            cnt += 1
        elif times[t-1] == 1 and times[t] == 0:
            reservation.append(t+9)
    #  18시는 카운트가 안됌
    if times[-1]:
        reservation.append('18')
        cnt += 1

    cnt_time.append(cnt)

    # 출력
    if n != 0:
        print(f'-----')

    print(f'Room {room_list[n]}:')

    if cnt_time[n] == 0:
        print(f'Not available')
    else:
        print(f'{cnt_time[n]} available:')

    for yes in range(len(reservation)):
        print(f'{reservation[yes*2]-reservation[yes*2+1]}')

