# Mr. Perfectly Fine
for _ in range(int(input())):
    vict = {"left":10**6, "right":10**6, "two":10**6}
    for _ in range(int(input())):
        minu, aq_skill = input().split()
        if aq_skill[0] == "1" and aq_skill[1] == "1":
            vict["two"] = int(minu) if vict["two"] > int(minu) else vict["two"]
        if aq_skill[0] == "1":
            vict["left"] = int(minu) if vict["left"] > int(minu) else vict["left"]
        elif aq_skill[1] == "1":
            vict["right"] = int(minu) if vict["right"] > int(minu) else vict["right"]
 
    if vict["two"]!=10**6 and vict["two"] < (vict["left"]+vict["right"]):
        print(vict["two"])
    else:
        print(vict["left"]+vict["right"]) if (vict["left"]+vict["right"]) < 10**6 else print(-1)