vidov = int(input())
max1 = 0
max2 = 0
max3 = 0
for k in range(vidov):
    vid = input()
    cvetov = int(input())
    if cvetov > max1:
        max1 = cvetov
        vid1 = vid
    elif cvetov < max1:
        if cvetov > max2:
            max2 = cvetov
            vid2 = vid
        elif cvetov < max2:
            if cvetov > max3:
                max3 = cvetov
                vid3 = vid
print(vid1)
print(vid2)
print(vid3)


