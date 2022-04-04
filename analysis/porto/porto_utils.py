import numpy as np

# camera coordinates... 225 of them
camera_coordinates = np.array([[41.16594068785048, -8.685427677460588], [41.16060982545167, -8.682337772675432],
                               [41.16579530644621, -8.678174984284318], [41.16346916011173, -8.67639399749843],
                               [41.16122370442626, -8.678797256775773], [41.15734647753728, -8.681007397004045],
                               [41.157168765807775, -8.67836810333339], [41.16129044998169, -8.676284605657525],
                               [41.16381052189705, -8.671692663824029], [41.161387377616514, -8.671113306676812],
                               [41.15390231632685, -8.67444652285714], [41.14975674363342, -8.674679188843138],
                               [41.15224494531915, -8.669550805206663],
                               [41.148884234966246, -8.673155694122679], [41.148286398250235, -8.669829754944212],
                               [41.15150172613503, -8.668220429535276], [41.15571857543715, -8.668821244354612],
                               [41.15284274594009, -8.667211918945677], [41.152471140789785, -8.664830117340452],
                               [41.15027378032761, -8.662512688751585], [41.147236131360394, -8.667104630585081],
                               [41.15386061013024, -8.657684712524778], [41.16322432417219, -8.66345474986888],
                               [41.160964042358586, -8.667469154923575], [41.15749069021114, -8.665731083481925],
                               [41.16043093514962, -8.658414017289298], [41.161610227101164, -8.656075131028311],
                               [41.14815150110105, -8.654113853717472], [41.15072486410714, -8.657214629330728],
                               [41.18707144574136, -8.67024443608042], [41.1897776469415, -8.682627025976144],
                               [41.195897526773386, -8.684459169251877], [41.18244858892193, -8.685159531574433],
                               [41.17996153389792, -8.682799187641328], [41.178443414932374, -8.682069626789277],
                               [41.180541542621214, -8.666159266342552], [41.17264470574743, -8.689343665672768],
                               [41.17183930253319, -8.680867885185707],
                               [41.17055361324843, -8.65751340567121], [41.1661711024398, -8.661061877697751],
                               [41.16626802285595, -8.651663417309567], [41.16859406983704, -8.668872470349118],
                               [41.168335624250155, -8.649002665966794], [41.17758799482947, -8.643315746175892],
                               [41.17225257049447, -8.624212219522198], [41.179165225526425, -8.623825981424053],
                               [41.18349333904548, -8.631507828042706], [41.1896297261061, -8.633481933877666],
                               [41.1876273893279, -8.64438243131419], [41.17748558205152, -8.642794563577374],
                               [41.177491028600876, -8.656109781502142], [41.1661855126207, -8.643466300178277],
                               [41.16525529092104, -8.64533715377242], [41.160958281697106, -8.64956431517989],
                               [41.153752889627306, -8.650293876031942], [41.154111871136145, -8.64533715377242],
                               [41.15075075059518, -8.64472873849562], [41.149068711945404, -8.641003895634789],
                               [41.152316315132566, -8.633107472294945], [41.14695473250925, -8.63332920902918],
                               [41.14499435575744, -8.640120562254888], [41.143200722857195, -8.64207321041773],
                               [41.13846740733647, -8.63687900674755], [41.13765939024977, -8.62941173685009],
                               [41.11424909927572, -8.627651298907727], [41.12510578598322, -8.606306161122959],
                               [41.11922199592545, -8.606821145253818], [41.135869816512596, -8.608553369852139],
                               [41.12788585490584, -8.593833406778408], [41.11966246983385, -8.601206785820679],
                               [41.137150533527425, -8.581251150749878], [41.1256683829191, -8.57989232005877],
                               [41.162895387839335, -8.634232551624706], [41.15704729851807, -8.630230695774486],
                               [41.1630853310423, -8.625163567907848], [41.16671991969178, -8.625506890661754],
                               [41.163069176865, -8.624970448858775], [41.166933903928395, -8.634746278064833],
                               [41.150591077905176, -8.63405963255702], [41.15611662617745, -8.62109919859706],
                               [41.14695540965855, -8.620627129810439], [41.15298865423673, -8.610347990459799],
                               [41.14562080151092, -8.611377958721517],
                               [41.14094941127508, -8.613441842157451], [41.1480429635048, -8.599233846957137],
                               [41.14206427434463, -8.602323751742293], [41.14983378467618, -8.580463357400523],
                               [41.157879696745354, -8.583494464565586], [41.16692612909815, -8.588472644497227],
                               [41.17125552837304, -8.59611157577164], [41.16476203781398, -8.599072734524082],
                               [41.16164690298464, -8.61319311046275], [41.1477681730759, -8.611687496243272],
                               [41.178053045333485, -8.606439531532354], [41.18347269478744, -8.603843153205938],
                               [41.180421484980336, -8.593672918585153], [41.19540687845471, -8.591612982061715],
                               [41.199992240177856, -8.612126516607614], [41.18862512091725, -8.652236151608614],
                               [41.18991772129928, -8.621978131997741], [41.184692298958794, -8.5564568452585],
                               [41.1802350652289, -8.535881339928157], [41.16770150722932, -8.543949424644953],
                               [41.14201297990058, -8.54729682149554], [41.13446767382651, -8.537319691383018],
                               [41.13033026909225, -8.525389225684776], [41.13841089484227, -8.518909008704796],
                               [41.14720148501666, -8.532212765418663],
                               [41.15584570777076, -8.59539788413757], [41.15823674620635, -8.59917443443054],
                               [41.16004612272103, -8.592737132794797], [41.16159697712035, -8.575141841657102],
                               [41.15555489984987, -8.572824413068235], [41.16715390402402, -8.570473194122314],
                               [41.15794594889333, -8.56734037399292], [41.146780149976536, -8.589251799624485],
                               [41.150464114697, -8.59435872558884], [41.14794352961828, -8.598736090701145],
                               [41.14532589639753, -8.619678778689426], [41.162387107470416, -8.625000281374973],
                               [41.1565712843642, -8.610237402957004], [41.151659742964675, -8.626459403079075],
                               [41.15321079579316, -8.613670630496067], [41.14952698540703, -8.6113532019072],
                               [41.15579580229212, -8.59161214355759], [41.17593898829544, -8.603877691900523],
                               [41.17135590536507, -8.606066374456676], [41.17563395608471, -8.600346146911699],
                               [41.17345352377201, -8.605957328170854], [41.175240144918604, -8.608608898828315],
                               [41.17719158517758, -8.609261919749732], [41.17821714644638, -8.606461693538185],
                               [41.177491081048764, -8.614176432794851], [41.17831475768118, -8.617910067743582],
                               [41.176425131207615, -8.619369189447683], [41.18288516725516, -8.613661448663992],
                               [41.179843955134544, -8.582591970328183], [41.179004147484015, -8.57061238120897],
                               [41.17512797263357, -8.566814373243883], [41.17006143033471, -8.58707057300524],
                               [41.17138591830332, -8.61308399550736], [41.16750937761953, -8.622422665864377],
                               [41.16612019760711, -8.606801480561643], [41.1608190982916, -8.607601433099415],
                               [41.186145227420376, -8.594641401328834],
                               [41.20178142684863, -8.650680760537854], [41.20596275319949, -8.6280858317964],
                               [41.1893102681115, -8.633428562872231], [41.15905182238579, -8.649969112712306],
                               [41.159570072576635, -8.64477815679943], [41.14965012632784, -8.641216183227654],
                               [41.16087015961073, -8.610270707613296], [41.15595894032283, -8.620999543672866],
                               [41.15272767431322, -8.608124940401382], [41.14652319710046, -8.615506379610366],
                               [41.1502071762577, -8.621257035738296], [41.16390717685348, -8.62039872885353],
                               [41.15731602455084, -8.591473786836929], [41.15996548897161, -8.573878495699233],
                               [41.16093477846425, -8.633230416780776], [41.15014254682827, -8.62614938498146],
                               [41.16345653883778, -8.601508148870293], [41.162945774839024, -8.581755845950829],
                               [41.146660308496486, -8.587334840701805], [41.15551441707591, -8.605359285281883],
                               [41.1661119234556, -8.601411073611962], [41.162675471082466, -8.634042456810096],
                               [41.15918605449983, -8.63593073195658], [41.15429224764543, -8.673138453888777],
                               [41.1612067975824, -8.637947871613386], [41.1632745586727, -8.645758464264754],
                               [41.187630456820145, -8.644814326691511], [41.1861448126132, -8.658976390290144],
                               [41.16876673225571, -8.667387797760847], [41.175709167534286, -8.603993246870775],
                               [41.17241426779562, -8.598757574873705], [41.16627626759425, -8.597555945235033],
                               [41.16608242664297, -8.573008368330736], [41.15100945759292, -8.567300500609884],
                               [41.15178499628671, -8.59734124157668], [41.14661456504063, -8.587642373778829],
                               [41.16304623675184, -8.63414297638604], [41.15787669368909, -8.63637457428643],
                               [41.152835996615124, -8.640837770087211], [41.16084923077286, -8.634314637762992],
                               [41.144175432613814, -8.597064118964164], [41.149992355473785, -8.593802552802055],
                               [41.14520958994829, -8.597235780341117], [41.15671349030644, -8.610110383612602],
                               [41.15399926880495, -8.612341981512992], [41.15102642106874, -8.610282044989555],
                               [41.165243169079005, -8.568053346259086], [41.1609784684575, -8.597750764471977],
                               [41.1574889615218, -8.610110383612602], [41.15697198173094, -8.607878785712211],
                               [41.14947531656027, -8.603243928534477], [41.1458559300004, -8.61440191803643],
                               [41.144175432613814, -8.616118531805961], [41.16511393980446, -8.618865113837211],
                               [41.16569546953293, -8.612084489447563], [41.16763386468877, -8.629937272650688],
                               [41.16459702015774, -8.643069367987602], [41.16110770588725, -8.637833695990532],
                               [41.15975070016419, -8.617320161444633], [41.15839366634432, -8.612599473578422],
                               [41.16459702015774, -8.599896531683891],
                               [41.154580897159086, -8.60590467987725], [41.153288382697326, -8.61362944184014],
                               [41.15684273614612, -8.624529939276664], [41.15218972536813, -8.621010881049125],
                               [41.160267658038364, -8.616805177313774], [41.169572202501996, -8.603587251288383],
                               [41.172350386700785, -8.613028627020805], [41.1759037064046, -8.604188066107719],
                               [41.17390094991022, -8.634228807074516], [41.17041213107955, -8.6419535690374],
                               [41.166664674278636, -8.614573579413383], [41.1634339360438, -8.601613145453422],
                               [41.15975070016419, -8.61740599213311], [41.158910634922044, -8.614230256659477],
                               [41.158846014072815, -8.579468827826469], [41.1427063379118, -8.61045937087383],
                               [41.14823255068787, -8.601103825829885], [41.1786041323577, -8.629825452542834],
                               [41.145196694982666, -8.57974324581676]])

