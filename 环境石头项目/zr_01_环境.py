
while True:
    print("请输入三种成分的比例：")
    clay = float(input("请输入clay的比例：%"))
    sand = float(input("请输入sand的比例：%"))
    silt = float(input("请输入silt的比例：%"))
    if clay + sand + silt == 100 and clay >= 0 and sand >= 0 and silt >= 0:
        print("您输入的操作是clay: %s%% sand: %s%%  silt: %s%%  " % (clay, sand, silt))


        class Wentworth:
            if clay > 90:
                print("Wentworth et al., 1922")
                print("Clay/claystone")

            elif 90 > clay > 50:
                if sand > silt:
                    print("Wentworth et al., 1922")
                    print("Sandy mud/Sandy mudstone")

                else:
                    print("Wentworth et al., 1922")
                    print("Mud/Mudstone")

            elif 50 > clay > 10:

                if sand > silt:
                    print("Wentworth et al., 1922")
                    print("Muddy sand/Muddy sandstone")

                else:
                    print("Wentworth et al., 1922")
                    print("Muddy silt/Muddy siltstone")

            elif clay < 10:

                if sand > silt:
                    print("Wentworth et al., 1922")
                    print("Sand/Sandstone")

                elif silt > sand:
                    print("Wentworth et al., 1922")
                    print("Silt/Siltstone")


        class Robinson:

            if sand > 50:
                print("Robinson, 1949")
                print("Sand/Sandstone" )
            elif silt > 50:
                print("Robinson, 1949")
                print("Silt/Siltstone")
            elif clay > 50:
                print("Robinson, 1949")
                print("Clay/Claystone")
            elif sand < 50 and silt < 50 and clay < 50:
                print("Robinson, 1949")
                print("LOAM(Sand-Silt-Clay)")


        class Trefethen:
            if clay > 80:
                print("Trefethen, 1950")
                print("Clay/Claystone")

            else:

                if clay > sand > silt and silt < 15:
                    print("Trefethen, 1950")
                    print("Sandy clay/Sandy claystone")

                elif clay > sand < silt and sand < 15:
                    print("Trefethen, 1950")
                    print("Silt clay/Silty claystone")

                elif clay > sand > 15 and clay > silt > 15:
                    print("Trefethen, 1950")
                    print("Sandy silty clay/ Sandy silty claystone")

            if sand > 80:
                print("Trefethen, 1950")
                print("Sand/Sandstone")

            else:

                if sand > silt > clay and clay < 15:
                    print("Trefethen, 1950")
                    print("Silty sand/Silty sandstone")

                elif sand > clay > silt and silt < 15:
                    print("Trefethen, 1950")
                    print("Clay sand/Clay sandstone")

                elif sand > clay > 15 and sand > silt > 15:
                    print("Trefethen, 1950")
                    print("Silty clay sand/Silty clay sandstone")

            if silt > 80:
                print("Trefethen, 1950")
                print("Silt/Siltstone")

            else:

                if silt > sand > clay and clay < 15:
                    print("Trefethen, 1950")
                    print("Sandy silt/Sandy siltstone")

                elif silt > clay > sand and sand < 15:
                    print("Trefethen, 1950")
                    print("Clay silt/Clay siltstone")

                elif silt > clay > 15 and silt > sand > 15:
                    print("Trefethen, 1950")
                    print("Sandy clay silt/Sandy clay siltstone")


        class Shepard:
            if sand > 75:
                print("Shepard, 1954")
                print("Sand/Sandstone")

            else:

                if sand > silt > clay and clay < 20:
                    print("Shepard, 1954")
                    print("Silty sand/Silty sandstone")

                elif sand > clay > silt and silt < 20:
                    print("Shepard, 1954")
                    print("Clayey sand/Clayey sandstone")

            if silt > 75:
                print("Shepard, 1954")
                print("Silt/Siltstone")

            else:

                if silt > sand > clay and clay < 20:
                    print("Shepard, 1954")
                    print("Sandy silt/Sandy siltstone")

                elif silt > clay > sand and sand < 20:
                    print("Shepard, 1954")
                    print("Clayey silt/Clay siltstone")

            if clay > 75:
                print("Shepard, 1954")
                print("Clay/claystone")

            else:

                if clay > sand > silt and silt < 20:
                    print("Shepard, 1954")
                    print("Sandy clay/Sandy claystone")

                elif sand < silt and sand < 20:
                    print("Shepard, 1954")
                    print("Silt clay/Silty claystone")

            if 20 < sand < 60 and 20 < silt < 60 and 20 < clay < 60:
                print("Shepard, 1954")
                print("Sand-silt-clay")


        class Joides:
            if clay > 90:
                print("JOIDES, 1974")
                print("Clay/claystone")

            elif 90 > clay > 10:

                if sand > silt:
                    print("JOIDES, 1974")
                    print("Sandy mud/Sandy mudstone")

                else:
                    print("JOIDES, 1974")
                    print("Mud/Mudstone/Shale")

            elif clay < 10:

                if sand > silt:
                    print("JOIDES, 1974")
                    print("Sandstone")

                elif silt > sand:
                    print("JOIDES, 1974")
                    print("Silt/Siltstone")


        class Folk:
            if sand > 50:

                if sand > 90:
                    print("Folk, 1980")
                    print("Sand/Sandstone")
                else:
                    if silt == 0:
                        print("Folk, 1980")
                        print("Clayed sand/Clayed sandstone")
                    else:
                        if clay/silt > 2:
                            print("Folk, 1980")
                            print("Clayed sand/Clayed sandstone")
                        elif 0.5 < clay/silt < 2:
                            print("Folk, 1980")
                            print("Muddy sand/Muddy sandstone")
                        else:
                            print("Folk, 1980")
                            print("Silty sand/Silty sandstone")

            elif 10 < sand < 50:
                if silt == 0:
                    print("Folk, 1980")
                    print("Clayed sand/Clayed sandstone")
                else:
                    if clay / silt > 2:
                        print("Folk, 1980")
                        print("Sandy clay/Sandy claystone")
                    elif 0.5 < clay / silt < 2:
                        print("Folk, 1980")
                        print("Sandy mud/Sandy mudstone")
                    else:
                        print("Folk, 1980")
                        print("Sandy silt/Sandy siltstone")

            else:
                if silt == 0:
                    print("Folk, 1980")
                    print("Clayed sand/Clayed sandstone")
                else:
                    if clay / silt > 2:
                        print("Folk, 1980")
                        print("Clay/Claystone")
                    elif 0.5 < clay / silt < 2:
                        print("Folk, 1980")
                        print("Mud/Mudstone")
                    else:
                        print("Folk, 1980")
                        print("Silt/siltstone")


        class Leg105:
            if sand > 80:
                print("Led 178, 1987")
                print("Sand/sandstone")
            elif sand < 80:

                if sand > silt > 10 and clay < 10:
                    print("Led 178, 1987")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > 10 and silt < 10:
                    print("Led 178, 1987")
                    print("Clayey sand/Clayey sandstone")
                elif sand > silt > 10 and sand > clay > 10:
                    print("Led 178, 1987")
                    print("Muddy sand/Muddy sandstone")

            if silt > 80:
                print("Led 178, 1987")
                print("Silt/siltstone")
            elif silt < 80:

                if silt > clay > 10 and sand < 10:
                    print("Led 178, 1987")
                    print("Clayey silt/Clayey siltstone")
                elif silt > sand > 10 and clay < 10:
                    print("Led 178, 1987")
                    print("Sandy silt/Sandy siltstone")
                elif silt > sand > 10 and silt > clay > 10:
                    print("Led 178, 1987")
                    print("Silt mud/Silty mudstone")

            if clay > 80:
                print("Led 178, 1987")
                print("Clay/claystone")
            elif silt < 80:

                if clay > silt > 10 and sand < 10:
                    print("Led 178, 1987")
                    print("Silty clay/Silty claystone")
                elif clay > sand > 10 and silt < 10:
                    print("Led 178, 1987")
                    print("Sandy silt/Sandy siltstone")
                elif clay > sand > 10 and clay > silt > 10:
                    print("Led 178, 1987")
                    print("Silt mud/Silty mudstone")


        class Leg178:
            if sand > 75:
                print("Leg 178, 1999")
                print("Sand/sandstone")
            elif sand < 75:

                if sand > silt > 12.5 and clay < 12.5:
                    print("Leg 178, 1999")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > 12.5 and silt < 12.5:
                    print("Leg 178, 1999")
                    print("Clayey sand/Clayey sandstone")
                elif sand > silt > 12.5 and sand > clay > 12.5:
                    print("Leg 178, 1999")
                    print("Sandy mud/Sandy mudstone")

            if silt > 75:
                print("Leg 178, 1999")
                print("Silt/siltstone")
            elif silt < 75:

                if silt > clay > 12.5 and sand < 12.5:
                    print("Leg 178, 1999")
                    print("Clayey silt/Clayey siltstone")
                elif silt > sand > 12.5 and clay < 12.5:
                    print("Leg 178, 1999")
                    print("Sandy silt/Sandy siltstone")
                elif silt > sand > 12.5 and silt > clay > 12.5:
                    print("Leg 178, 1999")
                    print("Silt mud/Silty mudstone")

            if clay > 75:
                print("Leg 178, 1999")
                print("Clay/claystone")
            elif silt < 75:

                if clay > silt > 12.5 and sand < 12.5:
                    print("Leg 178, 1999")
                    print("Silty clay/Silty claystone")
                elif clay > sand > 12.5 and silt < 12.5:
                    print("Leg 178, 1999")
                    print("Sandy clay/Sandy claystone")
                elif clay > sand > 12.5 and clay > silt > 12.5:
                    print("Leg 178, 1999")
                    print("Clayey mud/Clayey mudstone")


        class Leg183:
            if sand > 75:
                print("Leg 183, 2000")
                print("Sand/Sandstone")
            elif 40 < sand < 75:

                if sand > silt > clay and clay < 20:
                    print("Leg 183, 2000")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > silt and silt < 20:
                    print("Leg 183, 2000")
                    print("Clayey sand/Clayey sandstone")

            if silt > 75:
                print("Leg 183, 2000")
                print("Silt/Siltstone")
            elif 40 < silt < 75:

                if silt > sand > clay and clay < 20:
                    print("Leg 183, 2000")
                    print("Sandy silt/Sandy siltstone")
                elif silt > clay > sand and sand < 20:
                    print("Leg 183, 2000")
                    print("Clayey silt/Clayey siltstone")

            if clay > 75:
                print("Leg 183, 2000")
                print("Clay/Claystone")
            elif 40 < clay < 75:

                if clay > sand > silt and silt < 20:
                    print("Leg 183, 2000")
                    print("Sandy clay/Sandy claystone")
                elif clay > silt > sand and sand < 20:
                    print("Leg 183, 2000")
                    print("Silty clay/Silty claystone")
            elif 20 < clay < 60:

                if 40< sand < 60 and 20 < silt < 60:
                    print("Leg 183, 2000")
                    print("Muddy sand/Muddy sandstone")
                elif 20 < sand < 40 and 20 < silt < 60:
                    print("Leg 183, 2000")
                    print("Sandy mud/Sandy mudstone")


        class Leg210:
            if sand > 80:
                print("Leg 210, 2004")
                print("Sand/sandstone")
            elif sand < 80:

                if sand > silt > clay and clay < 20:
                    print("Leg 210, 2004")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > silt and silt < 20:
                    print("Leg 210, 2004")
                    print("Clayey sand/Clayey sandstone")

            if silt > 80:
                print("Leg 210, 2004")
                print("Silt/siltstone")
            elif silt < 80:

                if silt > clay > sand and sand < 20:
                    print("Leg 210, 2004")
                    print("Clayey silt/Clay siltstone")
                elif silt > sand > clay and clay < 20:
                    print("Leg 210, 2004")
                    print("Sandy silt/Sandy siltstone")

            if clay > 80:
                print("Leg 210, 2004")
                print("Clay/claystone")
            elif silt < 80:

                if clay > silt > sand and sand < 20:
                    print("Leg 210, 2004")
                    print("Silty clay/Silty claystone")
                elif clay > sand > silt and silt < 20:
                    print("Leg 210, 2004")
                    print("Sandy clay/Sandy claystone")

            if 20 < sand < 60 and 20 < silt < 60 and 20 < clay < 60:
                print("Leg 210, 2004")
                print("Sandy mud/Sandy mudstone to Muddy sand/Muddy sandstone")


        class Expendition317:
            if sand > 80:
                print("Expendition 317, 2011")
                print("Sand/sandstone")
            elif sand < 80:

                if sand > silt > clay and clay < 20:
                    print("Expendition 317, 2011")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > silt and silt < 20:
                    print("Expendition 317, 2011")
                    print("Clayey sand/Clayey sandstone")

            if silt > 80:
                print("Expendition 317, 2011")
                print("Silt/siltstone")
            elif silt < 80:

                if silt > clay > sand and sand < 20:
                    print("Expendition 317, 2011")
                    print("Clayey silt/Clay siltstone")
                elif silt > sand > clay and clay < 20:
                    print("Expendition 317, 2011")
                    print("Sandy silt/Sandy siltstone")

            if clay > 80:
                print("Expendition 317, 2011")
                print("Clay/claystone")
            elif silt < 80:

                if clay > silt > sand and sand < 20:
                    print("Expendition 317, 2011")
                    print("Silty clay/Silty claystone")
                elif clay > sand > silt and silt < 20:
                    print("Expendition 317, 2011")
                    print("Sandy clay/Sandy claystone")

            if 20 < silt < 60 and 20 < clay < 60:

                if 50 < sand < 60:
                    print("Expendition 317, 2011")
                    print("Muddy sand/Muddy sandstone")
                elif 20 < sand < 50:
                    print("Expendition 317, 2011")
                    print("Sandy mud/Sandy mudstone")


        class Expendition323:
            if sand > 75:
                print("Expendition 323, 2011")
                print("Sand/sandstone")
            elif sand < 75:

                if sand > silt > clay:
                    print("Expendition 323, 2011")
                    print("Silty sand/Silty sandstone")
                elif sand > clay > silt:
                    print("Expendition 323, 2011")
                    print("Clayey sand/Clayey sandstone")

            if silt > 75:
                print("Expendition 323, 2011")
                print("Silt/siltstone")
            elif silt < 75:

                if silt > clay > sand:
                    print("Expendition 323, 2011")
                    print("Clayey silt/Clay siltstone")
                elif silt > sand > clay:
                    print("Expendition 323, 2011")
                    print("Sandy silt/Sandy siltstone")

            if clay > 75:
                print("Expendition 323, 2011")
                print("Clay/Claystone")
            elif silt < 75:

                if clay > silt > sand:
                    print("Expendition 323, 2011")
                    print("Silty clay/Silty claystone")
                elif clay > sand > silt and silt < 20:
                    print("Expendition 323, 2011")
                    print("Sandy clay/Sandy claystone")


        class Expendition339:
            if clay > 75:
                print("Expendition 339, 2013")
                print("Clay/Claystone")
            elif 25 < clay < 75:
                print("Expendition 339, 2013")
                print("Mud/Mudstone")
            elif 25 < clay <50:

                if sand > silt:
                    print("Expendition 339, 2013")
                    print("Sandy mud/Sandy mudstone")
                elif silt > sand:
                    print("Expendition 339, 2013")
                    print("Silty mud/Silty mudstone")

            if sand > 75:
                print("Expendition 339, 2013")
                print("Sand/Sandstone")
            elif clay < 25 and silt < sand < 75:
                print("Expendition 339, 2013")
                print("Sandy silt/Sandy siltstone")

            if silt > 75:
                print("Expendition 339, 2013")
                print("Silt/Siltstone")
            elif clay < 25 and sand < silt < 75:
                print("Expendition 339, 2013")
                print("Silty sand/Silty sandstone")


    else:
        print("您输入的不正确请重新输入：")



