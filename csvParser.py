# -*- coding: utf-8 -*-
import csv
import sys
import numpy as np


def csvParser(path):
    try:
        nodes = []  # parsed nodes array
        errNodes = []  # unparsed nodes array (not possible)
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader)
            for row in reader:
                try:
                    # filter on London's pubs (facultative but really advised)
                    if(row[8] == 'City of London'):
                        nodes.append((int(row[5]), int(row[4])))
                except ValueError:
                    errNodes.append((row))

    except csv.Error as e:
        print('file {}, line {}: {}'.format(path, reader.line_num, e))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        if(len(errNodes)):  # Loggin error
            print("/!\ W : see error.log for more info")
            file = open('error.log', 'w')
            file.write("Can't cast northing or easting to int : \n")
            for node in errNodes:
                file.write(str(node)+'\n')
            file.close()

        return list(set(nodes))  # filtering duplicate values