# convert lat, lon -> lon, lat
camera_coordinates = camera_coordinates[:, ::-1]  # lat, lon --> lon, lat


def analy_str_xy(s):
    terms = s.strip("[").strip("]").strip("\n").split("],[")
    return terms


def check_overlap(cam_center_xy, Lon_inter, Lat_inter):
    true_cam_xy = []
    # if -8.630230695774486 41.15704729851807
    for i in range(cam_center_xy.shape[0]):
        coor = dict()
        coor['x1'] = cam_center_xy[i][0]  # - Lon_inter
        coor['y1'] = cam_center_xy[i][1]  # - Lat_inter
        coor['x2'] = cam_center_xy[i][0] + Lon_inter
        coor['y2'] = cam_center_xy[i][1] + Lat_inter
        flag = 0
        for j in range(i, cam_center_xy.shape[0]):
            if i == j:
                continue
            xj1 = cam_center_xy[j][0]  # - Lon_inter
            yj1 = cam_center_xy[j][1]  # - Lat_inter
            xj2 = cam_center_xy[j][0] + Lon_inter
            yj2 = cam_center_xy[j][1] + Lat_inter
            count = 0
            if (xj1 > coor['x1'] and xj1 < coor['x2']) or (xj2 > coor['x1'] and xj2 < coor['x2']):
                count += 1
            if (yj1 > coor['y1'] and yj1 < coor['y2']) or (yj2 > coor['y1'] and yj2 < coor['y2']):
                count += 1
            if count == 2:
                # print(i,j,cam_center_xy[i],cam_center_xy[j])
                flag = 1
                break

        if flag == 0:
            true_cam_xy.append([cam_center_xy[i][0], cam_center_xy[i][1]])
    return true_cam_xy


