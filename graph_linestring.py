


def main():
    graphfile = "/home/olivera/IdeaProjects/foursquare/graph_Singapore_2017_04/graph_Singapore_2017_04.csv"
    nf = open("linestring_graph_Singapore_2017_04.csv", 'w')
    nf.write("line;w" + '\n')
    with open(graphfile, 'r') as gf:
        lines = gf.readlines()[1:]
        for line in lines:
            el = line.split(',')
            lat1 = el[0]
            lng1 = el[1]
            lat2 = el[2]
            lng2 = el[3]
            w = el[4]
            nf.write("LINESTRING(" + str(lng1) + " " + str(lat1) + ", " + str(lng2) + " " + str(lat2) + ")" + ";" + str(w))

    nf.close()



if __name__ == '__main__':
    main()
