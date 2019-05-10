# qgis_graph2linestring
Short function that is converting graph from csv to WKT linestring format for direct import into QGIS.

To import graph with georeferenced point into QGIS software it needs to be in specific format. 
Text format with geometry that is readable for QGIS is WKT (well known text). If you want to present lines the proper formating is:

                            LINESTRING(longitude1 latitude1, longitude2 latitude2)
                            
REMEMBER to use semicolon as delimiter, since comma is used for linestring.

Short remider: 
Longitude represent easting [-180, +180], it refers to X coordinate
Latitude represent northing [-90, +90] it refers to Y coordinate.
