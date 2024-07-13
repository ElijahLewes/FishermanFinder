
import sys
# Includes commands for operating system

import random
# Generates pseudo-random numbers

import itertools
# Looping

import numpy as np
#imports numpy

import cv2 as cv
#imports openCV

#-----------------------------------#

#Map of python cape
MAP_FILE ='cape_python.png'
print("test map")

#Search area constants as squares.
###NOTE: constants all caps
SA1_CORNERS = (130,265, 180, 315) #UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305) #UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105, 205, 155, 255) #UL-X, UL-Y, LR-X, LR-Y)

class Search:
    
    def __init__(self, name):
        self.name = name
        self.img = cv.inread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE), file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = [0,0] #A local coordinate relative to each search area

        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3],
                            SA1_CORNERS[0] : SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3],
                            SA2_CORNERS[0] : SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3],
                            SA3_CORNERS[0] : SA3_CORNERS[2]]


        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0



# create the map class
def draw_map(self, last_known):
    # Display basemap with scale, last known xy location, search areas.
    cv.line(self.img, (20,370), (70, 370), (0,0, 0), 2)
    cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))
    cv.putText(self.img, '50 Nautical Miles', (71, 370), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

    cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]), (SA2_CORNERS[2], SA2_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)
    
    cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]), (SA3_CORNERS[2], SA3_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv.putText(self.img, '+ = Last Known Position', (274, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv.putText(self.img, '* = Actual Position', (275, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))

    cv.imshow('Search Area', self.img)
    cv.moveWindow('Search Area', 750, 10)
    cv.waitKey(500)


#Display base map with last known xy locations, scale, and search areas.
def draw_map(self, last_known):
    #draw scale bar
    cv.line(self.img, (20,370), (70,370), (0,0,0), 2)
    cv.putText(self.img, '0', (8,370), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))
    cv.putText(self.img, '50 Nautical Miles', (71,370), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

    #Add seach areas

    cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]),(SA1_CORNERS[2], SA1_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1]) + 15, cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]),(SA2_CORNERS[2], SA2_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1]) + 15, cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]),(SA3_CORNERS[2], SA3_CORNERS[3]), (0,0,0), 1)
    cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1]) + 15, cv.FONT_HERSHEY_PLAIN, 1, 0)


    #Add key
    cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv.putText(self.img, '+ = Last Known Position', (274, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv.putText(self.img, '* = Actual Position', (275, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))

    cv.imshow('Search Area', self.img)
    cv.moveWindow('Search Area', 750, 10)
    #milisecond delay between rendering map and game menu
    cv.waitKey(500)

x = []
y = []

#Return actual x y location of missubg sailor
def sailor_final_location(self, num_search_areas):
# Find sailor coordinates relative to any Search Area subarry
    self.sailor_actual[0] = np.random.choice(self.sa1.shape[1], 1)
    self.sailor_actual[1] = np.random.choice(self.sa1.shape[0], 1)

    area = int(random.triangular(1, num_search_areas + 1))

    if area == 1:
        x == self.sailor_actual[0] + SA1_CORNERS[0]
        y == self.sailor_actual[1] + SA1_CORNERS[1]

    elif area == 2: 
        x == self.sailor_actual[0] + SA2_CORNERS[0]
        y == self.sailor_actual[1] + SA2_CORNERS[1]
    
    elif area == 3:
        x == self.sailor_actual[0] + SA3_CORNERS[0]
        y == self.sailor_actual[1] + SA3_CORNERS[1]
    
    return x, y


#Set range of search effectiveness possible per area
def calc_search_effectiveness(self):
    self.sep1 = random.uniform(0.2, 0.9)
    self.sep2 = random.uniform(0.2, 0.9)
    self.sep3 = random.uniform(0.2, 0.9)


#Return search results and list searched coordinates
#-----> How to update this list with second search?
def conduct_search(self, area_num, area_array, effectivness_prob):
    local_y_range = range(area_array.shape[0])
    local_x_range = range(area_array.sahpe[1])
    coords = list(itertools.product(local_x_range, local_y_range))
    random.shuffle(coords)
    coords = coords[:int((len(coords) * effectivness_prob))]
    loc_actual = (self.sailor_actual[0], self.sailor_actual[1])
    if area_num == self.area_actual and loc_actual in coords: 
        return 'Found in Area {}.'.format(area_num), coords
    else:
        return 'Not Found', coords 

#Update area target probabilities based on search effectiveness
def revise_target_probs(self):
    denom = self.p1 * (1 - self.sep1) + self.p2 * (1 - self.sep2) /+ self.p3 * (1 - self.sep3)
    self.p1 = self.p1 * (1 - self.sep1) / denom
    self.p2 = self.p2 * (1 - self.sep2) / denom
    self.p3 = self.p3 * (1 - self.sep3) / denom

def draw_menu(search_num):
    print('\nSearch {}',format(search_num))
    print(
    """Choose next areas to search:
0 - Quit
1 - Search Area 1 twice
2 - Search Area 2 twice
3 - Search Area 3 twice
4 - Search Areas 1 & 2
5 - Search Areas 1 & 3
6 - Search Areas 2 & 3
7 - Start Over
"""
    )

def main ():
    print("Start program output")
    app = Search('Cape_Python')
    app.draw_map(last_known=(160, 290))
    sailor_x, sailor_y = app.sailor_final_location(num_search_areas=3)
    print("-" * 65)
    print("\nInitial Target (P) Probabilities:")
    print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))
    search_num = 1

    #Game play while loop
    
    while True:
        app.calc_search_effectiveness()
        draw_menu(search_num)
        choice = input("Choice: ")

        if choice == "0":
            sys.exit()

        elif choice == "1":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(1, app.sa1, app.sep1)
            app.sep1 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.sep2 = 0
            app.sep3 =0

        elif choice == "2":
            results_1, coordss_1 = app.conduct_search(2, app.sa2, app.sep1)
            results_2, coordss_2 = app.conduct_search(2, app.sa2, app.sep1)
            app.sep1 = 0
            app.sep2 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.sep3 =0

        elif choice == "3":
            results_1, coordss_1 = app.conduct_search(3, app.sa1, app.sep1)
            results_2, coordss_2 = app.conduct_search(3, app.sa1, app.sep1)
            app.sep1 =0
            app.sep2 = 0
            app.sep3 =(len(set(coords_1 + coords_2))) / (len(app.sa1)**2)

        elif choice == "4":
            results_1, coordss_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coordss_2 = app.conduct_search(2, app.sa1, app.sep1)
            app.sep3 =0

        elif choice == "5":
            results_1, coordss_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coordss_2 = app.conduct_search(1, app.sa1, app.sep1)
            app.sep1 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.sep2 = 0
            app.sep3 =0

        elif choice == "6":
            results_1, coordss_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coordss_2 = app.conduct_search(3, app.sa1, app.sep1)
            app.sep2 = 0

        elif choice == "7":
            main()

        else:
            print("\nSorry, but that isn't a valid choice.", file=sys.stderr)
            continue

        #Bayes rule for updated target probabilities
        app.revise_target_probs()

        print("\nSearch {} Results 1 = {}".format(search_num, results_1), file=sys.stderr)
        print("Search {} Results 2 = {}\n".format(search_num, results_2), file=sys.stderr)
        print("Search {} Effectiveness (E):".format(search_num))
        print("E1 = {:.3f}, E2 = {:.3f}, P3 = {:.3f}".format(app.sep1, app.sep2, app.sep3))

        if results_1 == 'Not Found' and results_2 == 'Not Found':
            print("\nNew Target Probabilities (P) for Search {}:".format(search_num + 1))
            print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))

        else:
            cv.circle(app.img, (sailor_x, sailor_y), 3, (255, 0, 0), -1)
            cv.imshow('Search Area', app.img)
            cv.waitKey(1500)
            main()
        search_num += 1
    if __name__ == '__main__':
        main()
