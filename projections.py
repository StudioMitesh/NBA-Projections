

from __future__ import division
import numpy as np
import json
import math



def getScore(year, data, pname):
    sc = 0
    for score_find in data:
    #Find the total score
        if (score_find["Year"] == year):
            if (score_find["Player"] == pname):
                sc += score_find["Score"]
    return sc
        
def getSeason(year, array, score, data, pname):
    fg = threep = twop = ft = orb = drb = ast = stl = blk = tov = pf = pts = 0
    fga = twopa = threepa = fta = 1
    for dpoints in data:
        if (dpoints["Year"] == year):
            if (dpoints["Player"] == pname):
                #print year, pname
                fg += float(dpoints["FG"])*(dpoints["Score"]/score)
                fga += dpoints["FGA"]*(dpoints["Score"]/score)
                threep += dpoints["3P"]*(dpoints["Score"]/score)
                threepa += dpoints["3PA"]*(dpoints["Score"]/score)
                twop += dpoints["2P"]*(dpoints["Score"]/score)
                twopa += dpoints["2PA"]*(dpoints["Score"]/score)
                ft += dpoints["FT"]*(dpoints["Score"]/score)
                fta += dpoints["FTA"]*(dpoints["Score"]/score)
                orb += dpoints["ORB"]*(dpoints["Score"]/score)
                drb += dpoints["DRB"]*(dpoints["Score"]/score)
                ast += dpoints["AST"]*(dpoints["Score"]/score)
                stl += dpoints["STL"]*(dpoints["Score"]/score)
                blk += dpoints["BLK"]*(dpoints["Score"]/score)
                tov += dpoints["TOV"]*(dpoints["Score"]/score)
                pf += dpoints["PF"]*(dpoints["Score"]/score)
    ftpc = ft/fta        
    twopc = twop/twopa
    threepc = threep/threepa
    fgpc = fg/fga
    trb = orb + drb
    pts = twop*2+threep*3+ft
    efg = (fg + 0.5*threep)/fga    
    array = ([fg, fga, fgpc, threep, threepa, threepc, twop, twopa, twopc, efg, ft, fta, ftpc, orb, drb, trb, ast, stl, blk, tov, pf, pts])
    return array

def printStats(array, seasons, player):
    print player
    yr = 1
    for i in range(seasons):
        print "Year " + str(yr)
        print str(array[i][21]) + " pts, " + str(array[i][16]) + " asts, " + str(array[i][15]) + " rebs, " + str(array[i][17]) + " stls, " + str(array[i][18]) + " blks"
        yr += 1
            
#for i in range(seasons):
#            for j in range(fields):


def main():
    seasons = 3
    fields = 22
    player = np.zeros((seasons, fields))
    array = np.zeros(fields)
    player_name = ["Dragan Bender", "Kris Dunn", "Buddy Hield", "Jamal Murray",
                  "Marquese Chriss", "Jakob Poeltl", "Thon Maker", "Malcolm Brogdon",
                  "Karl-Anthony Towns", "D'Angelo Russell", "Kristaps Porzingis",
                  "Emmanuel Mudiay", "Stanley Johnson", "Justise Winslow", "Myles Turner",
                  "Devin Booker", "Willy Hernangomez", "Nikola Jokic", "Andrew Wiggins", 
                  "Nikola Mirotic", "Nerlens Noel", "Elfrid Payton", "Jordan Clarkson",
                  "Marcus Smart", "Zach LaVine", "Mario Hezonja", "Jusuf Nurkic", 
                  "Jabari Parker", "Aaron Gordon", "Julius Randle", "Gary Harris", 
                  "Rodney Hood", "Dario Saric", "Dante Exum", "Doug McDermott", "TJ Warren",
                  "Kelly Oubre Jr", "Trey Lyles", "Frank Kaminsky", "Norman Powell", "Juan Hernangomez",
                  "Domantas Sabonis", "Skal Labissiere", "Jahlil Okafor", "Dejounte Murray"]

    with open('players.json') as data_file:
        data = json.load(data_file)
        score = 0
        year = 1
        for pname in player_name:
            while (year <= seasons):
                score = getScore(year, data, pname)
                player[year-1] = getSeason(year, array, score, data, pname)
                year += 1
            year = 1    
            f = open('sample_pl.csv', 'ab')
            np.savetxt(f, player, delimiter = ",")
            #print pname
            printStats(player, 3, pname)
    
main()
        
    
