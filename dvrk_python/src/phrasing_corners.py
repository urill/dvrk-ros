from robot import *
from copy import deepcopy
import time
import math
import PyKDL



def dictionary(robotName):
    r=robot(robotName)
    dict = {}
    dict[' '] = [('u'),('d')]
    dict['test2'] = [('r',90,60),('r',180,60),('r',270,60),('r',0,60)]

    dict['a'] = [('d'),('r',80,60),('r',0,10),('r',280,30),('r',180,20),('r',0,20),('r',280,30)]
    dict['b'] = [('d'),('r',90,60),('r',350,30),('r',270,20),('r',190,30),('r',350,40),('r',270,23),('r',180,40)] 
    dict['c'] = [('r',0,35),('d'),('r',180,30),('r',108.43,15.8114),('r',90,30),('r',71.57,15.8114),('r',0,30)]
    dict['d'] = [('d'),('r',90,60),('r',340,30),('r',270,40),('r',200,30)]
    dict['e'] = [('r',0,40),('d'),('r',180,40),('r',90,30),('r',0,30),('r',180,30),('r',90,30),('r',0,40)]
    dict['f'] = [('d'),('r',90,30),('r',0,30),('r',180,30),('r',90,30),('r',0,40)]
    dict['g'] = [('r',0,40),('r',90,35),('r',180,12),('d'),('r',0,12),('r',270,35),('r',180,40),('r',90,60),('r',0,40)]
    dict['h'] = [('d'),('r',90,60),('r',270,30),('r',0,40),('r',90,30),('r',270,60)]
    dict['i'] = [('d'),('r',0,40),('r',180,20),('r',90,60),('r',180,20),('r',0,40)]
    dict['j'] = [('r',90,16),('d'),('r',306.86,15),('r',0,12),('r',36.86,15),('r',90,40),('r',180,12),('r',0,24)]
    dict['k'] = [('d'),('r',90,60),('r',270,30),('r',45,40),('r',225,40),('r',315,40)]
    dict['l'] = [('d'),('r',90,60),('r',270,60),('r',0,40)]
    dict['m'] = [('d'),('r',90,60),('r',288.44,63),('r',71.56,63),('r',270,60)]
    dict['n'] = [('d'),('r',90,60),('r',303.69,72),('r',90,60)]
    dict['o'] = [('r',0,40),('d'),('r',180,40),('r',90,60),('r',0,40),('r',270,60)]
    dict['p'] = [('d'),('r',90,60),('r',0,40),('r',270,30),('r',180,40)]
    dict['q'] = [('r',0,40),('d'),('r',180,40),('r',90,60),('r',0,40),('r',270,60),('r',135,12),('r',315,24)]
    dict['r'] = [('d'),('r',90,60),('r',0,40),('r',270,30),('r',180,40),('r',315,45)]
    dict['s'] = [('d'),('r',0,40),('r',90,30),('r',180,40),('r',90,30),('r',0,40)]
    dict['t'] = [('r',0,20),('d'),('r',90,60),('r',180,20),('r',0,40)]
    dict['u'] = [('r',90,60),('d'),('r',270,60),('r',0,40),('r',90,60)]
    dict['v'] = [('r',0,20),('d'),('r',108.44,63),('r',288.44,63),('r',71.56,63)]
    dict['w'] = [('r',90,60),('d'),('r',270,60),('r',0,20),('r',90,40),('r',270,40),('r',0,20),('r',90,60)]
    dict['x'] = [('d'),('r',56.31,72),('r',236.31,36),('r',123.69,36),('r',303.69,72)]
    dict['y'] = [('r',0,20),('d'),('r',90,30),('r',56.31,36),('r',236.31,36),('r',123.69,36)]
    dict['z'] = [('r',56.31,72),('r',180,40),('d'),('r',0,40),('r',236.31,72),('r',0,40)]
    dict['?'] = [('r',0,20),('d'),('u'),('r',90,10),('d'),('r',90,25),('r',0,20),('r',90,25),('r',180,40)] 


    calibration_or_nah = raw_input('do you need to calibrate?(y or n) ')
    if calibration_or_nah == 'y':
        raw_input('Move the arm to the top left of your paper (press enter to continue)')
        topleft = r.get_desired_cartesian_position().p
        print topleft
        top_left = deepcopy(topleft)
        print top_left
        print " "
        raw_input('Move the arm to the top right of your paper (press enter to continue)')
        topright = r.get_desired_cartesian_position().p
        print topright
        top_right = deepcopy(topright)
        print top_right
        print " "
        raw_input('Move the arm to the bottom left of your paper (press enter to continue)')
        bottomleft = r.get_desired_cartesian_position().p
        print bottomleft
        bottom_left = deepcopy(bottomleft)
        print bottom_left
        print " "
    elif calibration_or_nah == 'n':
        print "enter coordinates in an x y z format without commas"
        top_left = raw_input('please enter the coordinates for the top left point: ')
        top_left = top_left.split()
        for i in range (0,3):
            top_left[i] = float(top_left[i])
        #top_left = tuple(top_left)
        top_left = PyKDL.Vector(top_left[0], top_left[1], top_left[2])
        print top_left
        print " "
        top_right = raw_input('please enter the coordinates for the top right point: ')
        top_right = top_right.split()
        for i in range (0,3):
            top_right[i] = float(top_right[i])
        #top_right = tuple(top_right)
        top_right = PyKDL.Vector(top_right[0], top_right[1], top_right[2])
        print top_right
        print " "
        bottom_left = raw_input('please enter the coordinates for the bottom left point: ')
        bottom_left = bottom_left.split()
        for i in range (0,3):
            bottom_left[i] = float(bottom_left[i])
        #bottom_left = tuple(bottom_left)
        bottom_left = PyKDL.Vector(bottom_left[0],bottom_left[1],bottom_left[2])
        print bottom_left
        print " "
    else:
        print "invalid input"

    length_of_paper = (((top_left.x() - top_right.x())**2) + ((top_left.y() - top_right.y())**2)) ** 0.5
    width_of_paper = (((top_left.x() - bottom_left.x())**2) + ((top_left.y() - bottom_left.y())**2)) ** 0.5    
    
    print top_left
    print top_right
    center_page_x = (top_left.x() + top_right.x())/2.0
    center_page_y = (top_left.y() + bottom_left.y())/2.0
    print center_page_x
    print center_page_y
    time.sleep(1.0)
    raw_input('Press enter to move to middle')
    print r.get_desired_cartesian_position()
    r.delta_move_cartesian([0.0,0.0,0.040])
    time.sleep(1.0)
    print r.get_desired_cartesian_position()
    r.move_cartesian([center_page_x,center_page_y,bottom_left.z()+0.040])
    raw_input('Press enter to move z axis')
    print r.get_desired_cartesian_position()
    time.sleep(1.0)
    start_x = top_left.x()
    start_y = top_left.y()-.04
    print start_x
    print start_y
    r.delta_move_cartesian([0.0,0.0, 0.030])
    raw_input('Enter to move to start')
    r.move_cartesian([start_x,start_y,top_left.z()]) 
    rot_1 = Rotation.Identity() #sets to standard rotation
    #rot_1 = Rotation(0.47,0.87,-0.17,0.80,-0.50,-0.34,-0.38,0.02,-0.92)
    r.move_cartesian_rotation(rot_1)
    letter_number = 0 #used to keep the letters spaced out evenly
    word_number = 0   #used to keep the words spaced out evenly
    line_number = 0   #used to keep the lines spaced out evenly

    cycle_number = 0 #counts the position in the list of actions to create a letter
    phrase_cycle = 0 #counts the position in the list of letters
    word_count = 0   #counts the position in the list of words
    line_count = 0   #counts the position in the list of lines




    time.sleep(2.0)
    phrase = raw_input('enter the words you would like writen: ').lower()
    phrase = phrase.split()

    list_of_words = [] #formats user input as a list of words where each word is a list
    for i in range(0, len(phrase)):
        n = list(phrase[i])
        list_of_words.append(n)

    print list_of_words

    counter_characters = 0 #checks number of characters per line
    draw_list = [] #list of words per line
    word = [] #list of characters in word per line
    for i in range (0,len(list_of_words)): #formats the words into lines of text
       
        word_length = len(list_of_words[i])
        if counter_characters + word_length <= math.floor(length_of_paper/0.02): #checks to see if the next word will make the line longer than 10 characters
            counter_characters += (word_length + 1) #if it isn't longer, it will add that word to the line
            word.append(list_of_words[i])

            if i == len(list_of_words)-1:
                   draw_list.append(word)      
        else:
            draw_list.append(word) #if line is longer than 10 characters, it will add the whole line of words, minus the new, to draw_list
            word = [] #then it will set the next line to have no words in it, and add the new word to that next line
            counter_characters = len(list_of_words[i])+1
            word.append(list_of_words[i])
            if i == len(list_of_words)-1:
                   draw_list.append(word)  
        
    
    print length_of_paper
    print width_of_paper               
    print draw_list
    
    time.sleep(10)

    for line_count in range (0,int(math.floor(width_of_paper/0.02))):


        for word_count in range (0,len(draw_list[line_count])):

            length_of_word = len(draw_list[line_count][word_count])

            for phrase_cycle in range (0, length_of_word):
                length_of_letter_list = len(dict[draw_list[line_count][word_count][phrase_cycle]])  
               
                print draw_list[line_count][word_count][phrase_cycle]


                r.delta_move_cartesian([0.0,0.0,0.01])
                r.move_cartesian_translation([start_x+letter_number+word_number,start_y+line_number,top_left.z()]) #before writing another letter, the robot moves to the next letter, word, or line's starting position

                for cycle_number in range (0, length_of_letter_list): 
                    if dict[draw_list[line_count][word_count][phrase_cycle]][cycle_number][0] == 'r':        # ('r',angle,distance)
                        angle = math.radians(dict[draw_list[line_count][word_count][phrase_cycle]][cycle_number][1])
                        length = (dict[draw_list[line_count][word_count][phrase_cycle]][cycle_number][2])/2500.0

                   
                        x_position = math.cos(angle)*length
                        y_position = math.sin(angle)*length

                        r.delta_move_cartesian([x_position,y_position,0.0])
                      

                    elif dict[draw_list[line_count][word_count][phrase_cycle]][cycle_number] == 'u':         #u = pen up
                        r.delta_move_cartesian([0.0,0.0,0.01])
                    elif dict[draw_list[line_count][word_count][phrase_cycle]][cycle_number] == 'd':         #d = pen down
                        r.delta_move_cartesian([0.0,0.0,-0.01])


                letter_number += .02
            word_number += .02
        letter_number = 0
        word_number = 0
        line_number -= .04
        r.delta_move_cartesian([0.0,0.0,0.03])



if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print sys.argv[0] + ' requires one argument, i.e. name of dVRK arm'
    else:
        dictionary(sys.argv[1])
