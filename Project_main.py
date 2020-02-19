class Face_Transform():
    """
    This concstitute the main App
    contains the main Thread
    This deals with the main GUI and its components
    """

    #print("hai")
    def __init__(self):
        import cv2 as cv
        import pygame as py
        import pygame_camera as CAMERA
        import numpy as np
        import dlib as dl
        import os
        import sys
        import time
        import random

        self.cv = cv
        self.os = os
        self.CAMERA = CAMERA
        self.py = py
        self.t = time
        self.sys = sys
        self.np = np
        self.dl = dl
        self.rdm = random
        self.clock = py.time.Clock()


        py.init()
        py.mixer.init()

        self.Exit = 0
        # Colors
        self.blue = 0, 0, 255
        self.cyan = 0, 255, 255
        self.black = 0, 0, 0
        self.red = 255, 0, 0
        self.white = 255, 255, 255
        self.pale_blue = 190, 150, 255
        self.yellow = 255, 255, 0
        self.green = 0, 255, 10
        self.orange = 255, 50, 0
        self.indigo = 20, 0, 255
        self.pink_grad = 212, 0, 255


        #self.glasses = self.cv.CascadeClassifier('harcascade_eye_tree_eyeglasses.xml')

        #All_sprites_loading
        self.bg_img = py.image.load("Background_imgs/H_F_digi_grid_1024x683.jpg")

        ## Are_you_sure page related
        #is just emonji set

        ##Home page related
        self.Proceed_bg = py.image.load("Sprite_imgs/proceed_bg3.png")
        self.Name_bg = py.image.load("Sprite_imgs/FAce_mask_bg.png")
        self.face_num_bg = py.image.load("Sprite_imgs/face_number_bg.png")

        self.settings_bg = py.image.load("Sprite_imgs/proceed_bg2.png")
        # self.Proceed_bg = None
        # self.Proceed_bg = None

        #Mask_set
        import string
        ele = []
        for val in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            for i in range(6):
                ele.append(val + str(i).upper())
        loc = "Face_masks/"
        # print(ele)
        # print(loc + key + '.png' for key in ele)
        self.Mask_set = {key: py.image.load(loc + key + '.png') for key in ele}

        #Event_imgs
        self.Event_set = {
            "undo":      py.image.load("Event_imgs/icons8-undo-64.png"),
            "redo":      py.image.load("Event_imgs/icons8-redo-64.png"),
            "faces":     py.image.load("Event_imgs/icons8-theatre-capture-96.png"),
            "settings":  py.image.load("Event_imgs/icons8-settings-64.png"),
            "export":    py.image.load("Event_imgs/export_64px.png"),
            "org" :      py.image.load("Event_imgs/icons8-org-64.png"),
            #"forward":   py.image.load("Event_imgs/icons8-forward-button-64.png"),
            #"backward":  py.image.load("Event_imgs/icons8-back-arrow-64-1.png"),
            "DL":        py.image.load("Event_imgs/icons8-double-left-64.png"),
            "DR":        py.image.load("Event_imgs/icons8-double-right-64.png"),
            "click":     py.image.load("Event_imgs/icons8-top-view-64.png"),
            "capture2":  py.image.load("Event_imgs/icons8-pictures-CAPTURE-64.png"),
            "sad_sun":   py.image.load("Event_imgs/icons8-sad-sun-64.png"),
            "capture":   py.image.load("Event_imgs/icons8-face-id-64.png"),
            "happy":     py.image.load("Event_imgs/icons8-happy-64.png"),
            "add_text":  py.image.load("Event_imgs/icons8-color-48.png"),

            "HOME"    :  py.image.load("Event_imgs/icons8-home-64.png"),
            "DWLD"    :  py.image.load("Event_imgs/icons8-download-40.png")

        }

        self.Funny_emonjis =[
           py.image.load("Funny_emonjis/icons8-dove-8.png"),
           py.image.load("Funny_emonjis/icons8-dove-16.png"),
           py.image.load("Funny_emonjis/icons8-dove-20.png"),
           py.image.load("Funny_emonjis/icons8-geometric-flowers-16.png"),
           py.image.load("Funny_emonjis/icons8-geometric-flowers-32.png"),
           py.image.load("Funny_emonjis/icons8-gradient-line-8.png"),
           py.image.load("Funny_emonjis/icons8-gradient-line-16.png"),
           py.image.load("Funny_emonjis/icons8-gradient-line-20.png"),
           py.image.load("Funny_emonjis/icons8-lotus-8.png"),
           py.image.load("Funny_emonjis/icons8-lotus-16.png"),
           py.image.load("Funny_emonjis/icons8-lotus-20.png"),
           py.image.load("Funny_emonjis/icons8-geometric-flowers-16.png"),
           py.image.load("Funny_emonjis/icons8-geometric-flowers-32.png") ,
                   ]

        #Mask_Button_Set

        #Emonji_Set
        self.Emonji_Set = {
           "sun": py.image.load("Funny_emonjis/icons8-sun-96.png"),
           "sad_sun":   py.image.load("Funny_emonjis/icons8-sad-sun-96.png")
        }

        #control set
        self.Control_set = {

                             "Anm_mask":    py.image.load("Controls/icons8-anonymous-mask-64.png"),

                             "Eye":         py.image.load("Controls/icons8-eye-64(2).png"),

                             "Flip":        py.image.load("Controls/icons8-flip-horizontal-64.png"),

                             "Grid":        py.image.load("Controls/icons8-grid-64.png"),

                             "Music":       py.image.load("Controls/icons8-music-64.png"),

                             "Sound":       py.image.load("Controls/icons8-musical-notes-64.png"),

                             "Ntf":         py.image.load("Controls/icons8-notification-64.png"),

                             "Gears":       py.image.load("Controls/icons8-gears-16.png"),

                             "delete":      py.image.load("Controls/icons8-delete-25.png")


                             }

        #Effect Button set

        self.Effect_Button_set = {

            "yellow": py.image.load("Effect_button_Set/sh_bn1.png"),
            "red":    py.image.load("Effect_button_Set/shbn2.png"),
            "green":  py.image.load("Effect_button_Set/sh_bn3.png"),
            "black":  py.image.load("Effect_button_Set/shbn4.png"),
            "blue":   py.image.load("Effect_button_Set/sbn5.png"),
            "violet": py.image.load("Effect_button_Set/sbn6.png")

            #,py.image.load("Effect_button_Set/sh_bn1.png")

            }



        ###animation blits
        self.drone = py.image.load("Sprite_imgs/Drone-PNG-Photos.png")
        self.flying_stork1 = py.image.load("Sprite_imgs/icons8-flying-stork-with-bundle-48.png")
        self.flying_stork2 = py.image.load("Sprite_imgs/icons8-flying-stork-with-bundle-48(1).png")
        self.mouth_happy = py.image.load("Sprite_imgs/icons8-smiling-mouth-100.png")
        self.mouth_sad = py.image.load("Sprite_imgs/icons8-monster-mouth-64.png")
        self.eye = py.image.load("Sprite_imgs/icons8-eye-48.png")
        self.nose = py.image.load("Sprite_imgs/icons8-smelling-80.png")
        #self.comp_anims = [A1, A2, A3, A2, A1]
        ###
        #
        ##All global settings flags

        self.global_effects = {}

        ##motion sprites

        self.Motion_set = {
                          "undo":      py.image.load("Motion_sprites/icons8-undo-64(1).png"),
                          "redo":      py.image.load("Motion_sprites/icons8-redo-64.png"),
                          "org" :      py.image.load("Motion_sprites/icons8-event-64.png"),
                          "export":    py.image.load("Motion_sprites/icons8-export-64.png"),
                          "Sound":     py.image.load("Motion_sprites/icons8-musical-notes-64(1).png"),
                          "Music":     py.image.load("Motion_sprites/icons8-music-64(1).png"),

                          "Ntf":        py.image.load("Motion_sprites/icons8-notification-64(1).png"),
                          "Grid":       py.image.load("Motion_sprites/icons8-grid-64(1).png"),
                          "Flip":       py.image.load("Motion_sprites/icons8-flip-horizontal-64.png"),
                          "Anm_mask":   py.image.load("Motion_sprites/icons8-anonymous-mask-64(1).png"),
                          "Eye":        py.image.load("Motion_sprites/icons8-eye-64(3).png"),
                          "add_text":   py.image.load("Motion_sprites/icons8-color-48(1).png"),
                          "capture" :   py.image.load("Motion_sprites/icons8-face-id-64.png"),

                           "Gears":     py.image.load("Motion_sprites/icons8-gears-16(2).png"),
                           "click":     py.image.load("Motion_sprites/icons8-top-view-64.png"),

                           "settings":  py.image.load("Motion_sprites/icons8-settings-64.png"),

                           "h_sun":     py.image.load("Motion_sprites/icons8-sun-96(1).png"),
                           "s_sun":     py.image.load("Motion_sprites/icons8-sad-sun-96(1).png"),
                            "delete":   py.image.load("Motion_sprites/icons8-delete-25.png"),

                            "HOME"   :  py.image.load("Motion_sprites/icons8-home-64(1).png"),
                            "DWLD"   :  py.image.load("Motion_sprites/icons8-download-40.png"),
                           #py.image.load(""),
                        }

        #### Machine learning moddel_paths
        self.model_paths = ["models/candy.t7",
                            "models/composition_vii.t7",
                            "models/feathers.t7",
                            "models/la_muse.t7",
                            "models/mosaic.t7",
                            "models/starry_night.t7",
                            "models/the_scream.t7",
                            "models/the_wave.t7",
                            "models/udnie.t7"
        ]
        self.up_arr = self.py.image.load("Sprite_imgs/icons8-sort-up-32(1).png")
        self.dwn_arr = self.py.image.load("Sprite_imgs/icons8-sort-down-32.png")

    def color_generator(self):
        """
        It generates random color
        :return: Ntg
        """

        while True:
            colors = []
            for i in range(3):
                Num = self.rdm.randint(0, 255)
                colors.append(Num)

            yield colors

    def Drawing_Text(self, screen, x_pos, y_pos, text, text_style, text_size, text_color,bg_color = None, max_width = 718, max_height = 478):
        #print("\nDrawing\n")
        """
        Draws text onto screen

        :param screen:
        :param x_pos:
        :param y_pos:
        :param text: text to be drawn
        :param text_style:
        :param text_size:
        :param text_color:
        :param bg_color
        :return: tot_len that is printed on screen
        """
        tot_len = 0
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        font = self.py.font.SysFont(text_style, text_size)
        space = font.size(' ')[0]  # The width of a space.
        x, y = x_pos, y_pos
        width, height = 0, 0

        for line in words:
            for word in line:
                word_surface = font.render(word, 1, text_color,bg_color)
                word_width, word_height = word_surface.get_size()
                width, height = word_width, word_height
                if x + word_width >= max_width:
                    x = x_pos  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
                tot_len += x
            x = x_pos # Reset the x.
            y += height
        return tot_len



    def Create_Window(self, width, height, bg_color, caption):
        """
        Draws a window onto screen
        :param width: width of the window to be created
        :param height: Height of the window to be created
        :param bg_color: Back ground color of the window
        :param caption: Name of the window
        :return: a window
        """
        #print("Creating")
        screen = self.py.display.set_mode((width, height))
        screen.fill(bg_color)
        self.py.display.set_caption(caption)
        return screen

    def Settings_page_maker(self,screen):
        """
        This contains the globals settings and settings page related stuff
        :param screen:
        :return:
        """
        Settings_page_end = False
        while not Settings_page_end:
            mouse_pos = self.py.mouse.get_pos()
            #print(mouse_pos)
            screen.fill(self.black)
            screen.blit(self.bg_img, (0,0))
            TEXTS = ["Bg_Music", "Sound", "Notify", "Grid", "Flip", "Face_Rect", "Eyes_Rect"]
            y = 20
            l = len(TEXTS)
            for i in range(l):
                self.Drawing_Text(screen, 50, y,  TEXTS[i] + ": ", "times", 30, self.black, self.yellow)
                y += 60

            TEXTS = ["Sound", "Music", "Ntf", "Grid", "Flip", "Anm_mask", "Eye"]
            screen.blit(self.Control_set["Sound"], (600, 5))
            screen.blit(self.Control_set["Music"], (600, 55))
            y = 125
            l = len(TEXTS)
            for i in range(2, l):
                screen.blit(self.Control_set[TEXTS[i]], (600, y))
                y += 60
            screen.blit(self.Control_set["Gears"], (290, 197))
            screen.blit(self.Control_set["Gears"], (409, 197))

            x1, x2 = 610, 650 ##displaying positions


            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    Settings_page_end = True
                if event.type == self.py.KEYDOWN:
                    if event.key == self.py.K_q:
                        Settings_page_end = True
                if event.type == self.py.MOUSEBUTTONDOWN:

                    if (x1 <mouse_pos[0]< x2) and (19< mouse_pos[1] < 51):
                        if self.py.mouse.get_pressed()[0] == True:
                            if(self.app_settings["bgm"] == 1):
                                self.py.mixer.music.pause()
                                #self.py.mixer.music.set_endevent()
                                self.app_settings["bgm"] = 0
                            else:
                                #self.py.mixer.music.load("sounds/Turtle_Time.mp3")
                                self.py.mixer.music.unpause()
                                self.app_settings["bgm"] = 1
                    self.clock.tick(4)
                    if (x1 <mouse_pos[0]< x2) and (73< mouse_pos[1] < 109):
                        if self.py.mouse.get_pressed()[0] == True:
                            if (self.app_settings["snd"] == 1):
                                self.py.mixer.music.pause()
                                #self.py.mixer.music.set_endevent()
                                self.app_settings["snd"] = 0

                            else:
                                self.py.mixer.music.unpause()
                                self.app_settings["snd"] = 1
                    self.clock.tick(4)
                    if  (x1 <mouse_pos[0]< x2) and (140< mouse_pos[1] < 180):
                        if self.py.mouse.get_pressed()[0] == True:
                            if (self.app_settings["ntfy"] == 1):
                                self.app_settings["ntfy"] = 0
                            else:
                                self.app_settings["ntfy"] = 1
                    self.clock.tick(4)
                    if (x1 <mouse_pos[0]< x2) and (192< mouse_pos[1] < 232):
                        if self.py.mouse.get_pressed()[0] == True:
                            if self.py.mouse.get_pressed()[0] == True:
                                if (self.app_settings["grid"] == 1):
                                    self.app_settings["grid"] = 0

                                else:
                                    self.app_settings["grid"] = 1
                    self.clock.tick(4)
                    if (x1 <mouse_pos[0]< x2) and (259< mouse_pos[1] < 294):
                        if self.py.mouse.get_pressed()[0] == True:
                            if self.py.mouse.get_pressed()[0] == True:
                                if (self.app_settings["flip"] == 1):
                                    self.app_settings["flip"] = 0

                                else:
                                    self.app_settings["flip"] = 1
                    self.clock.tick(4)
                    if (x1 <mouse_pos[0]< x2) and (316< mouse_pos[1] < 354):
                        if self.py.mouse.get_pressed()[0] == True:
                            if self.py.mouse.get_pressed()[0] == True:
                                if (self.app_settings["frct"] == 1):
                                    self.app_settings["frct"] = 0

                                else:
                                    self.app_settings["frct"] = 1
                    self.clock.tick(4)
                    if (x1 <mouse_pos[0]< x2) and (385< mouse_pos[1] < 416):
                        if self.py.mouse.get_pressed()[0] == True:
                            if self.py.mouse.get_pressed()[0] == True:
                                if (self.app_settings["erct"] == 1):
                                    self.app_settings["erct"] = 0

                                else:
                                    self.app_settings["erct"] = 1
                    self.clock.tick(4)
            #settings icons
            if (x1 <mouse_pos[0]< x2) and (19< mouse_pos[1] < 51):
                screen.blit(self.Motion_set["Sound"], (600, 5))

            if  (x1 <mouse_pos[0]< x2) and (73< mouse_pos[1] < 109):
                screen.blit(self.Motion_set["Music"], (600,55))

            if  (x1 <mouse_pos[0]< x2) and (140< mouse_pos[1] < 180):
                screen.blit(self.Motion_set["Ntf"], (600, 125))

            if  (x1 <mouse_pos[0]< x2) and (192< mouse_pos[1] < 232):
                screen.blit(self.Motion_set["Grid"], (600, 185))

            if  (x1 <mouse_pos[0]< x2) and (259< mouse_pos[1] < 294):
                screen.blit(self.Motion_set["Flip"], (600, 245))

            if  (x1 <mouse_pos[0]< x2) and (316< mouse_pos[1] < 354):
                screen.blit(self.Motion_set["Anm_mask"], (600, 305))

            if  (x1 <mouse_pos[0]< x2) and (385< mouse_pos[1] < 416):
                screen.blit(self.Motion_set["Eye"], (600, 365))

            ##displaying close and delete
            if not self.app_settings["bgm"]:
                screen.blit(self.Control_set["delete"], (655, 24))
            if not self.app_settings["snd"]:
                screen.blit(self.Control_set["delete"], (655, 78))
            if not self.app_settings["ntfy"]:
                screen.blit(self.Control_set["delete"], (655, 140))
            if not self.app_settings["grid"]:
                screen.blit(self.Control_set["delete"], (655, 192))
            if not self.app_settings["flip"]:
                screen.blit(self.Control_set["delete"], (655, 259))
            if not self.app_settings["frct"]:
                screen.blit(self.Control_set["delete"], (655, 316))
            if not self.app_settings["erct"]:
                screen.blit(self.Control_set["delete"], (655, 385))

            self.py.display.update()
            self.clock.tick(2)

    def ARE_YOU_SURE(self,screen):
        """
        This is the confirmation window
        :param screen: screen
        :return: Ntg
        """
        self.py.mixer.music.pause()

        AYS_page_end = False
        color = self.color_generator()
        while not AYS_page_end:
            mouse_pos = self.py.mouse.get_pos()
            flag = True
            #print("mouse_pos", mouse_pos)
            screen.fill(self.black)
            screen.blit(self.bg_img, (0, 0))
            self.py.draw.rect(screen, self.black, self.py.Rect(258, 125, 218, 40))
            self.Drawing_Text(screen, 260, 129, "ARE YOU SURE", "times", 30, next(color))


            screen.blit(self.Emonji_Set["sad_sun"], (60, 200))
            screen.blit(self.Emonji_Set["sun"], (560, 200))

            screen.blit(self.eye, (278, 180))
            screen.blit(self.eye, (393, 180))
            screen.blit(self.nose, (321, 230))

            self.py.draw.rect(screen, self.pale_blue, self.py.Rect(66, 300, 80, 40))
            self.Drawing_Text(screen,76 , 302, "YES", "times", 30, self.black)
            self.py.draw.rect(screen, self.pale_blue, self.py.Rect(566, 300, 80, 40))
            self.Drawing_Text(screen, 586, 302, "NO", "times", 30, self.black)

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    AYS_page_end = True
                if event.type == self.py.MOUSEBUTTONDOWN:
                    if (66 < mouse_pos[0] < 146) and (300 < mouse_pos[1] < 340):
                        self.gameLoop = False
                        self.py.mixer.quit()
                        self.py.quit()
                        self.sys.exit(0)

                    if (566 < mouse_pos[0] < 646) and (300 < mouse_pos[1] < 340):
                        if self.py.mouse.get_pressed()[0] == True:
                            self.py.mixer.music.unpause()
                            AYS_page_end = True

            if (66 < mouse_pos[0] < 146) and (300 < mouse_pos[1] < 340):
                self.py.draw.rect(screen, self.red, self.py.Rect(66, 300, 80, 40))
                self.Drawing_Text(screen, 76, 302, "YES", "times", 30, self.black)
                screen.blit(self.Motion_set["s_sun"], (60, 200))
                flag = False
            if (566 < mouse_pos[0] < 646) and (300 < mouse_pos[1] < 340):
                self.py.draw.rect(screen, self.blue, self.py.Rect(566, 300, 80, 40))
                self.Drawing_Text(screen, 586, 302, "NO", "times", 30, self.black)
                screen.blit(self.Motion_set["h_sun"], (560, 200))

            if (flag): screen.blit(self.mouth_happy, (310, 279))
            self.py.display.flip()
            self.clock.tick(600)

    def Frame_changer(self, frame, option):
        """

        :param frame: cv2 frame object
        :param option: integer
        :return: modified frame
        """

        Effect_names = ["SLE", "RED", "GRE", "B/W", "BLU", "MAG"]
        self.magic = False

        if option == "ORG":
            return frame
        elif option == "B/W":
            return self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)
        elif option == "EDG":
            frame = self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)
            return self.cv.Canny(frame, 50, 100)
        elif option == "GRE":
            Conv_hsv_Gray = self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)
            ret, mask = self.cv.threshold(Conv_hsv_Gray, 0, 255, self.cv.THRESH_BINARY_INV | self.cv.THRESH_OTSU)
            indices = self.np.where(mask <= 150)

            for x, y in zip(indices[0], indices[1]):
                if (0 < y < 636) and (56 < x < 416):
                    frame[x, y] = [0, 255, 0]
            indices = self.np.where(mask > 150)

            for x, y in zip(indices[0], indices[1]):
                if (0 < y < 636) and (56 < x < 416):
                    frame[x, y] = [25, 25, 0]

            return frame

        elif option == "BLU":
            Conv_hsv_Gray = self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)
            ret, mask = self.cv.threshold(Conv_hsv_Gray, 0 , 255, self.cv.THRESH_BINARY_INV | self.cv.THRESH_OTSU)
            indices = self.np.where(mask <= 150)

            for x,y in zip(indices[0], indices[1]):
                if(0 < y < 636) and (56 < x < 416):
                    frame[x, y] = [255, 0, 0]
            indices = self.np.where(mask > 150)

            for x,y in zip(indices[0], indices[1]):
                if(0 < y < 636) and (56 < x < 416):
                    frame[x, y] = [0, 0, 0]

            return frame
        elif option == "RED":

            Conv_hsv_Gray = self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)

            ret, mask = self.cv.threshold(Conv_hsv_Gray, 0, 255, self.cv.THRESH_BINARY_INV | self.cv.THRESH_OTSU)
            indices = self.np.where(mask <= 150)

            frame[indices[0], indices[1], :] = [0, 0, 255]

            indices = self.np.where(mask > 150)
            frame[indices[0], indices[1], :] = [0, 0, 0]
            return frame
        elif option == "MAG":
            self.magic = True
        return frame


    def detect(self, gray):
        detector = self.dl.get_frontal_face_detector()

        predictor = self.dl.shape_predictor("shape_predictor_68_face_landmarks.dat")

        faces_coords = []
        FACE_MARKS = []

        faces = detector(gray)
        for face in faces:
            #print(face)
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            faces_coords.append([x1, y1, x2-x1, y2-y1])
            self.cv.rectangle(gray, (x1, y1), (x2, y2), (0, 255, 0), 3)

            landmarks = predictor(gray, face)
            FACE_MARKS.append(landmarks)

        return faces_coords, FACE_MARKS

    def notify(self,screen, text,bg_color, position, t_color = (255, 255, 255)):
        """

        :param text: str
        :param bg_color: tuple
        :param position: tuple
        :param t_color: tuple
        :return: ntg
        """

        Len = len(text)
        c = Len
        b = 10
        l = 20
        while(c > 8):
            l += 20
            b += 10
            c -= 8


        self.py.draw.rect(screen, bg_color, [position[0], position[1],l + position[0], b + position[1] ], 0)
        c = Len
        l = 0
        if(c <= 8):
            self.Drawing_Text(screen, position[0] + 2, position[1] + 2, text, "times", 25, t_color)
        while(c > 8):
            self.Drawing_Text(screen, position[0] + 2, position[1] + 2,text[l:l+ 8], "times", 25, t_color)
            l += 8
            position[1] += 10
            c -= 8

    def draw_grid(self, screen, x, y, width, height, horx, very):
        for i in range(x, width,horx):
            self.py.draw.line(screen, self.blue, (i, y), (i, height), 1)


        for i in range(y, height, very):
            #print("bye  ", i)
            self.py.draw.line(screen, self.blue, (x, i), (width, i), 1)


    def End_page_window(self, screen, frame,current_Mask,face_coords, ARGS = None):
        page_end = False
        save_flag = False
        while not page_end:
            print("Positions in end page, ",self.py.mouse.get_pos())
            pos = self.py.mouse.get_pos()
            screen.fill(self.black)
            screen.blit(frame, (40,0))
            if current_Mask != None:
                for fc in face_coords:
                    screen.blit(self.Mask_set[current_Mask] ,
                                (fc[0] - self.Mask_position_diff_set[current_Mask][0] + 40 ,
                                 fc[1] - self.Mask_position_diff_set[current_Mask][1] + 4))
            #self.Drawing_Text()
            self.py.draw.rect(screen, self.black, self.py.Rect(680, 1, 717, 478), 0)
            self.py.draw.rect(screen, self.black, self.py.Rect(39, 416, 640, 477), 0)
            screen.blit(self.Event_set["HOME"], (87, 418))
            screen.blit(self.Event_set["DWLD"], (593, 426))
            screen.blit(self.Event_set["settings"], (315, 418))
            if ARGS != None:
                self.Drawing_Text(screen, ARGS[0][0] + 40, ARGS[0][1], ARGS[1], ARGS[3], ARGS[2], ARGS[4])
            if save_flag:
                self.Drawing_Text(screen, 40, 12, "Successfully saved", "times", 30, self.green)
                self.Drawing_Text(screen, 280, 12, "GOTO ->","times", 30, self.blue)
                self.Drawing_Text(screen, 400, 12, "C:\\F_T_pictures", "times", 30, self.yellow)


            if 95 < pos[0] < 136 and 435 < pos[1] < 469:
                screen.blit(self.Motion_set["HOME"], (87, 418))
            if 325 < pos[0] < 364 and 435 < pos[1] < 469:
                screen.blit(self.Motion_set["settings"], (315, 418))
            if 601 < pos[0] < 632 and 435 < pos[1] < 469:
                screen.blit(self.Motion_set["DWLD"], (593, 426))


            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    self.cam_End = False
                    page_end = True
                if event.type == self.py.KEYDOWN:
                    keypressed = self.py.key.get_pressed()
                    if (keypressed[self.py.K_LCTRL] or keypressed[self.py.K_RCTRL]) and keypressed[self.py.K_s] == True:
                        if not save_flag:
                            currpath = r'C:\F_T_pictures'
                            if not self.os.path.exists(currpath):
                                self.os.makedirs(currpath)
                            INT = self.rdm.randint(0, 999)
                            file = "img" + str(INT) + ".jpeg"
                            while file in self.os.path.abspath(currpath):
                                file = "img" + str(self.rdm.randint(0, 999)) + "jpeg"
                            rect = self.py.Rect(40, 60, 640, 361)
                            sub = screen.subsurface(rect)
                            self.py.image.save(sub, self.os.path.abspath(currpath + "\\" + file))
                            save_flag = True
                            self.Drawing_Text(screen, 40, 12, r"   Saving......   ", "times", 30, self.red)
                        self.clock.tick(200)
                    if keypressed[self.py.K_h] == True:
                        page_end = True
                    if keypressed[self.py.K_SPACE]:
                        self.Settings_page_maker(screen)
                if event.type == self.py.MOUSEBUTTONDOWN:
                    if 95 < pos[0] < 136 and 435 < pos[1] < 469:
                        page_end = True
                    if 325 < pos[0] < 364 and 435 < pos[1] < 469:
                        self.Settings_page_maker(screen)
                    if 601 < pos[0] < 632 and 435 < pos[1] < 469:
                        #self.py.Surface.lock(screen)
                        if not save_flag:
                            currpath = r'C:\F_T_pictures'
                            if not self.os.path.exists(currpath):
                                self.os.makedirs(currpath)
                            INT = self.rdm.randint(0,999)
                            file = "img" + str(INT) + ".jpeg"
                            while file in self.os.path.abspath(currpath):
                                file = "img" + str(self.rdm.randint(0, 999)) + "jpeg"
                            rect = self.py.Rect(40, 60, 640, 361)
                            sub = screen.subsurface(rect)
                            self.py.image.save(sub, self.os.path.abspath(currpath + "\\" + file))
                            save_flag = True
                            self.Drawing_Text(screen, 40, 12, r"   Saving......   ", "times", 30, self.red)
                        self.clock.tick(200)
            self.py.display.flip()
            self.clock.tick(20)
        ##Creating another instance
        Obj = Main()
        Obj.proceed()

    def get_fonts(self):
        available = self.py.font.get_fonts()
        # get_fonts() returns a list of lowercase spaceless font names
        op = []
        for font in available:
            op.append(font)
        return op

    def A_T_W_shift_1(self,screen, TEXT = None, SIZE = None):
        shift_end = False
        Max = 1140
        color_inactive = self.py.Color('lightskyblue3')
        color_active = self.py.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        cursor = '|'
        size = 30
        if SIZE != None:
            size = SIZE
        if TEXT != None:
            text = TEXT
        Min_size, Max_size = 20 , 200

        while not shift_end:
            Total_len = len(text)
            Rem = Max - Total_len
            if(Rem == 0):
                color = color_inactive
                cursor = " "
            mouse_pos = self.py.mouse.get_pos()
            ##print("Mouse_pos:-", mouse_pos)
            #print(mouse_pos)
            screen.fill(self.black)
            screen.blit(self.Proceed_bg, (546, 3))
            self.Drawing_Text(screen, 584, 15, "NEXT", "times", 35, self.black)
            input_box = self.py.Rect(0, 66, 718, 412)

            # Rectangles as backgrounds
            self.py.draw.rect(screen, self.pink_grad, self.py.Rect(10, 11, 140, 50), 2)
            self.py.draw.rect(screen, color, input_box, 2)
            self.py.draw.rect(screen, self.pale_blue, self.py.Rect(177, 18, 100, 36), 2)
            self.py.draw.rect(screen, self.pale_blue, self.py.Rect(327, 18, 210, 36), 2)

            #increase or decrease size
            self.py.draw.rect(screen, self.pale_blue, self.py.Rect(277, 18, 40, 37), 0)
            self.py.draw.polygon(screen, self.yellow, [(280, 31), (297,20), (313,31)],0)
            self.py.draw.polygon(screen, self.yellow, [(280, 43), (297,54), (313,43)],0)
            self.py.draw.line(screen,self.black, (276, 37), (316, 37),2)
            #self.py.draw.polygon(screen, self.black, [(), (,), (,)],0)

            self.Drawing_Text(screen, 14, 20, "TEXT HERE", "times", 25, color)
            self.Drawing_Text(screen, 181, 23, "SIZE:" + str(size), "times", 25, self.green)
            self.Drawing_Text(screen, 331, 23, "REMAINING:" + str(Rem).zfill(4), "times", 25, self.green)

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    return None, None

                if event.type == self.py.KEYDOWN:
                    if event.key == self.py.K_q:
                        return None, None
                    if active:
                        if event.key == self.py.K_RETURN:
                            text += "\n"
                        elif event.key == self.py.K_BACKSPACE:
                            if(len(text) != 0):
                                text = text[:-1]
                        else:
                            if(Rem != 0):
                                text += event.unicode
                    else:
                        if event.key == self.py.K_RETURN:
                            active = not active
                            color = color_active if active else color_inactive

                if event.type == self.py.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive

                    if 556 < mouse_pos[0] < 704 and 7 < mouse_pos[1] < 60:
                        shift_end = True
                    if 276 < mouse_pos[0] < 316 and 20 < mouse_pos[1] < 35:
                        if size < Max_size :
                            size += 1
                        print("HIT")
                    if 276 < mouse_pos[0] < 316 and 39 < mouse_pos[1] < 54:
                        if Min_size < size:
                            size -= 1
                        print("Good HIT")

                if 556 < mouse_pos[0] < 704 and 7 < mouse_pos[1] < 60:
                    screen.blit(self.Proceed_bg, (548, 5))
                    self.Drawing_Text(screen, 586, 17, "NEXT", "times", 35, self.black)
                    self.clock.tick(20)
                if 276 < mouse_pos[0] < 316 and 20 < mouse_pos[1] < 35:
                    self.py.draw.polygon(screen, self.blue, [(280, 31), (297, 20), (313, 31)], 0)

                if 276 < mouse_pos[0] < 316 and 39 < mouse_pos[1] < 54:
                    self.py.draw.polygon(screen, self.blue, [(280, 43), (297, 54), (313, 43)], 0)
                self.clock.tick(400)
            Total_len = self.Drawing_Text(screen,input_box.x + 5, input_box.y + 5, text + cursor,
                              None, size, color)
            if cursor == "|":
                cursor = " "
            else:
                cursor = "|"

            self.py.display.flip()
            self.clock.tick(600)
        return text, size
    def A_T_W_shift_2(self,screen, FONT = None, COLOR = None):
        shift_end = False
        color = (199, 195, 189)
        color_active = self.pink_grad
        color_inactive = color
        R_A, G_A, B_A = 14, 100, 232
        A_colors = [color] * 3
        F_Boxes = [self.py.Rect(300, y, 230, 40) for y in range(120, 431, 62)]
        color_ch, font_ch = (R_A, G_A, B_A), "arial"
        if COLOR != None:
            R_A, G_A, B_A = COLOR
            color_ch = COLOR
        if FONT != None:
            font_ch = FONT
        R_A_Y, G_A_Y, B_A_Y = 364 - R_A, 364 - G_A, 364 - B_A
        fonts = self.get_fonts()
        start, end = 0, 5
        while not shift_end:
            mouse_pos = self.py.mouse.get_pos()
            color_ch = (R_A, G_A, B_A)

            screen.fill(self.black)
            self.py.draw.rect(screen, self.pink_grad, self.py.Rect(0,0,718, 478),2)
            screen.blit(self.Proceed_bg, (546, 3))
            self.Drawing_Text(screen, 584, 15, "NEXT", "times", 35, self.black)
            # Rectangles as backgrounds
            y = 50
            x = 33
            ##for color & font main rects
            self.py.draw.rect(screen, color, self.py.Rect(x,y,100,40), 2)
            self.Drawing_Text(screen, 42, 60, "COLOR", "times", 20, self.pink_grad)
            self.py.draw.rect(screen, color, self.py.Rect(x, y + 40, 233, 300), 2)

            self.py.draw.rect(screen, color, self.py.Rect(290,y,100,40), 2)
            self.Drawing_Text(screen, 302, 60, "FONT", "times", 20, self.pink_grad)
            self.py.draw.rect(screen, color, self.py.Rect(290,y + 40,250,350), 2)
            #indicator right
            #self.py.draw.rect(screen, color, self.py.Rect(), 2)
            y += 40
            ##for RGB
            Red_Box = self.py.Rect(53, y + 15,50,259)
            Green_Box = self.py.Rect(123,y + 15,50,259)
            Blue_Box = self.py.Rect(193,y + 15,50,259)
            self.py.draw.rect(screen, A_colors[0],Red_Box , 2)
            self.py.draw.rect(screen, A_colors[1], Green_Box , 2)
            self.py.draw.rect(screen, A_colors[2], Blue_Box, 2)

            R, G, B = 0,0,0
            x = 55
            curr = None
            for _ in range(3):
                y = 107
                for i in range(255, -1, -1):
                    if 55 == x:
                        R = i
                        curr = R_A_Y
                    elif 125 == x :
                        G = i
                        curr = G_A_Y
                    else:
                        B = i
                        curr = B_A_Y
                    self.py.draw.line(screen, (R, G, B), (x, y), (x + 46, y),1)
                    y += 1
                self.py.draw.line(screen, self.pink_grad, (x ,curr), (x + 46, curr), 1)
                x += 70



            self.Drawing_Text(screen, 73, 365, "R", "times", 20, self.pink_grad)
            self.Drawing_Text(screen, 137, 365, "G", "times", 20, self.pink_grad)
            self.Drawing_Text(screen, 208, 365, "B", "times", 20, self.pink_grad)

            self.Drawing_Text(screen, 73, 92, str(R_A), "times", 12, self.yellow)
            self.Drawing_Text(screen, 137, 92 , str(G_A), "times", 12, self.yellow)
            self.Drawing_Text(screen, 208, 92, str(B_A), "times", 12, self.yellow)
            # sample hexagon
            self.py.draw.polygon(screen,self.pink_grad, [(80,400), (80 + 150, 400),
                                 (80 + 150 +25, 430) ,(80 + 150, 460), (80, 460), (80 - 25, 430)],2)
            ##choosen color
            self.py.draw.polygon(screen, color_ch, [(82,402), (82 + 150, 402),
                                 (78 + 150 +25, 430) ,(82 + 150, 458), (82, 458), (82 - 25, 430)],0)

            ##font sub rects
            UP_Butt = self.py.Rect(370, 120 - 30 + 5, 100,20)
            Down_Butt = self.py.Rect(370,415 , 100, 20)

            self.py.draw.rect(screen,self.pink_grad,UP_Butt,0)
            screen.blit(self.up_arr, (403, 90))
            self.py.draw.rect(screen, self.pink_grad, Down_Butt, 0)
            screen.blit(self.dwn_arr, (403, 409))
            y = 120

            for i in range(5):
                c = self.white
                F_Box_C = [color] * 5
                if font_ch == fonts[start + i]:
                        F_Box_C[i] = self.pink_grad
                        c = self.yellow
                S = fonts[start + i]
                self.py.draw.rect(screen, F_Box_C[i], F_Boxes[i], 2)
                if F_Boxes[i].collidepoint(mouse_pos):
                    if F_Box_C[i] != self.pink_grad:
                        self.py.draw.rect(screen, self.green,F_Boxes[i], 2)
                if len(S) >= 10:
                    S = S[:10] + ".."
                self.Drawing_Text(screen, 305, y + 1, S, fonts[start + i], 30,c)
                y += 50 + 12

            ##sample
            self.py.draw.rect(screen, color, self.py.Rect(541, 219, 100, 40), 2)
            self.Drawing_Text(screen, 550, 229, "SAMPLE", "times", 20, self.pink_grad)
            self.py.draw.rect(screen, self.pink_grad, self.py.Rect(541, 260, 172 , 120), 2)
            self.Drawing_Text(screen, 548, 273, "I am Crazy",font_ch, 30, color_ch)

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    return None, None

                if event.type == self.py.MOUSEBUTTONDOWN:
                    # If the user clicked on the color boxes rect.
                    EVENT_PS = event.pos
                    L = len(fonts)

                    for i in range(0, 5):
                        if F_Boxes[i].collidepoint(EVENT_PS):
                            font_ch = fonts[start + i]

                    if UP_Butt.collidepoint(EVENT_PS):
                        if start >= 1:
                            start -= 1
                            end -= 1
                    if Down_Butt.collidepoint(EVENT_PS):
                        if end <= (L - 1):
                            start += 1
                            end += 1

                    if 107 <= EVENT_PS[1] <= 107 + 255 :
                        if Red_Box.collidepoint(EVENT_PS):
                            R_A =   107  + 255 - EVENT_PS[1]
                            R_A_Y = EVENT_PS[1]
                            self.py.draw.rect(screen, self.pink_grad, Red_Box, 2)
                            A_colors[0] = color_active
                            A_colors[1] = color_inactive
                            A_colors[2] = color_inactive

                        if Green_Box.collidepoint(EVENT_PS):
                            G_A = 107  + 255 - EVENT_PS[1]
                            G_A_Y = EVENT_PS[1]
                            self.py.draw.rect(screen, self.pink_grad, Green_Box, 2)
                            A_colors[1] = color_active
                            A_colors[0] = color_inactive
                            A_colors[2] = color_inactive

                        if Blue_Box.collidepoint(EVENT_PS):
                            B_A = 107  + 255 - EVENT_PS[1]
                            B_A_Y = EVENT_PS[1]
                            self.py.draw.rect(screen, self.pink_grad, Blue_Box, 5)
                            A_colors[2] = color_active
                            A_colors[0] = color_inactive
                            A_colors[1] = color_inactive

                    if 556 < mouse_pos[0] < 704 and 7 < mouse_pos[1] < 60:
                        shift_end = True

                if event.type == self.py.KEYDOWN:
                    keypressed = self.py.key.get_pressed()
                    EVENT_PS = mouse_pos
                    if keypressed[self.py.K_RETURN]:
                        shift_end = True
                    if keypressed[self.py.K_q]:
                        return None, None

                    if 107 <= EVENT_PS[1] <= 107 + 255:
                        if Red_Box.collidepoint(EVENT_PS):
                            if keypressed[self.py.K_UP] == True:
                                if 254 >= R_A:
                                    R_A += 1
                                    R_A_Y -= 1
                            if keypressed[self.py.K_DOWN] == True:
                                if 1 <= R_A:
                                    R_A -= 1
                                    R_A_Y += 1

                        if Green_Box.collidepoint(EVENT_PS):
                            if keypressed[self.py.K_UP] == True:
                                if 254 >= G_A:
                                    G_A += 1
                                    G_A_Y -= 1
                            if keypressed[self.py.K_DOWN] == True:
                                if 1 <= G_A:
                                    G_A -= 1
                                    G_A_Y += 1
                        if Blue_Box.collidepoint(EVENT_PS):
                            if keypressed[self.py.K_UP] == True:
                                if 254 >= B_A:
                                    B_A += 1
                                    B_A_Y -= 1
                            if keypressed[self.py.K_DOWN] == True:
                                if 1 <= B_A:
                                    B_A -= 1
                                    B_A_Y += 1

            if 556 < mouse_pos[0] < 704 and 7 < mouse_pos[1] < 60:
                screen.blit(self.Proceed_bg, (548, 5))
                self.Drawing_Text(screen, 586, 17, "NEXT", "times", 35, self.black)
                self.clock.tick(20)
            if UP_Butt.collidepoint(mouse_pos):
                self.py.draw.rect(screen, self.green, UP_Butt, 2)
                print("very sad morning")

            if Down_Butt.collidepoint(mouse_pos):
                self.py.draw.rect(screen, self.green, Down_Butt, 2)
                print("very bad morning")

            self.py.display.flip()
            self.clock.tick(600)
        return font_ch, color_ch

    def A_T_W_shift_3(self,screen, TEXT, SIZE, FONT, COLOR):
        shift_end = False
        color_inactive = self.py.Color('lightskyblue3')
        pos_ch = (2, 66)
        pos_box = self.py.Rect(0, 60, 640, 355)
        text, size, font, color = TEXT, SIZE, FONT, COLOR
        while not shift_end:
            mouse_pos = self.py.mouse.get_pos()

            screen.fill(self.black)
            self.draw_grid(screen, 2, 62, 638, 413, 5, 5)
            ARGS = pos_ch, text, size, font, color
            if ARGS != None:
                self.Drawing_Text(screen, ARGS[0][0], ARGS[0][1], ARGS[1], ARGS[3], ARGS[2], ARGS[4])
            self.py.draw.rect(screen, self.black, [640, 1, 717, 478], 0)
            self.py.draw.rect(screen, self.black, [0, 416, 640, 477], 0)
            screen.blit(self.Proceed_bg, (548, 1))
            self.Drawing_Text(screen, 586, 13, "NEXT", "times", 35, self.black)

            screen.blit(self.Effect_Button_set["green"], (647, 150))
            self.Drawing_Text(screen, 652, 155, "T & S", "times", 25, self.black)

            screen.blit(self.Effect_Button_set["green"], (647, 250))
            self.Drawing_Text(screen, 652, 255, "F & C", "times", 25, self.black)

            # Rectangles as backgrounds
            self.py.draw.rect(screen, self.pink_grad, self.py.Rect(80, 11, 210, 45), 2)
            self.py.draw.rect(screen, self.pink_grad, pos_box, 2)

            self.Drawing_Text(screen, 84, 20, "PICK A POSITION", "times", 25, color)

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    return None

                if event.type == self.py.KEYDOWN:
                    keypress = self.py.key.get_pressed()
                    if keypress[self.py.K_RETURN] == True:
                        shift_end = True
                    if keypress[self.py.K_q]:
                        return  None
                    if keypress[self.py.K_t] == True or keypress[self.py.K_s] == True:
                        if text != None and size != None:
                            text, size = self.A_T_W_shift_1(screen, text, size)
                    if keypress[self.py.K_f] or keypress[self.py.K_c]:
                        if font != None and color != None:
                            font, color = self.A_T_W_shift_2(screen, font, color)

                if event.type == self.py.MOUSEBUTTONDOWN:
                    if pos_box.collidepoint(mouse_pos):
                        pos_ch = mouse_pos

                    if 558 < mouse_pos[0] < 706 and 5 < mouse_pos[1] < 48:
                        shift_end = True

                    if  647 < mouse_pos[0] < 707 and 150 < mouse_pos[1] < 190 :
                        if text != None and size != None:
                            text, size = self.A_T_W_shift_1(screen, text, size)
                    if 647 < mouse_pos[0] < 707 and 250 < mouse_pos[1] < 290 :
                        if font != None and color != None:
                            font, color = self.A_T_W_shift_2(screen, font, color)

            if 647 < mouse_pos[0] < 707 and 150 < mouse_pos[1] < 190:
                screen.blit(self.Effect_Button_set["green"], (649, 152))
                self.Drawing_Text(screen, 654, 157, "T & S", "times", 25, self.black)
            if 647 < mouse_pos[0] < 707 and 250 < mouse_pos[1] < 290:
                screen.blit(self.Effect_Button_set["green"], (649, 252))
                self.Drawing_Text(screen, 654, 257, "F & C", "times", 25, self.black)

            if 558 < mouse_pos[0] < 706 and 5 < mouse_pos[1] < 48:
                screen.blit(self.Proceed_bg, (550, 3))
                self.Drawing_Text(screen, 588, 15, "NEXT", "times", 35, self.black)
            if pos_box.collidepoint(mouse_pos):
                self.Drawing_Text(screen, 400, 20, str(mouse_pos), "times", 20, self.red)
            self.py.draw.circle(screen, self.yellow, pos_ch, 2, 0)
            self.Drawing_Text(screen, 300, 20, str(pos_ch), "times", 20, self.green)
            print("Mouse_pos:-", mouse_pos)

            self.py.display.flip()
            self.clock.tick(600)
        return pos_ch, text, size, font, color

    def Add_text_window(self,screen):

        TEXT, SIZE = self.A_T_W_shift_1(screen)
        FONT, COLOR, ARGS = (None,)*3
        if TEXT != None:
            FONT, COLOR = self.A_T_W_shift_2(screen)
        if FONT != None:
            ARGS = self.A_T_W_shift_3(screen, TEXT, SIZE, FONT, COLOR)
        if ARGS != None:
            self.clock.tick(200)
            return ARGS


    def Information_window(self,screen):
        inf_page_end = False
        while not inf_page_end:
            mouse_pos = self.py.mouse.get_pos()
            screen.fill(self.black)
            screen.blit(self.bg_img, (0, 0))
            TEXTS = ["Undo (Ctrl+Z)", "Redo (Ctrl+Y)", "Original (O)", "Export (Ctrl+E)", "Mask", "Click (Enter)", "Add_text (+/A)"]
            y = 20
            for i in range(len(TEXTS)):
                self.Drawing_Text(screen, 50, y, TEXTS[i] + " :", "times", 30, self.black, self.yellow)
                y += 60

            screen.blit(self.Event_set["undo"], (600, 5))
            screen.blit(self.Event_set["redo"], (600, 55))
            y = 125
            TEXTS = ["org", "export", "click", "capture", "add_text"]
            for i in range(len(TEXTS)):
                screen.blit(self.Event_set[TEXTS[i]], (600, y))
                y += 60

            screen.blit(self.eye, (278, 180))
            screen.blit(self.eye, (393, 180))

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    inf_page_end = True
                if event.type == self.py.KEYDOWN:
                    if event.key == self.py.K_q:
                        inf_page_end = True

            self.py.display.flip()
            self.clock.tick(600)

    def Redraw_Window(self,screen, frame,face_coords, landmarks, Effect_names,Mask_names, current_Mask, drone_pos = None, ARGS = None):

        #self.camera.set(3, 640)
        #self.camera.set(4, 480)

        #print("HERE HERE", frame.dtype, frame.shape)
        color = self.yellow

        draw_pts = [17, 21, 22, 26, 36, 39, 42,45]
        draw_lines = [(17, 21), (17, 36), (21, 39),(22, 26), (22, 42), (26, 45), (36, 41), (41, 39), (42, 46), (46, 45)]
        #extra = [, , , (36, 30), (39, 30), (42, 30),(45, 30), (48, 30) (48, 51), (48, 66),
        # (51, 54), (54, 30), (66, 54)]
        #pts = [45, 30, 48, 51, 54, 66]

        screen.blit(frame, (0, -4))

        if not self.cam_End :
            if self.app_settings["erct"] == 1:

                for LM in landmarks:
                    for n in draw_pts:

                        x = LM.part(n).x
                        y = LM.part(n).y

                        if 0 < x < 635 and 58 < y < 416:
                            self.py.draw.circle(screen, (199, 195, 189), (x, y), 3, 2)

                    for ele in draw_lines:
                        x1 = LM.part(ele[0]).x
                        y1 = LM.part(ele[0]).y
                        x2 = LM.part(ele[1]).x
                        y2 = LM.part(ele[1]).y

                        if 0 < x2 < 635 and 0 < y2 < 416:
                            self.py.draw.line(screen,(199, 195, 189),(x1, y1), (x2, y2), 1)

            if self.app_settings["frct"] == 1:
                for fc in face_coords:
                    print("here\n\n\n", fc)
                    if 120 <= fc[2] <= 160:
                        color = self.green
                    if 0 < fc[0] + fc[2] < 635 and 58 < fc[1] + fc[2] < 416:
                        self.py.draw.rect(screen, color , fc, 3)


        print("Mouse_pos",self.py.mouse.get_pos())
        ##Current Mask
        if current_Mask != None:

            if color == self.green:
                for fc in face_coords:
                    if 120 <= fc[2] <= 160:
                        if 0 < fc[0] + fc[2] < 635 and 58 < fc[1] + fc[2] < 416:
                            screen.blit(self.Mask_set[current_Mask],
                                        (fc[0] - self.Mask_position_diff_set[current_Mask][0],
                                         fc[1] - self.Mask_position_diff_set[current_Mask][1] ))

        if self.app_settings["grid"] == 1:
            self.draw_grid(screen, 0, 56, 640, 416, 91, 89)

        if ARGS != None:
            self.Drawing_Text(screen, ARGS[0][0], ARGS[0][1], ARGS[1], ARGS[3], ARGS[2], ARGS[4])
        self.py.draw.rect(screen, self.black, [640, 1, 717, 478], 0)
        self.py.draw.rect(screen, self.black, [0, 416, 640, 477], 0)

        self.py.draw.rect(screen, self.pink_grad, [640, 1, 717, 478], 2)
        self.py.draw.rect(screen, self.pink_grad, [0, 416, 640, 477], 2)


        # back and forward
        screen.blit(self.Event_set["undo"], (8, -4))
        screen.blit(self.Event_set["redo"], (78, -3))
        screen.blit(self.Event_set["org"], (510, -4))
        screen.blit(self.Event_set["export"], (578, -4))
        screen.blit(self.face_num_bg, (152, -10))
        # Text should be drawn
        self.Drawing_Text(screen, 234, -2, "Faces Found"
                          , "times", 36, self.green)
        self.Drawing_Text(screen, 421, -3,
                          str(len(face_coords)).center(3), "times", 56, self.yellow)

        ##Double arrows
        screen.blit(self.Event_set["DL"], (-10, 416))
        screen.blit(self.Event_set["DR"], (586,416))

        # capture center
        screen.blit(self.Event_set["capture"], (295, 418))

        #mask_bgs down sprites
        screen.blit(self.Event_set["click"], (62, 418))
        screen.blit(self.Event_set["click"], (142, 418))
        screen.blit(self.Event_set["click"], (222, 418))
        screen.blit(self.Event_set["click"], (370, 418))
        screen.blit(self.Event_set["click"], (450, 418))
        screen.blit(self.Event_set["click"], (530, 418))
        x,y = 62, 418
        #drawing text for the above various masks
        for i in range(6):
            if i == 3:
                x += 68
            self.Drawing_Text(screen,x + 21 , y + 22, Mask_names[i], "times", 24, self.green)
            x += 80

        #right side effects
        #settings
        screen.blit(self.Event_set["settings"], (650,6))

        screen.blit(self.Effect_Button_set["yellow"], (645, 73))

        screen.blit(self.Effect_Button_set["red"], (645, 133))
        screen.blit(self.Effect_Button_set["green"], (645, 193))
        screen.blit(self.Effect_Button_set["black"], (645, 253))
        screen.blit(self.Effect_Button_set["blue"], (645, 313))
        screen.blit(self.Effect_Button_set["violet"], (645, 373))
        #drwing text for above side buttons
        self.Drawing_Text(screen, 657, 82,  Effect_names[0], "times", 24, self.black)
        self.Drawing_Text(screen, 657, 142, Effect_names[1], "times", 24, self.white)
        self.Drawing_Text(screen, 657, 202, Effect_names[2], "times", 24, self.black)
        self.Drawing_Text(screen, 657, 262, Effect_names[3], "times", 24, self.white)
        self.Drawing_Text(screen, 657, 322, Effect_names[4], "times", 24, self.black)
        self.Drawing_Text(screen, 657, 382, Effect_names[5], "times", 24, self.white)

        screen.blit(self.Event_set["add_text"], (656, 422))

        if drone_pos != None:
            screen.blit(self.flying_stork1, drone_pos)
            screen.blit(self.flying_stork2, drone_pos)

        if self.magic:
            for i in range(100):
                pos = self.rdm.randint(0, 620), self.rdm.randint(68, 402)
                ch = self.rdm.randint(0, 12)
                screen.blit(self.Funny_emonjis[ch], pos)

    def change_music_settings(self, key):
        if self.app_settings[key] == 0:
            self.py.mixer.music.pause()
        else:
            self.py.mixer.music.unpause()

    def Home_page_window(self,screen):
        """
        This is the applications Home page
        :param screen:
        #:exit: used to check whether like close button got hit or not
        :return:
        """
        Homepage_end = False
        #if self.bg_music == "True":
        if self.app_settings["bgm"] == 1:
            self.py.mixer.music.play(-1)

        dr_pos  = [165, 460, 452]

        flag  = 0
        colors = self.color_generator()
        while not Homepage_end:
            self.change_music_settings("bgm")
            mouse_pos = self.py.mouse.get_pos()
            #Drawing section
            screen.fill(self.black)
            screen.blit(self.bg_img, (0,0))
            screen.blit(self.Name_bg, (7,40))
            self.Drawing_Text(screen, 110,60, "FACE-TRANSFORMER", "times", 50, self.pink_grad)
            self.Drawing_Text(screen, 277, 116, "-by PRAvEEN KuMaR", "times", 20, next(colors))
            screen.blit(self.settings_bg, (50,370))
            self.Drawing_Text(screen,62, 383, "SETTINGS","times",30,self.black )
            screen.blit(self.Effect_Button_set["green"], (333, 429))
            self.Drawing_Text(screen, 340, 437, "INFO", "times", 25, self.black)
            screen.blit(self.Proceed_bg, (500,370))
            self.Drawing_Text(screen, 518, 383, "PROCEED", "times", 30, self.black)

            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    self.py.mixer.music.pause()
                    #if I inclue MT , I shd pause threads
                    self.ARE_YOU_SURE(screen)
                    self.py.mixer.music.unpause()


                if event.type == self.py.MOUSEBUTTONDOWN:
                    if (70 < mouse_pos[0] < 214) and (374 < mouse_pos[1] < 429):
                        if self.py.mouse.get_pressed()[0] == True:
                            self.Settings_page_maker(screen)
                            #self.py.mixer.music.unpause()
                    if (333< mouse_pos[0] < 390) and (429 < mouse_pos[1] < 472):
                        self.Information_window(screen)

                    if (504 < mouse_pos[0] < 666) and (374 < mouse_pos[1] < 429):
                        if self.py.mouse.get_pressed()[0] == True:
                            Homepage_end = True
                            #goto settings page

                if event.type == self.py.KEYDOWN:
                    #print("key_down, key_down")
                    keypressed = self.py.key.get_pressed()
                    if keypressed[self.py.K_RETURN] == True or keypressed[self.py.K_RIGHT] == True:
                        Homepage_end = True
                        self.py.mixer.music.stop()
                        self.clock.tick(60)
                    if keypressed[self.py.K_SPACE] == True or keypressed[self.py.K_s] == True:
                        self.Settings_page_maker(screen)
                    if keypressed[self.py.K_i] == True:
                        self.Information_window(screen)


            if (70 < mouse_pos[0] < 214) and (374 < mouse_pos[1] < 429):
                screen.blit(self.settings_bg, (53, 372))
                self.Drawing_Text(screen, 65, 385, "SETTINGS", "times", 30, self.black)

            if (332< mouse_pos[0] < 388) and (429 < mouse_pos[1] < 472):
                screen.blit(self.Effect_Button_set["green"], (336, 431))
                self.Drawing_Text(screen, 342, 439, "INFO", "times", 25, self.black)

            if (504 < mouse_pos[0] < 666) and (374 < mouse_pos[1] < 429):
                screen.blit(self.Proceed_bg, (503, 372))
                self.Drawing_Text(screen, 521, 385, "PROCEED", "times", 30, self.black)


            screen.blit(self.drone, (dr_pos[0], dr_pos[2]))
            screen.blit(self.drone, (dr_pos[1], dr_pos[2]))

            if dr_pos[2] <= 320:
                screen.blit(self.mouth_happy, (310, 279))

            if dr_pos[2] <= 300:
                screen.blit(self.nose, (321, 230))

            if dr_pos[2] <= 205:
                screen.blit(self.eye, (278, 180))
                screen.blit(self.eye, (393, 180))
            k = 411, 300
            if not flag and dr_pos[2] > 130:
                #print("Hai")
                if dr_pos[2] > 411:
                    dr_pos[0] += 1
                    dr_pos[1] -= 1
                    dr_pos[2] -= 0.4

                elif dr_pos[2] > 294:
                    dr_pos[0] -=  1
                    dr_pos[1] +=  1
                    dr_pos[2] -= 0.8
                else:
                    dr_pos[2] -= 0.8
            else:
                if  dr_pos[2] > 66:
                    dr_pos[0] -= 1.5
                    dr_pos[1] += 1.5
                    dr_pos[2] -= 0.8
                else:
                    dr_pos[0] += 1.5
                    dr_pos[1] -= 1.5
                    flag = 1
            #self.t.sleep(123)
            if dr_pos[0] > 1000 and dr_pos[1] < -10 :
                flag = 0
                name_color = self.yellow
                dr_pos = [165, 460, 452]

            self.py.display.flip()
            self.clock.tick(600)


    def app_main(self):
        self.app_settings = {"bgm": 1, "snd": 1, "ntfy": 1, "grid": 0, "flip": 0, "frct": 1, "erct": 1}

        screen = self.Create_Window(720, 480, self.black, "Face_detection")
        App_main_Loop_end = False

        self.py.mixer.music.load("sounds/Turtle_Time.mp3")

        self.Home_page_window(screen)
        current_Effect = "org"
        current_Mask = None
        Event_STACK_M = [current_Mask, ]
        store = []
        
        self.py.mixer.music.load("sounds/Clover_3.mp3")
        self.py.mixer.music.play(-1)

        Effect_names = ["EDG", "RED", "GRE", "B/W", "BLU", "MAG"]

        vals = []
        Max_Masks = 24
        LET = ["A", 'B', 'C', 'D', 'E', 'F', "G"]
        MAX_LM = len(LET) - 1
        for ele in LET:
            for i in range(MAX_LM):
                vals.append(ele + str(i))
        self.Mask_position_diff_set = {
            vals[0] : (300, 200),
            vals[1] : (30,100),
            vals[2] : (30, 50),
            vals[3] : (45, 80),
            vals[4] : (40, 100),
            vals[5] : (60, 60),
        }
        self.Mask_position_diff_set.update({key: (0, 0) for key in vals[6:]})
        Display_drone = None
        X_dr , Y_dr = (-50,-50)

        ind = 0
        DL_End = False
        DR_End = True

        opt = "ORG"
        self.cam = False

        camera = self.cv.VideoCapture(0)

        ret, prev_frame = camera.read()
        self.cam_End = False
        self.magic = False
        #Picture_Q = Pic_gen()
        ARGS = None
        print("App started")
        while not App_main_Loop_end:
            self.change_music_settings("snd")

            pos = self.py.mouse.get_pos()
            #print("MPW pos", pos)

            screen.fill(self.black)
            # reading from self.camera
            if not self.cam_End :
                _, frame = camera.read()
                prev_frame = frame
            else:
                frame = prev_frame

            gray = self.cv.cvtColor(frame, self.cv.COLOR_BGR2GRAY)

            face_coords, landmarks = self.detect(gray)

            frame = self.Frame_changer(frame, opt)
            #frame = self.cv.cvtColor(frame, self.cv.COLOR_BGR2RGB)
            #frame = self.np.rot90(frame)
            self.cv.imwrite("temp.jpg", frame)
            frame = self.py.image.load("temp.jpg")
            #frame = self.py.surfarray.make_surface(frame)
            #frame = self.py.transform.flip(frame, True, False)

            Mask_names = [LET[ind] + str(i) for i in range(0, 6)]

            if Display_drone != None:
                if X_dr <= Display_drone[1][0] and Y_dr >= Display_drone[1][1]:
                    X_dr += 36
                    Y_dr -= 40
                else:
                    X_dr, Y_dr = Display_drone[0]


            self.Redraw_Window(screen, frame, face_coords, landmarks, Effect_names,Mask_names,
                               Event_STACK_M[-1], (X_dr, Y_dr), ARGS)

            ##Top Motion sprites
            if not self.cam_End :
                #undo
                if 16< pos[0] <60 and 11<pos[1]<48 :
                    screen.blit(self.Motion_set["undo"], (8, -4))
                #redo
                if 86< pos[0] <131 and 11< pos[1] <48:
                    screen.blit(self.Motion_set["redo"], (78, -3))
                #org
                if 521< pos[0] <564 and 12< pos[1] <52:
                    screen.blit(self.Motion_set["org"],(510, -4))

                ##DOWN Motion sprites
                if 5 < pos[0] < 38 and 424 < pos[1] < 477:
                    if not DR_End:screen.blit(self.Event_set["DL"], (-13, 416))
                if 603 < pos[0] < 632 and 424 < pos[1] < 477:
                    if not DL_End:screen.blit(self.Event_set["DR"], (589, 416))

                if 70 < pos[0] < 116 and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (62, 418))

                if  151 < pos[0] < 199 and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (142, 418))

                if  230 < pos[0] < 278  and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (222, 418))

                if  376 < pos[0] < 420  and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (370, 418))

                if 458 < pos[0] < 500  and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (450, 418))

                if 538 < pos[0] < 585 and 426 < pos[1] < 474:
                    screen.blit(self.Motion_set["click"], (530, 418))

                ##capture
                if 304 < pos[0] < 351 and 428 < pos[1] < 475:
                    screen.blit(self.Motion_set["capture"],(295, 418))

                #settings
                if 650 < pos[0] < 720 and 6 < pos[1] < 65:
                    screen.blit(self.Motion_set["settings"], (650, 6))
                #Add_text
                if 663 < pos[0] < 705 and 433 < pos[1] < 468 :
                    screen.blit(self.Motion_set["add_text"], (656, 422))
            else:
                # export
                if 585 < pos[0] < 621 and 6 < pos[1] < 52:
                    screen.blit(self.Motion_set["export"], (578, -4))

            x_pos_l , x_pos_r = 646, 713
            y_pos_l, y_pos_r = 75, 112
            blit_butt_x = 646
            draw_text_x = 658

            # right side effects

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["yellow"], (blit_butt_x, 75))
                # drwing text for above side buttons
                self.Drawing_Text(screen, draw_text_x, 84, Effect_names[0], "times", 24, self.black)

            y_pos_l = y_pos_r + 25
            y_pos_r = y_pos_l + 38

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["red"], (blit_butt_x, 135))
                self.Drawing_Text(screen, draw_text_x, 144, Effect_names[1], "times", 24, self.white)

            y_pos_l = y_pos_r + 25
            y_pos_r = y_pos_l + 38

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["green"], (blit_butt_x, 195))
                self.Drawing_Text(screen, draw_text_x, 204, Effect_names[2], "times", 24, self.black)

            y_pos_l = y_pos_r + 25
            y_pos_r = y_pos_l + 38

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["black"], (blit_butt_x, 255))
                self.Drawing_Text(screen, draw_text_x, 264, Effect_names[3], "times", 24, self.white)

            y_pos_l = y_pos_r + 25
            y_pos_r = y_pos_l + 38

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["blue"], (blit_butt_x, 315))
                self.Drawing_Text(screen, draw_text_x, 324, Effect_names[4], "times", 24, self.black)

            y_pos_l = y_pos_r + 25
            y_pos_r = y_pos_l + 38

            if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                screen.blit(self.Effect_Button_set["violet"], (blit_butt_x, 375))
                self.Drawing_Text(screen, draw_text_x, 384, Effect_names[5], "times", 24, self.white)

            ##All buttons
            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    # if I inclue MT , I shd pause threads
                        self.ARE_YOU_SURE(screen)

                if event.type == self.py.KEYDOWN:
                    keypressed = self.py.key.get_pressed()
                    if keypressed[self.py.K_o] == True:
                        self.ARE_YOU_SURE(screen)
                    if keypressed[self.py.K_RETURN] == True:
                        self.cam_End = True
                        self.clock.tick(3)
                    if (keypressed[self.py.K_LCTRL] or keypressed[self.py.K_RCTRL]) and keypressed[self.py.K_z] == True:
                        if len(Event_STACK_M) == 0:
                            current_Mask = None
                        else:
                            if len(Event_STACK_M) > 1:
                                temp = Event_STACK_M.pop()
                                store.append(temp)

                    if (keypressed[self.py.K_LCTRL] or keypressed[self.py.K_RCTRL]) and keypressed[self.py.K_z] == True:
                        if len(store) != 0:
                            temp = store.pop()
                            Event_STACK_M.append(temp)
                    if (keypressed[self.py.K_LCTRL] or keypressed[self.py.K_RCTRL]) and keypressed[self.py.K_e] == True:
                        self.clock.tick(3)
                        if self.cam_End == True:
                            self.End_page_window(screen, frame, current_Mask, face_coords, ARGS)
                            self.clock.tick(10)
                            camera = self.cv.VideoCapture(0)
                            Display_drone = None
                            self.cam_End = False

                    if keypressed[self.py.K_o] == True:
                        opt = "ORG"
                        current_Mask = None
                    if keypressed[self.py.K_SPACE] == True or keypressed[self.py.K_s] == True:
                        self.Settings_page_maker(screen)
                    if keypressed[self.py.K_PLUS] == True or keypressed[self.py.K_a] == True:
                        ARGS = self.Add_text_window(screen)
                    if keypressed[self.py.K_LEFT] == True:
                        if not DR_End and ind > 0:
                            ind -= 1
                        if ind == 0:
                            DR_End = True
                        else:
                            DR_End = False

                    if keypressed[self.py.K_RIGHT] == True:
                        if not DL_End and ind < MAX_LM:
                            ind += 1
                            DR_End = False
                        if ind == MAX_LM:
                            DL_End = True
                        else:
                            DL_End = False

                if event.type == self.py.MOUSEBUTTONDOWN:
                    ##RIGHT SIDE EFFECTS
                    # setting clicked
                    if 650<pos[0]<720 and 6 < pos[1] < 65:
                        self.Settings_page_maker(screen)

                    x_pos_l, x_pos_r = 646, 713
                    y_pos_l, y_pos_r = 75, 112
                    blit_butt_x = 646
                    draw_text_x = 658

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "EDG"

                    y_pos_l = y_pos_r + 25
                    y_pos_r = y_pos_l + 38

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "RED"

                    y_pos_l = y_pos_r + 25
                    y_pos_r = y_pos_l + 38

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "GRE"

                    y_pos_l = y_pos_r + 25
                    y_pos_r = y_pos_l + 38

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "B/W"

                    y_pos_l = y_pos_r + 25
                    y_pos_r = y_pos_l + 38

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "BLU"

                    y_pos_l = y_pos_r + 25
                    y_pos_r = y_pos_l + 38

                    if x_pos_l < pos[0] < x_pos_r and y_pos_l < pos[1] < y_pos_r:
                        opt = "MAG"

                    # Add_text
                    if 663 < pos[0] < 705 and 433 < pos[1] < 468:
                        ARGS = self.Add_text_window(screen)


                    ##TOP EFFECTS
                    #undo
                    if 16 < pos[0] < 60 and 11 < pos[1] < 48:
                        if len(Event_STACK_M) == 0:
                            current_Mask = None
                        else:
                            if len(Event_STACK_M) > 1:
                                temp = Event_STACK_M.pop()
                                store.append(temp)
                    #redo
                    if 86 < pos[0] < 131 and 11 < pos[1] < 48:
                        if len(store) != 0:
                            temp = store.pop()
                            Event_STACK_M.append(temp)
                    #org
                    if 521 < pos[0] < 564 and 12 < pos[1] < 52:
                        opt = "ORG"
                        current_Mask = None

                    #export
                    if 585 < pos[0] < 621 and 6 < pos[1] < 52:
                        self.clock.tick(3)
                        if self.cam_End == True:
                            self.End_page_window(screen, frame, current_Mask, face_coords, ARGS)
                            self.clock.tick(10)
                            camera = self.cv.VideoCapture(0)
                            Display_drone = None
                            self.cam_End = False

                    ##DOWN EFFECTS
                    #print("I am index",ind)
                    if 5 < pos[0] < 38 and 424 < pos[1] < 477:
                        if not DR_End and ind > 0:
                            ind -= 1
                        if ind == 0:
                            DR_End = True
                        else:
                            DR_End = False

                    if 603 < pos[0] < 632 and 424 < pos[1] < 477:
                        if not DL_End and ind < MAX_LM:
                            ind += 1
                            DR_End = False
                        if ind == MAX_LM:
                            DL_End = True
                        else:
                            DL_End = False

                    if 70 < pos[0] < 116 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '0'
                        Event_STACK_M.append(current_Mask)

                    if 151 < pos[0] < 199 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '1'
                        Event_STACK_M.append(current_Mask)

                    if 230 < pos[0] < 278 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '2'
                        Event_STACK_M.append(current_Mask)

                    if 376 < pos[0] < 420 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '3'
                        Event_STACK_M.append(current_Mask)

                    if 458 < pos[0] < 500 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '4'
                        Event_STACK_M.append(current_Mask)

                    if 538 < pos[0] < 585 and 426 < pos[1] < 474:
                        current_Mask = LET[ind] + '5'
                        Event_STACK_M.append(current_Mask)

                    ##capture
                    if 304 < pos[0] < 351 and 428 < pos[1] < 475:
                        self.cam_End = True
                        Display_drone = [(299, 369), (575, 50)]
                        X_dr, Y_dr = Display_drone[0]
                        camera.release()

            self.py.display.update()
            self.clock.tick(1)
        print("App ended")

class Main():
    def proceed(self):
        ft =Face_Transform()
        ft.app_main()

if __name__ == "__main__":
    obj = Main()
    obj.proceed()
