# City-building strategy game - Simp City
# Created by: Armirola Roseller III Tumolva - S10223630K

''' #Display Menu# '''

def main_menu():
    print('Welcome, mayor of Simp City!')
    print('----------------------------')
    print('1. Start new game')
    print('2. Load saved game')
    print('3. Show high scores')
    print('\n0. Exit')

    menu_option = True
    while menu_option == True:
        menu_choice = int(input('Your choice? '))

        #Start new game / Load saved game
        if (menu_choice == 1) or (menu_choice == 2):
            gameplay(menu_choice)
        #Show high scores
        elif menu_choice == 3:
            high_score_file = open('highscores.csv')
            high_score_list = []

            #Transfer from .csv file to list
            for row in high_score_file:
                row = row.split(',')
                if row[0] != 'Rank':
                    high_score_list.append(list(row))

            high_score_file.close()

            #Print rankings
            print('\n--------- HIGH SCORES ---------')
            print('Pos Player                Score')
            print('--- ------                -----')
            for row in high_score_list:
                print('{:>2s}. {:25s}{:>2s}'.format(row[0],row[1],row[2][:-1]))
            print('-------------------------------\n')

            main_menu()
        #Exit game
        elif menu_choice == 0:
            quit()
        #If user input is not as expected
        else:
            menu_option = True


''' #Start Game# '''

