

from __future__ import division
import numpy as np
import json
import math



def getScore(year, data):
    sc = 0
    for s in data:
    #Find the total score
        if (s["Year"] == year):
            sc += s["Score"]
    return sc
        
def getSeason(year, array, score, data):
    fg = fga = threep = threepa = twop = twopa = ft = fta = orb = drb = ast = stl = blk = tov = pf = pts = 0
    for dpoints in data:
        if (dpoints["Year"] == year):
            fg += dpoints["FG"]*(dpoints["Score"]/score)
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

    with open('JEmbiid/JEmbiid.json') as data_file:
        data = json.load(data_file)
        scoe = 0
        year = 1
        while (year <= seasons):
            score = getScore(year, data)
            player[year-1] = getSeason(year, array, score, data)
            year += 1
    printStats(player, seasons, "Joel Embiid")   
    np.savetxt('sample.csv', player, delimiter = ",")
    
main()
        
    
