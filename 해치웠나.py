import turtle
import random

def draw_star(t, x, y, size, color="gold", filled=False):
    """
    t      : turtle.Turtle 객체
    x, y   : 별의 중심(대략) 좌표 (별은 x,y에서 약간 이동해서 그려집니다)
    size   : 별 한 변의 길이 (크기)
    color  : 선/채우기 색
    filled : True면 채운 별, False면 윤곽선 별
    """
    t.penup()
    # 별을 그릴 시작 위치 조정 (중심 기준 보정)
    t.goto(x, y - size/3)
    t.setheading(0)
    t.pendown()

    t.color(color)
    if filled:
        t.begin_fill()

    # 5각 별은 한 변을 그린 다음 144도 우회전 (혹은 36도 좌회전)
    for _ in range(5):
        t.forward(size)
        t.right(144)

    if filled:
        t.end_fill()

def random_stars(count=10, width=800, height=600):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor("midnight blue")
    screen.title("Turtle Stars")

    t = turtle.Turtle()
    t.speed(0)  # 최대 속도
    t.hideturtle()
    colors = ["white", "gold", "yellow", "light green", "cyan", "light pink"]

    for _ in range(count):
        x = random.randint(-width//2 + 50, width//2 - 50)
        y = random.randint(-height//2 + 50, height//2 - 50)
        size = random.randint(20, 120)
        color = random.choice(colors)
        filled = random.choice([True, False, False])  # 채운 별은 좀 적게
        draw_star(t, x, y, size, color, filled)

    # 큰 중앙 별 하나 추가
    draw_star(t, 0, 0, 200, color="gold", filled=True)

    # 클릭하면 종료
    screen.exitonclick()

if __name__ == "__main__":
    random_stars(count=12, width=900, height=700)