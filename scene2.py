import pygame
from dino import Dino

FPS = 60
WIDTH = 1200
HEIGHT = 800


def cut_scen_2(screen, color, score, HI, road_cord_x1, birthday_code, language, keys, water_number, fire_number, money, road_speed, road_v, moon_list, sun_list):
    clock = pygame.time.Clock()

    num_0 = pygame.image.load('imgs/0.png')
    num_0.set_colorkey('white')
    num_1 = pygame.image.load('imgs/1.png')
    num_1.set_colorkey('white')
    num_2 = pygame.image.load('imgs/2.png')
    num_2.set_colorkey('white')
    num_3 = pygame.image.load('imgs/3.png')
    num_3.set_colorkey('white')
    num_4 = pygame.image.load('imgs/4.png')
    num_4.set_colorkey('white')
    num_5 = pygame.image.load('imgs/5.png')
    num_5.set_colorkey('white')
    num_6 = pygame.image.load('imgs/6.png')
    num_6.set_colorkey('white')
    num_7 = pygame.image.load('imgs/7.png')
    num_7.set_colorkey('white')
    num_8 = pygame.image.load('imgs/8.png')
    num_8.set_colorkey('white')
    num_9 = pygame.image.load('imgs/9.png')
    num_9.set_colorkey('white')
    nums_dict = {
        '0': num_0,
        '1': num_1,
        '2': num_2,
        '3': num_3,
        '4': num_4,
        '5': num_5,
        '6': num_6,
        '7': num_7,
        '8': num_8,
        '9': num_9
    }
    HI_img = pygame.image.load('imgs/HI.png')
    HI_img.set_colorkey('white')
    mag_left = pygame.image.load('imgs/fire_magician.png')
    mag_left = pygame.transform.scale(mag_left, (48, 100))
    mag_left = pygame.transform.flip(mag_left, True, False)
    mag_left.set_colorkey('white')
    mag_right = pygame.image.load('imgs/fire_magician.png')
    mag_right = pygame.transform.scale(mag_right, (48, 100))
    mag_right.set_colorkey('white')
    road1 = pygame.image.load('imgs/road.png')
    road1.set_colorkey('white')
    dialog_left = pygame.image.load('imgs/dialog_left.png')
    dialog_right = pygame.image.load('imgs/dialog_right.png')
    cloud = pygame.image.load('imgs/cloud.png')
    cloud.set_colorkey('white')
    night_sun = pygame.image.load('imgs/night_sun.png')
    night_sun.set_colorkey('black')
    moon = pygame.image.load('imgs/moon.png')
    moon.set_colorkey('black')
    star = pygame.image.load('imgs/star.png')
    star.set_colorkey('black')
    dialog_left.set_colorkey('white')
    dialog_right.set_colorkey('white')
    if birthday_code:
        dino1 = pygame.image.load('imgs/dino_bd_1.png')
        d_y = 310 - 32
        d_x = 100
    else:
        d_y = 310
        d_x = 100
        dino1 = pygame.image.load('imgs/dino1.png')
    dino1.set_colorkey('white')
    d = Dino(d_x, d_y)
    running = True
    mag_cord_x = WIDTH
    mag_cord_y = 384
    t = 1
    t_c = 1
    score_str = str(score)
    score_cord_y = 50
    HI_str = str(HI)
    HI_t = 0
    HI_coard_y = 700
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                quit()  # running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка событий мыши
                if event.button == 1:
                    if t > 200 and t < 1600:
                        t_c = t // 100
                        if t_c % 2 == 1:
                            t_c += 1
                            t = t_c * 100
                        elif t_c % 2 == 0:
                            t_c += 2
                            t = t_c * 100
            if event.type == pygame.KEYDOWN:  # обработка событий клавиатуры
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == 32:
                    if t > 200 and t < 1600:
                        t_c = t // 100
                        if t_c % 2 == 1:
                            t_c += 1
                            t = t_c * 100
                        elif t_c % 2 == 0:
                            t_c += 2
                            t = t_c * 100
        screen.fill(color)
        screen.blit(dino1, (d_x, d_y + 95))
        screen.blit(road1, (0, 470))
        moon_x = moon_list[0]
        star_x1 = moon_list[1]
        star_x2 = moon_list[2]
        star_x3 = moon_list[3]
        star_x4 = moon_list[4]
        star_x5 = moon_list[5]
        star_x6 = moon_list[6]
        star_x7 = moon_list[7]
        star_x8 = moon_list[8]
        star_x9 = moon_list[9]
        star_x10 = moon_list[10]
        cloud_x1 = sun_list[0]
        cloud_x2 = sun_list[1]
        cloud_x3 = sun_list[2]
        cloud_x4 = sun_list[3]
        cloud_x5 = sun_list[4]
        cloud_x6 = sun_list[5]
        cloud_x7 = sun_list[6]
        cloud_x8 = sun_list[7]
        cloud_x9 = sun_list[8]
        cloud_x10 = sun_list[9]
        sun_x = sun_list[10]
        if color == (0, 0, 0):
            screen.blit(moon, (moon_x, 80))
            screen.blit(star, (star_x1, 125))
            screen.blit(star, (star_x2, 150))
            screen.blit(star, (star_x3, 140))
            screen.blit(star, (star_x4, 110))
            screen.blit(star, (star_x5, 140))
            screen.blit(star, (star_x6, 137))
            screen.blit(star, (star_x7, 135))
            screen.blit(star, (star_x8, 133))
            screen.blit(star, (star_x9, 122))
            screen.blit(star, (star_x10, 147))
        else:
            screen.blit(cloud, (cloud_x1, 123))
            screen.blit(cloud, (cloud_x2, 200))
            screen.blit(cloud, (cloud_x3, 216))
            screen.blit(cloud, (cloud_x4, 147))
            screen.blit(cloud, (cloud_x5, 111))
            screen.blit(cloud, (cloud_x6, 50))
            screen.blit(cloud, (cloud_x7, 91))
            screen.blit(cloud, (cloud_x8, 131))
            screen.blit(cloud, (cloud_x9, 115))
            screen.blit(cloud, (cloud_x10, 100))
            screen.blit(night_sun, (sun_x, 100))

        moon_x -= 1
        star_x1 -= 1
        star_x2 -= 1
        star_x3 -= 1
        star_x4 -= 1
        star_x5 -= 1
        star_x6 -= 1
        star_x7 -= 1
        star_x8 -= 1
        star_x9 -= 1
        star_x10 -= 1
        cloud_x1 -= 1
        cloud_x2 -= 1
        cloud_x3 -= 1
        cloud_x4 -= 1
        cloud_x5 -= 1
        cloud_x6 -= 1
        cloud_x7 -= 1
        cloud_x8 -= 1
        cloud_x9 -= 1
        cloud_x10 -= 1
        sun_x -= 1
        if star_x1 <= -40:
            star_x1 = 1200
        if star_x2 <= -40:
            star_x2 = 1200
        if star_x3 <= -40:
            star_x3 = 1200
        if star_x4 <= -40:
            star_x4 = 1200
        if star_x5 <= -40:
            star_x5 = 1200
        if star_x6 <= -40:
            star_x6 = 1200
        if star_x7 <= -40:
            star_x7 = 1200
        if star_x8 <= -40:
            star_x8 = 1200
        if star_x9 <= -40:
            star_x9 = 1200
        if star_x10 <= -40:
            star_x10 = 1200
        if sun_x <= - 100:
            sun_x = 1200
        if cloud_x1 <= - 115:
            cloud_x1 = 1200
        if cloud_x2 <= - 115:
            cloud_x2 = 1200
        if cloud_x3 <= - 115:
            cloud_x3 = 1200
        if cloud_x4 <= - 115:
            cloud_x4 = 1200
        if cloud_x5 <= - 115:
            cloud_x5 = 1200
        if cloud_x6 <= - 115:
            cloud_x6 = 1200
        if cloud_x7 <= - 115:
            cloud_x7 = 1200
        if cloud_x8 <= - 115:
            cloud_x8 = 1200
        if cloud_x9 <= - 115:
            cloud_x9 = 1200
        if cloud_x10 <= - 115:
            cloud_x10 = 1200
        if moon_x <= -40:
            moon_x = 1200

        moon_list = [moon_x, star_x1, star_x2, star_x3, star_x4, star_x5, star_x6, star_x7, star_x8, star_x9, star_x10]
        sun_list = [cloud_x1, cloud_x2, cloud_x3, cloud_x4, cloud_x5, cloud_x6, cloud_x7, cloud_x8, cloud_x9, cloud_x10,
                    sun_x]
        t += 1
        if t < 200:
            # t += 1
            mag_cord_x -= 1
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
        if t > 200 and t < 400:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Привет, Дино.", False, (0, 0, 0))
                screen.blit(text, (930, 570))
                # t += 1
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hi, Dino.", False, (0, 0, 0))
                screen.blit(text, (930, 570))
        elif t >= 400 and t < 600:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Здравствуйте.", False, (0, 0, 0))
                screen.blit(text, (40, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Вы очень похожи", False, (0, 0, 0))
                screen.blit(text, (40, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("на мага воды.", False, (0, 0, 0))
                screen.blit(text, (40, 610))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Hello.", False, (0, 0, 0))
                screen.blit(text, (40, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("You look like", False, (0, 0, 0))
                screen.blit(text, (40, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("a water mag.", False, (0, 0, 0))
                screen.blit(text, (40, 590))
            # t += 1
        elif t >= 600 and t < 800:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я его брат.", False, (0, 0, 0))
                screen.blit(text, (930, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Как я понимаю, он уже", False, (0, 0, 0))
                screen.blit(text, (930, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("рассказал тебе про ", False, (0, 0, 0))
                screen.blit(text, (930, 610))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("нашу ситуацию.", False, (0, 0, 0))
                screen.blit(text, (930, 630))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("I am his brother.", False, (0, 0, 0))
                screen.blit(text, (930, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Has he already told you", False, (0, 0, 0))
                screen.blit(text, (930, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("about our situation?", False, (0, 0, 0))
                screen.blit(text, (930, 510))
        elif t >= 800 and t < 1000:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Да.", False, (0, 0, 0))
                screen.blit(text, (40, 570))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Yes.", False, (0, 0, 0))
                screen.blit(text, (40, 590))
        elif t >= 1000 and t < 1200:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я помогу тебе.", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Сим. Салабим.", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 590))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("I will help you.", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Sim. Salabim.", False,
                                 (0, 0, 0))
                screen.blit(text, (930, 590))
        elif t >= 1200 and t < 1400:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_right, (900, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Теперь ты можешь",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("извергать огненные шары.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render(" Они тебе помогут в",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 610))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("битве с чудовищем.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 630))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Now you can spew",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 370))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("fireballs. They will",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 590))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("help you in the battle",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 610))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("with the monster.",
                                 False,
                                 (0, 0, 0))
                screen.blit(text, (930, 630))
        elif t >= 1400 and t < 1600:
            screen.blit(mag_left, (mag_cord_x, mag_cord_y))
            screen.blit(dialog_left, (10, 500))
            if language == 'rus':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Я помогу вам.", False, (0, 0, 0))
                screen.blit(text, (40, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("До свидания.", False, (0, 0, 0))
                screen.blit(text, (40, 590))
            elif language == 'eng':
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render("Thanks. I will try.", False, (0, 0, 0))
                screen.blit(text, (40, 570))
                f2 = pygame.font.SysFont('arial', 18)
                text = f2.render(" to help. Goodbye.", False, (0, 0, 0))
                screen.blit(text, (40, 590))
        elif t >= 1600 and t < 1830:
            # t += 1
            mag_cord_x += 1
            screen.blit(mag_right, (mag_cord_x, mag_cord_y))
        elif t >= 1830:
            running = False
            # origin_dino(screen, color, score, HI, birthday_code, language, keys)

        score_out = []
        for i in range(1, len(score_str) + 1):
            score_out.insert(0, score_str[len(score_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        score_cord_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (score_cord_x, score_cord_y))
            score_cord_x += 30

        # преобразует лучший счет в поверхность и выводит ее:
        score_out = []
        HI_coard_y = 700
        screen.blit(HI_img, (870, 700))
        for i in range(1, len(HI_str) + 1):
            score_out.insert(0, HI_str[len(HI_str) - i])
        while len(score_out) != 5:
            score_out.insert(0, '0')
        HI_coard_x = 970
        for i in range(len(score_out)):
            screen.blit(nums_dict[score_out[i]], (HI_coard_x, HI_coard_y))
            HI_coard_x += 30
        pygame.display.flip()
