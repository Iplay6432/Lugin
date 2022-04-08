@@ -14,29 +14,71 @@ Y = 300
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

displays = pygame.display.set_mode((X, Y))
pygame.display.set_caption('The Path to login')
fwint = f'{os.getcwd()}\\logins\\font.ttf'
font1 = pygame.font.Font(fwint, 24)
font1 = pygame.font.Font(None, 24)
global text
text = ''
def mainscree():
    global center
    global text
    global texts
    global text1
    global center1
    text = font1.render('What Would You Like', True, green)
    texts = font1.render('What Would You Like', True, green)
    text1 = font1.render('to do today?',True, green)
    center = text.get_rect()
    center1 = text.get_rect()
    center = texts.get_rect()
    center1 = texts.get_rect()
    center.center = (X // 2, Y // 4)
    center1.center = (X // 2, Y // 3.1)
    displays.fill(white)
    displays.blit(text, center)
    displays.blit(texts, center)
    displays.blit(text1, center1)
def maketextbox(x,y,w,h):
    input_box = pygame.Rect(x, y, w, h)
    text = ''
    clock = pygame.time.Clock()
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    if ev.type == pygame.MOUSEBUTTONDOWN:
        if input_box.collidepoint(ev.pos):
            # Toggle the active variable.
            active = not active
        else:
            active = False
        # Change the current color of the input box.
        color = color_active if active else color_inactive
    if ev.type == pygame.KEYDOWN:
        if active:
            if ev.key == pygame.K_RETURN:
                print(text)
                text = ''
            elif ev.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += ev.unicode

    displays.fill((30, 30, 30))
    # Render the current text.
    txt_surface = font1.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width() + 10)
        # Blit the text.
    displays.blit(txt_surface, (x + 5, y + 5))
        # Blit the input_box rect.
    pygame.draw.rect(displays, color, input_box, 2)
    pygame.display.flip()
    clock.tick(30)
def login():
    print("hi")
    global text2
    text2 = font1.render('Enter Username And Passowrd', True, green)
    global text
    text = ''

def signup():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
@ -89,7 +131,8 @@ while True:
    mouse = pygame.mouse.get_pos()
    mouse1 = pygame.mouse.get_pos()
    mainscree()

    if asd == 1:
        maketextbox(100, 100, 140, 32)
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
@ -99,6 +142,5 @@ while True:

            button1()
            button2()
            pygame.display.update()