def gameplay(menu_choice):
    #NEW GAME / SAVED GAME
    while True:
        if menu_choice == 1:
            #New data overrides saved data
            #Overwriting remaining buildings
            file = open("data.csv",'w')
            data = 'BCH:8\nFAC:8\nHSE:8\nSHP:8\nHWY:8\n'
            data_dict = {'BCH':8,'FAC':8,'HSE':8,'SHP':8,'HWY':8} #Does not change unless including more buildings
            file.write(data)
            file.close()

            #Overwriting position
            file = open('posdata.csv','w')
            placement_list = '   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n   \n'
            file.write(placement_list)
            file.close()

            #Overwriting turns
            file = open('turnsdata.csv','w')
            turns = '1'
            file.write(turns)
            file.close
            turns = int(turns)

            placement_list = [['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ']]
            break
        if menu_choice == 2:
            #Does not change unless including more buildings
            building_list = ['BCH','FAC','HSE','SHP','HWY']
            data_list = ['','','','','']
            building_dict = {1: 'BCH', 2: 'FAC', 3: 'HSE', 4: 'SHP', 5: 'HWY'}
            placement_list = [['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ']]

            data_dict = {'BCH':8,'FAC':8,'HSE':8,'SHP':8,'HWY':8} #Changes depending on saved game

            try:
                #Saved data is read (number of buildings left)
                file = open("data.csv",'r')

                for z in range(5):
                    for line in file:
                        data_list[z] = line
                        break
                data = ''.join(data_list)

                file.close()
                #Updating number of buildings from saved game into data dictionary
                n = 4
                for building in building_list:
                    number = data[n]
                    try:
                        data_dict[building] = int(number)
                    except ValueError:
                        data_dict[building] = 0
                    n += 6

                #Saved data is read (position of buildings)
                n = 0
                posdata = []
                file = open('posdata.csv','r')

                for line in file:
                    posdata.append(line[:-1])

                for list in placement_list:
                    for i in range(4):
                        list[i] = posdata[n]
                        n += 1

                file.close()

                #Saved data is read (turns left)
                turns = 1
                file = open('turnsdata.csv','r')
                for line in file:
                    turns = int(line)

                file.close()
            except FileNotFoundError:
                print('No saved game found!\n')
                main_menu()

            break

    #Placement variables, score variable and turn variable
    import random
    position_list = [['a1','b1','c1','d1'],['a2','b2','c2','d2'],['a3','b3','c3','d3'],['a4','b4','c4','d4']]
    building_list = ['BCH','FAC','HSE','SHP','HWY']
    building_dict = {1: 'BCH', 2: 'FAC', 3: 'HSE', 4: 'SHP', 5: 'HWY'}
    number1 = random.randint(1, 5)
    number2 = random.randint(1, 5)

    while turns <= 17:
        if turns <= 16:
            print('\nTurn {:<}'.format(turns))

            #Condition if both buildings are unavailable (reshuffle buildings)
            if (data_dict[building_dict[number1]] == 0) and (data_dict[building_dict[number2]] == 0):
                number1 = random.randint(1, 5)
                number2 = random.randint(1, 5)

            #4x4 board
            border_row = ['A', 'B', 'C', 'D']
            border_column = ['1', '2', '3', '4']
            no = 0
            no1 = 1

            print('   {:^5s} {:^5s} {:^5s} {:^5s}       {:15s}{:15s}'.format(border_row[0],border_row[1],border_row[2],border_row[3],'Building','Remaining'))
            print('  +-----+-----+-----+-----+      {:15s}{:15s}'.format('--------','---------'))
            for i in range(len(placement_list)):
                print(' {}|'.format(border_column[i]), end='')
                for j in range(len(placement_list[i])):
                    print(' {:^3s} |'.format(placement_list[i][j]), end='')
                
                #ADVANCED REQUIREMENT (Always show buildings remaining)
                try:
                    print('      {:15s}{:<15d}'.format(building_list[no],data_dict[building_list[no]]), end='')
                except IndexError:
                    pass
                else:
                    no += 2

                try:        
                    print('\n  +-----+-----+-----+-----+      {:15s}{:<15d}'.format(building_list[no1],data_dict[building_list[no1]]))
                except IndexError:
                    print('\n  +-----+-----+-----+-----+')
                else:
                    no1 += 2

            # Options
            print('1. Build a {}'.format(building_dict[number1]))
            print('2. Build a {}'.format(building_dict[number2]))
            print('3. See current score\n')
            print('5. Save game')
            print('0. Exit to main menu')

            while True:
                try:
                    game_choice = int(input('Your choice? '))
                except ValueError:
                    pass
                else:
                    if (game_choice == 1) or (game_choice == 2) or (game_choice == 3) or (game_choice == 5) or (game_choice == 0):
                        break

            gameplay_option = True
            while gameplay_option == True:
                #Choice 1 (building)
                if game_choice == 1:
                    placement_cond1 = False
                    placement_cond2 = False
                    placement_cond3 = False
                    placement_cond4 = False
                    mistake = False

                    #Condition if building of option 1 is still available
                    if data_dict[building_dict[number1]] < 1:
                        print('No more existing buildings left')
                        break
                    else:
                        placement = input('Build where? ')
                        
                        #Placement of building
                        for s in range(len(position_list)):
                            for d in range(len(position_list[s])):
                                if placement.lower() == position_list[s][d]:
                                    if turns == 1:
                                        placement_list[s][d] = building_dict[number1]
                                        turns += 1  
                                    else:
                                        if placement_list[s][d] != '   ':
                                            print('You cannot build on an existing building.')
                                            mistake = True
                                        else:
                                            try:
                                                if placement_list[s-1][d] == '   ':
                                                    placement_cond1 = True
                                                else:
                                                    placement_cond1 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s+1][d] == '   ':
                                                    placement_cond2 = True
                                                else:
                                                    placement_cond2 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s][d-1] == '   ':
                                                    placement_cond3 = True
                                                else:
                                                    placement_cond3 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s][d+1] == '   ':
                                                    placement_cond4 = True
                                                else:
                                                    placement_cond4 = False
                                            except IndexError:
                                                pass

                                            #Condition compiler

                                            #Middle (4 conditions)
                                            if (placement == 'b2') or (placement == 'c2') or (placement == 'b3') or (placement == 'c3'):
                                                if (placement_cond1 == True) and (placement_cond2 == True) and (placement_cond3 == True) and (placement_cond4 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Upper left corner (2 conditions)
                                            elif (placement == 'a1'):
                                                if (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Upper right corner (2 conditions)
                                            elif (placement == 'a4'):
                                                if (placement_cond3 == True) and (placement_cond2 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Lower left corner (2 conditions)
                                            elif (placement == 'd1'):
                                                if (placement_cond1 == True) and (placement_cond4 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Lower right corner (2 conditions)
                                            elif (placement == 'd4'):
                                                if (placement_cond1 == True) and (placement_cond3 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Left side (3 conditions)
                                            elif (placement == 'a2') or (placement == 'a3'):
                                                if (placement_cond1 == True) and (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Right side (3 conditions)
                                            elif (placement == 'd2') or (placement == 'd3'):
                                                if (placement_cond1 == True) and (placement_cond3 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Upper side (3 conditions)
                                            elif (placement == 'b1') or (placement == 'c1'):
                                                if (placement_cond3 == True) and (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1
                                            #Lower side (3 conditions)
                                            elif (placement == 'b4') or (placement == 'c4'):
                                                if (placement_cond1 == True) and (placement_cond4 == True) and (placement_cond3 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number1]
                                                    turns += 1

                                    #Removal of no. of buildings and applying score addition
                                    if mistake == False:
                                        data_dict[building_dict[number1]] -= 1
                                        data_dict[building_dict[number2]] -= 1
                                        number1 = random.randint(1, 5)
                                        number2 = random.randint(1, 5)                                    

                                    break

                    break
                elif game_choice == 2: #Choice 2 (building)
                    placement_cond1 = False
                    placement_cond2 = False
                    placement_cond3 = False
                    placement_cond4 = False
                    mistake = False

                    #Condition if building of option 2 is still available
                    if data_dict[building_dict[number2]] < 1:
                        print('No more existing buildings left')
                        break
                    else:
                        placement = input('Build where? ')
                        
                        #Placement of building
                        for s in range(len(position_list)):
                            for d in range(len(position_list[s])):
                                if placement.lower() == position_list[s][d]:
                                    if turns == 1:
                                        placement_list[s][d] = building_dict[number2]
                                        turns += 1  
                                    else:
                                        if placement_list[s][d] != '   ':
                                            print('You cannot build on an existing building.')
                                            mistake = True
                                        else:
                                            try:
                                                if placement_list[s-1][d] == '   ':
                                                    placement_cond1 = True
                                                else:
                                                    placement_cond1 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s+1][d] == '   ':
                                                    placement_cond2 = True
                                                else:
                                                    placement_cond2 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s][d-1] == '   ':
                                                    placement_cond3 = True
                                                else:
                                                    placement_cond3 = False
                                            except IndexError:
                                                pass

                                            try:
                                                if placement_list[s][d+1] == '   ':
                                                    placement_cond4 = True
                                                else:
                                                    placement_cond4 = False
                                            except IndexError:
                                                pass

                                            #Condition compiler

                                            #Middle (4 conditions)
                                            if (placement == 'b2') or (placement == 'c2') or (placement == 'b3') or (placement == 'c3'):
                                                if (placement_cond1 == True) and (placement_cond2 == True) and (placement_cond3 == True) and (placement_cond4 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Upper left corner (2 conditions)
                                            elif (placement == 'a1'):
                                                if (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Upper right corner (2 conditions)
                                            elif (placement == 'a4'):
                                                if (placement_cond3 == True) and (placement_cond2 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Lower left corner (2 conditions)
                                            elif (placement == 'd1'):
                                                if (placement_cond1 == True) and (placement_cond4 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Lower right corner (2 conditions)
                                            elif (placement == 'd4'):
                                                if (placement_cond1 == True) and (placement_cond3 == True):
                                                    print('You must build next to an existing building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Left side (3 conditions)
                                            elif (placement == 'a2') or (placement == 'a3'):
                                                if (placement_cond1 == True) and (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Right side (3 conditions)
                                            elif (placement == 'd2') or (placement == 'd3'):
                                                if (placement_cond1 == True) and (placement_cond3 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Upper side (3 conditions)
                                            elif (placement == 'b1') or (placement == 'c1'):
                                                if (placement_cond3 == True) and (placement_cond4 == True) and (placement_cond2 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1
                                            #Lower side (3 conditions)
                                            elif (placement == 'b4') or (placement == 'c4'):
                                                if (placement_cond1 == True) and (placement_cond4 == True) and (placement_cond3 == True):
                                                    print('You must build next to an exisitng building.')
                                                    mistake = True
                                                else:
                                                    placement_list[s][d] = building_dict[number2]
                                                    turns += 1

                                    #Removal of no. of buildings and applying score addition
                                    if mistake == False:
                                        data_dict[building_dict[number1]] -= 1
                                        data_dict[building_dict[number2]] -= 1
                                        number1 = random.randint(1, 5)
                                        number2 = random.randint(1, 5)    
                    break
                #Choice 4 (see current score)
                elif game_choice == 3:
                    calculate_score(placement_list)
                    break
                #Choice 5 (save game)
                elif game_choice == 5:
                    #Saving remaining buildings
                    #data = 'BCH:8\nFAC:8\nHSE:8\nSHP:8\nHWY:8\n'
                    file = open("data.csv", "w")
                    data = 'BCH:{}\nFAC:{}\nHSE:{}\nSHP:{}\nHWY:{}\n'.format(data_dict['BCH'],data_dict['FAC'],data_dict['HSE'],data_dict['SHP'],data_dict['HWY'])
                    file.write(data)
                    file.close()

                    #Saving position
                    file = open('posdata.csv', 'w')
                    placement_list = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(placement_list[0][0],placement_list[0][1],placement_list[0][2],placement_list[0][3],placement_list[1][0],placement_list[1][1],placement_list[1][2],placement_list[1][3],placement_list[2][0],placement_list[2][1],placement_list[2][2],placement_list[2][3],placement_list[3][0],placement_list[3][1],placement_list[3][2],placement_list[3][3])
                    file.write(placement_list)
                    file.close()

                    #Saving turns
                    file = open('turnsdata.csv','w')
                    turns = str(turns)
                    file.write(turns)
                    file.close()

                    print('\nGame saved!\n')
                    main_menu()
                elif game_choice == 0: #Choice 6 (exit to main menu)
                    print()
                    main_menu()
                    break
                else: #If user imput is not what's provided
                    print('Incorrect input')
                    gameplay_option = True

        else:
            #End game
            print('Final layout of Simp City:')
            print('   {:^5s} {:^5s} {:^5s} {:^5s} '.format(
                border_row[0], border_row[1], border_row[2], border_row[3]))
            print('  +-----+-----+-----+-----+')
            for i in range(len(placement_list)):
                print(' {}|'.format(border_column[i]), end='')
                for j in range(len(placement_list[i])):
                    print(' {:^3s} |'.format(placement_list[i][j]), end='')
                print('\n  +-----+-----+-----+-----+')

            score_total = calculate_score(placement_list)
            high_score(score_total)
            break
            

''' Calculating scores '''

def calculate_score(placement_list):
    hse_score = []
    fac_score = []
    shp_score = []
    hwy_score = []
    bch_score = []
    fac_count = 0
    count = 0

    for y in range(len(placement_list)):
        for x in range(len(placement_list[y])):
            building = placement_list[y][x]
            
            #Checking of building
            if building == '   ':
                continue
            elif building == 'BCH':
                #A Beach (BCH) scores 3 points if it is built in column A or column D, or 1 point otherwise.
                if (x == 0) or (x == 3):
                    bch_score.append(3)
                else:
                    bch_score.append(1)
            elif building == 'FAC':
                #A Factory (FAC) scores 1 point per factory (FAC) in the city, up to a maximum of 4 points for the first 4 factories;
                #all subsequent factories only score 1 point each. For example
                #•	If there are 3 factories in the city, each factory will score 3 points, for a total of 3+3+3 = 9 points. 
                #•	If there are 5 factories in the city, the first 4 factories will score 4 points each while the 5th factory will score 1 point, for a total of 4+4+4+4+1 = 17 points.
                fac_count += 1
                #Factory calc continues outside of the nested for loop

            elif (building == 'HSE') or (building == 'SHP'):
                #If a House (HSE) is next to a factory (FAC), then it scores 1 point only. Otherwise, it scores 1 point for each adjacent house (HSE) or shop (SHP), and 2 points for each adjacent beach (BCH).
                
                #A Shop (SHP) scores 1 point per different type of building adjacent to it.
                adjacent_list = []
                try:
                    adjacent_list.append(placement_list[y-1][x])
                except IndexError:
                    pass

                try:
                    adjacent_list.append(placement_list[y+1][x])
                except IndexError:
                    pass

                try:
                    adjacent_list.append(placement_list[y][x-1])
                except IndexError:
                    pass

                try:
                    adjacent_list.append(placement_list[y][x+1])
                except IndexError:
                    pass
                
                if building == 'HSE':
                    if 'FAC' in adjacent_list:
                        hse_score.append(1)
                    else:
                        for i in adjacent_list:
                            if i == 'BCH':
                                hse_score.append(2)
                            elif (i == 'HSE') or (i == 'SHP'):
                                hse_score.append(1)

                elif building == 'SHP':
                    unique_list = []
                    for i in adjacent_list:
                        if (i not in unique_list) and (i != '   '):
                            unique_list.append(i)

                    #shp_score = the number of unique items in unique_list
                    shp_score.append(len(unique_list))

            elif building == 'HWY':
                #A Highway (HWY) scores 1 point per connected highway (HWY) in the same row (not column).
                left_side = ''
                right_side = ''
                try:
                    right_side = placement_list[y][x+1]
                except IndexError:
                    pass

                try:
                    left_side = placement_list[y][x-1]
                except IndexError:
                    pass

                if 'HWY' == right_side:
                    if 'HWY' == left_side:
                        count += 1
                    else:
                        count += 2
                else:
                    if 'HWY' != left_side:
                        count += 1         

        #Highway calc cont.
        if count != 0:
            hwy_count = count
            for i in range(count):
                hwy_score.append(hwy_count)
            count = 0

    #Factory calc cont.
    if fac_count <= 4:
        for i in range(fac_count):
            fac_score.append(4)
    else:
        fac_score = [4,4,4,4]
        for i in range(fac_count - 4):
            fac_score.append(1)

    #Score printing
    bch_total = 0
    hse_total = 0
    fac_total = 0
    shp_total = 0
    hwy_total = 0

    #Beach
    print('BCH:',end=' ')
    if bch_score:
        #Calc total
        for i in bch_score:
            bch_total += i

        #Print total
        if len(bch_score) != 1:
            for i in range(len(bch_score) -1):
                print('{} +'.format(bch_score[i]),end=' ')
            print('{} = {}'.format(bch_score[-1],bch_total))
        else:
            print('{} = {}'.format(bch_total,bch_total))
    else:
        print('0')

    #House
    print('HSE:',end=' ')
    if hse_score:
        #Calc total
        for i in hse_score:
            hse_total += i

        #Print total
        if len(hse_score) != 1:
            for i in range(len(hse_score) -1):
                print('{} +'.format(hse_score[i]),end=' ')
            print('{} = {}'.format(hse_score[-1],hse_total))
        else:
            print('{} = {}'.format(hse_total,hse_total))
    else:
        print('0')

    #Factory
    print('FAC:',end=' ')
    if fac_score:
        #Calc total
        for i in fac_score:
            fac_total += i

        #Print total
        if len(fac_score) != 1:
            for i in range(len(fac_score) -1):
                print('{} +'.format(fac_score[i]),end=' ')
            print('{} = {}'.format(fac_score[-1],fac_total))
        else:
            print('{} = {}'.format(fac_total,fac_total))
    else:
        print('0')

    #Shop
    print('SHP:',end=' ')
    if shp_score:
        #Calc total
        for i in shp_score:
            shp_total += i

        #Print total
        if len(shp_score) != 1:
            for i in range(len(shp_score) -1):
                print('{} +'.format(shp_score[i]),end=' ')
            print('{} = {}'.format(shp_score[-1],shp_total))
        else:
            print('{} = {}'.format(shp_total,shp_total))
    else:
        print('0')

    #Highway
    print('HWY:',end=' ')
    if hwy_score:
        #Calc total
        for i in hwy_score:
            hwy_total += i

        #Print total
        if len(hwy_score) != 1:
            for i in range(len(hwy_score) -1):
                print('{} +'.format(hwy_score[i]),end=' ')
            print('{} = {}'.format(hwy_score[-1],hwy_total))
        else:
            print('{} = {}'.format(hwy_total,hwy_total))
    else:
        print('0')

    #Total score calc
    score_total = bch_total + hse_total + shp_total + hwy_total + fac_total
    print('Total score: {}'.format(score_total))
    return score_total


''' ADVANCED REQUIREMENT (Display high scores) '''

def high_score(score_total):
    #Opening .csv file and reading to a list
    high_score_file = open('highscores.csv')
    high_score_list = []

    #Transfer from .csv file to list
    for row in high_score_file:
        row = row.split(',')
        high_score_list.append(row)

    high_score_file.close()

    #Checking if user score is eligible for ranking
    points_list = []
    high_score_position = 0
    lowest_score = int(high_score_list[-1][2][:-1])

    if score_total > lowest_score:
        for row in high_score_list:
            point = int(row[2][:-1])
            points_list.append(point)
        points_list.sort(reverse=True)
        
        #Looking for position in high scores list
        for points in points_list:
            if score_total > points:
                high_score_position = points_list.index(points) + 1
                break

        print('Congratulations! You made the high score board at position {}!'.format(high_score_position))
        player_name = input('Please enter your name (max 20 chars): ')

        #Insert high score into high score list
        new_high_score = [str(high_score_position),player_name,'{}\n'.format(score_total)]
        high_score_list.insert(high_score_position - 1,new_high_score)
        high_score_list.remove(high_score_list[-1])


        #Re-ranking (1 to 10)
        high_score_str = high_score_list
        for i in range(len(high_score_list)):
            high_score_str[i][0] = str(i + 1)
            high_score_list[i][0] = str(i + 1)

        #Joining nested list (high_score_list)
        for i in range(len(high_score_list)):
            high_score_list[i] = ','.join(high_score_list[i])
        high_score_list = ''.join(high_score_list)

        #File writing
        high_score_file = open('highscores.csv','w')
        high_score_file.write(high_score_list)
        high_score_file.close()

    else:
        print('Unfortunately, you have not made it to the leaderboard. Try again next time!')

    #Print rankings
    high_score_file = open('highscores.csv')
    high_score_list = []

    #Transfer from .csv file to list
    for row in high_score_file:
        row = row.split(',')
        if row[0] != 'Rank':
            high_score_list.append(list(row))

    high_score_file.close()

    print('\n--------- HIGH SCORES ---------')
    print('Pos Player                Score')
    print('--- ------                -----')
    for row in high_score_list:
        print('{:>2s}. {:25s}{:>2s}'.format(row[0],row[1],row[2][:-1]))
    print('-------------------------------\n')

    main_menu()

main_menu()
gameplay()

''' Remaining Tasks '''
# ADDITIONAL REQUIREMENTS #

# IMPLEMENTED:
# - ALWAYS SHOW BUILDILNGS REMAINING
# - HIGH SCORES
# - PROGRAM VALIDATION

# NOT IMPLEMENTED:
# - MONUMENT
# - PARK
# - OPTIONAL BUILDING POOL
# - OPTIONAL CITY SIZE