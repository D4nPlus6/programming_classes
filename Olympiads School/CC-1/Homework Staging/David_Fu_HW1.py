fieldDims = []
fieldSpecs = []
nuclearPayloads = []
for i in iter(int, 1):
    n,m = map(int, input().split(' '))
    if (n == 0 and m == 0):
        break

    fieldDims.append([n,m])

    tmp = []
    enrichedUraniumCapsule = []
    for j in range(n):
        tmpInput = input()
        tmp.append(tmpInput)
        if '*' in tmpInput:
            for o in range(len(tmpInput)):
                if tmpInput[o] == '*':
                    enrichedUraniumCapsule.append([j,o])
                
    fieldSpecs.append(tmp)
    nuclearPayloads.append(enrichedUraniumCapsule)


# stagingFields = [[[0]*i[1]]*i[0] for i in fieldDims]
stagingFields = [[[0]*fieldDims[i][1] for j in range(fieldDims[i][0])] for i in range(len(fieldDims))]

# stagingFields = [[[[0 for _ in range(i[1])] for _ in range(i[0])]] for i in fieldDims]


print('\n\n---------------Debug Zone:----------------\n')
print("Field dims:",fieldDims,';\n')
print('Field specs:',fieldSpecs,';\n')
print('Nuclear payloads:',nuclearPayloads,';\n')
print('Staging fields:',stagingFields,';\n')
print('\n-------------------------------------------\n\n')



def addOneAroundMine(stagingField,mineY,mineX):
    sF = stagingField

    directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
    for d in directions:
        curMineY = mineY+d[0]
        curMineX = mineX+d[1]
        if curMineY < 0 or curMineX < 0 or curMineY > len(stagingField)-1 or curMineX > len(stagingField[0])-1 or sF[curMineY][curMineX] == '*':
            continue
        print(f"[Debugging] Currently at [{curMineY},{curMineX}] (array is {sF})")
        sF[curMineY][curMineX] += 1
        print(f"[Debugging] Added one to [{curMineY},{curMineX}] (array is now {sF})")


for i in range(len(stagingFields)):
    for j in nuclearPayloads[i]:
        mineY = j[0]
        mineX = j[1]
        addOneAroundMine(stagingFields[i],mineY,mineX)
        stagingFields[i][mineY][mineX] = '*'

for i in range(len(stagingFields)):
    print(f"Field #{i+1}:")
    for j in range(len(stagingFields[i])):
        print(''.join(map(str, stagingFields[i][j])))
    try:
        if stagingFields[i+1]:
            print()
    except:
        pass


# note: i just finished this in summerschool, too lazy to optimize this rn
# note1: just realized there are quite a few area above line 40 that can be optimized to reduce memory usage
# note2: screw memory usage, sacrifices must be made; as long as cpu usage is low it's good
# note3: might be a good idea to make a private github repo just for this class, cuz I've been rewriting so frequently and vs code's ctrl+z isn't all-powerful
