import os

SPFilePath = "C:\\Users\\anubhav\\Desktop\\X-Plane 11\Custom Scenery\\scenery_packs.ini"
OverlaysPath = "D:\Ortho4XP\yOrtho4XP_Overlays\Earth nav data"

scenery_packs = open(SPFilePath,'r')
entries = scenery_packs.readlines()


def findOrthoentries (ent):
    ortho_ref = "zOrtho4XP_"
    ortho_entries =[]
    for i in range (0,len(ent)-1):
        if ent[i].find(ortho_ref) > 0:
            start = ent[i].find(ortho_ref)+10
            end = start+7
            ortho_entries.append(ent[i][start:end])
    print("{} number of tiles found in Scenery Packs".format(len(ortho_entries)))
    return ortho_entries

def findOverlays(op):
    Overlays_list=[]
    for root, dirs, files in os.walk(op):
        for name in files:
            Overlays_list.append(name[0:7])
    print("{} number of DSF found in Overlays folder".format(len(Overlays_list)))
    return Overlays_list


def checkOrthos(tiles,overlays):

    if sorted(tiles) == sorted(overlays):
        print("All tiles have overlays and all overlays have tiles")
    else:
        print ("Oops. Either a tile or overlays is missing. Doing more work....")
        missing_tiles = []
        missing_overlays = []
        for i, t in enumerate(tiles):
            if t not in overlays:
                missing_overlays.append(t)
        for j, o in enumerate(overlays):
            if o not in tiles:
                missing_tiles.append(o)
        if not missing_tiles:
            print ("There are no missing tiles")
        else:
            print ("Here are the missing tiles:")
            dmt = "\n".join(missing_tiles)
            print(dmt)
        if not missing_overlays:
            print("There are no missing overlays")
        else:
            print("Here are the missing overlays:")
            dmo = "\n".join(missing_overlays)
            print(dmo)


oe = findOrthoentries(entries)
ol = findOverlays(OverlaysPath)
checkOrthos(oe,ol)

input("Press Enter to Exit....")