def cam_map_index(cam_center_xy, Lon_inter, Lat_inter, Lon_a, Lon_b, Lat_a, Lat_b):
    camap_index = dict()
    for i in range(cam_center_xy.shape[0]):
        small_float = 0.001
        xindex = int((cam_center_xy[i][0] - small_float * Lon_inter - Lon_a) / (1.05 * Lon_inter))
        yindex = int((cam_center_xy[i][1] - small_float * Lat_inter - Lat_a) / (1.05 * Lat_inter))
        # print(xindex,yindex)
        if camap_index.get(xindex) == None:
            camap_index[xindex] = dict()
        if camap_index[xindex].get(yindex) == None:
            camap_index[xindex][yindex] = []
        camap_index[xindex][yindex].append(i)

        xindex = int((cam_center_xy[i][0] + (1 + small_float) * Lon_inter - Lon_a) / (1.05 * Lon_inter))
        yindex = int((cam_center_xy[i][1] + (1 + small_float) * Lat_inter - Lat_a) / (1.05 * Lat_inter))
        # print(xindex,yindex)
        if camap_index.get(xindex) == None:
            camap_index[xindex] = dict()
        if camap_index[xindex].get(yindex) == None:
            camap_index[xindex][yindex] = []
        camap_index[xindex][yindex].append(i)

        xindex = int((cam_center_xy[i][0] - small_float * Lon_inter - Lon_a) / (1.05 * Lon_inter))
        yindex = int((cam_center_xy[i][1] + (1 + small_float) * Lat_inter - Lat_a) / (1.05 * Lat_inter))
        # print(xindex,yindex)
        if camap_index.get(xindex) == None:
            camap_index[xindex] = dict()
        if camap_index[xindex].get(yindex) == None:
            camap_index[xindex][yindex] = []
        camap_index[xindex][yindex].append(i)

        xindex = int((cam_center_xy[i][0] + (1 + small_float) * Lon_inter - Lon_a) / (1.05 * Lon_inter))
        yindex = int((cam_center_xy[i][1] - small_float * Lat_inter - Lat_a) / (1.05 * Lat_inter))
        # print(xindex,yindex)
        if camap_index.get(xindex) == None:
            camap_index[xindex] = dict()
        if camap_index[xindex].get(yindex) == None:
            camap_index[xindex][yindex] = []
        camap_index[xindex][yindex].append(i)

    return camap_index