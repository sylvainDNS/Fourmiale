# -*- coding: utf-8 -*-
import csv
import sys


def csvParser(path):
    try:
        nodes = []
        errNodes = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader)
            for row in reader:
                try:
                    if(row[8] == 'City of London'):
                        # if(len(nodes) < 20):
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

        filteredNodes = []  # Filtering duplicates values
        for node in set(nodes):
            filteredNodes.append(node)

        return filteredNodes
