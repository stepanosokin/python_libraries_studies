# https://pcjericks.github.io/py-gdalogr-cookbook/geometry.html
# https://gdal.org/api/python/osgeo.ogr.html
from osgeo import ogr
from base64 import b64decode

# Create a Point
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(1198054.34, 648493.09)
print(point.ExportToWkt())

# Create a LineString
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(1116651.439379124, 637392.6969887456)
line.AddPoint(1188804.0108498496, 652655.7409537067)
line.AddPoint(1226730.3625203592, 634155.0816022386)
line.AddPoint(1281307.30760719, 636467.6640211721)
print(line.ExportToWkt())

# Create a Polygon
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
print(poly.ExportToWkt())

# Create a Polygon with holes
outRing = ogr.Geometry(ogr.wkbLinearRing)
outRing.AddPoint(1154115.274565847, 686419.4442701361)
outRing.AddPoint(1154115.274565847, 653118.2574374934)
outRing.AddPoint(1165678.1866605144, 653118.2574374934)
outRing.AddPoint(1165678.1866605144, 686419.4442701361)
outRing.AddPoint(1154115.274565847, 686419.4442701361)
innerRing = ogr.Geometry(ogr.wkbLinearRing)
innerRing.AddPoint(1149490.1097279799, 691044.6091080031)
innerRing.AddPoint(1149490.1097279799, 648030.5761158396)
innerRing.AddPoint(1191579.1097525698, 648030.5761158396)
innerRing.AddPoint(1191579.1097525698, 691044.6091080031)
innerRing.AddPoint(1149490.1097279799, 691044.6091080031)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(outRing)
poly.AddGeometry(innerRing)
print(poly.ExportToWkt())

# Create a MultiPoint
multipoint = ogr.Geometry(ogr.wkbMultiPoint)
point1 = ogr.Geometry(ogr.wkbPoint)
point1.AddPoint(1251243.7361610543, 598078.7958668759)
multipoint.AddGeometry(point1)
point2 = ogr.Geometry(ogr.wkbPoint)
point2.AddPoint(1240605.8570339603, 601778.9277371694)
multipoint.AddGeometry(point2)
point3 = ogr.Geometry(ogr.wkbPoint)
point3.AddPoint(1250318.7031934808, 606404.0925750365)
multipoint.AddGeometry(point3)
print(multipoint.ExportToWkt())

# Create a MultiLineString
multiline = ogr.Geometry(ogr.wkbMultiLineString)
line1 = ogr.Geometry(ogr.wkbLineString)
line1.AddPoint(1214242.4174581182, 617041.9717021306)
line1.AddPoint(1234593.142744733, 629529.9167643716)
multiline.AddGeometry(line1)
line2 = ogr.Geometry(ogr.wkbLineString)
line2.AddPoint(1184641.3624957693, 626754.8178616514)
line2.AddPoint(1219792.6152635587, 606866.6090588232)
multiline.AddGeometry(line2)
print(multiline.ExportToWkt())

# Create a MultiPolygon
multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)
poly1 = ogr.Geometry(ogr.wkbPolygon)
ring1 = ogr.Geometry(ogr.wkbLinearRing)
ring1.AddPoint(1204067.0548148106, 634617.5980860253)
ring1.AddPoint(1204067.0548148106, 620742.1035724243)
ring1.AddPoint(1215167.4504256917, 620742.1035724243)
ring1.AddPoint(1215167.4504256917, 634617.5980860253)
ring1.AddPoint(1204067.0548148106, 634617.5980860253)
poly1.AddGeometry(ring1)
multipolygon.AddGeometry(poly1)
poly2 = ogr.Geometry(ogr.wkbPolygon)
ring1 = ogr.Geometry(ogr.wkbLinearRing)
ring1.AddPoint(1179553.6811741155, 647105.5431482664)
ring1.AddPoint(1179553.6811741155, 626292.3013778647)
ring1.AddPoint(1194354.20865529, 626292.3013778647)
ring1.AddPoint(1194354.20865529, 647105.5431482664)
ring1.AddPoint(1179553.6811741155, 647105.5431482664)
poly2.AddGeometry(ring1)
multipolygon.AddGeometry(poly2)
print(multipolygon.ExportToWkt())

# Create a GeometryCollection
geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(-122.23, 47.09)
geomcol.AddGeometry(point)
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(-122.60, 47.14)
line.AddPoint(-122.48, 47.23)
geomcol.AddGeometry(line)
print(geomcol.ExportToWkt())

# Create Geometry from WKT
wkt = 'POINT (1120351.5712494177 741921.4223245403)'
point = ogr.CreateGeometryFromWkt(wkt)
print(f'{point.GetX()}, {point.GetY()}')

# Create Geometry from GeoJSON
geojson = """{"type":"Point","coordinates":[108420.33,753808.59]}"""
point = ogr.CreateGeometryFromJson(geojson)
print(f'{point.GetX()}, {point.GetY()}')

# Create Geometry from GML
gml = """<gml:Point xmlns:gml="http://www.opengis.net/gml"><gml:coordinates>108420.33,753808.59</gml:coordinates></gml:Point>"""
point = ogr.CreateGeometryFromGML(gml)
print(f'{point.GetX()}, {point.GetY()}')

# Create Geometry from WKB
wkb = b64decode("AIAAAAFBMkfmVwo9cUEjylouFHrhAAAAAAAAAAA=")
point = ogr.CreateGeometryFromWkb(wkb)
print(f'{point.GetX()}, {point.GetY()}')

# Count Points in a Geometry
wkt = "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
line = ogr.CreateGeometryFromWkt(wkt)
print(line.GetPointCount())

# Count Geometries in a Geometry
wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
multipoint = ogr.CreateGeometryFromWkt(wkt)
print(f'Geometry has {multipoint.GetGeometryCount()} geometries')

# Iterate over Geometries in a Geometry
wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
multipoint = ogr.CreateGeometryFromWkt(wkt)
for point in multipoint:
    print(f'{point.GetX()}, {point.GetY()}')
# OR
for i in range(multipoint.GetGeometryCount()):
    pt = multipoint.GetGeometryRef(i)
    print(f'{i + 1}) {pt.ExportToWkt()}')

# Buffer a Geometry
wkt = 'POINT (1198054.34 648493.09)'
point = ogr.CreateGeometryFromWkt(wkt)
bufferDistance = 500
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.Buffer
buffer = point.Buffer(bufferDistance)
print(f'{point.ExportToWkt()} buffered by {bufferDistance} is {buffer.ExportToWkt()}')

# Calculate Envelope of a Geometry
wkt = "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
line = ogr.CreateGeometryFromWkt(wkt)
# Get Envelope returns a tuple (minX, maxX, minY, maxY)
env = line.GetEnvelope()
print(f'minX: {env[0]}, minY: {env[1]}, maxX: {env[2]}, maxY: {env[3]}')

# Calculate the Area of a Geometry
wkt = "POLYGON ((1162440.5712740074 672081.4332727483, 1162440.5712740074 647105.5431482664, 1195279.2416228633 647105.5431482664, 1195279.2416228633 672081.4332727483, 1162440.5712740074 672081.4332727483))"
polygon = ogr.CreateGeometryFromWkt(wkt)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.GetArea
print(f'Area = {polygon.GetArea()}')

# Calculate the Length of a Geometry
wkt = "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
line = ogr.CreateGeometryFromWkt(wkt)
print(f'Length = {line.Length()}')

# Get the geometry type (as a string) from a Geometry
wkts = [
    "POINT (1198054.34 648493.09)",
    "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)",
    "POLYGON ((1162440.5712740074 672081.4332727483, 1162440.5712740074 647105.5431482664, 1195279.2416228633 647105.5431482664, 1195279.2416228633 672081.4332727483, 1162440.5712740074 672081.4332727483))"
]
for wkt in wkts:
    geom = ogr.CreateGeometryFromWkt(wkt)
    print(f'{geom.GetGeometryName()}')

# Calculate intersection between two Geometries
wkt1 = "POLYGON ((1208064.271243039 624154.6783778917, 1208064.271243039 601260.9785661874, 1231345.9998651114 601260.9785661874, 1231345.9998651114 624154.6783778917, 1208064.271243039 624154.6783778917))"
wkt2 = "POLYGON ((1199915.6662253144 633079.3410163528, 1199915.6662253144 614453.958118695, 1219317.1067437078 614453.958118695, 1219317.1067437078 633079.3410163528, 1199915.6662253144 633079.3410163528)))"
poly1 = ogr.CreateGeometryFromWkt(wkt1)
poly2 = ogr.CreateGeometryFromWkt(wkt2)
intersect = poly1.Intersection(poly2)
print(f'Intersection is {intersect.ExportToWkt()}')

# Calculate union between two Geometries
wkt1 = "POLYGON ((1208064.271243039 624154.6783778917, 1208064.271243039 601260.9785661874, 1231345.9998651114 601260.9785661874, 1231345.9998651114 624154.6783778917, 1208064.271243039 624154.6783778917))"
wkt2 = "POLYGON ((1199915.6662253144 633079.3410163528, 1199915.6662253144 614453.958118695, 1219317.1067437078 614453.958118695, 1219317.1067437078 633079.3410163528, 1199915.6662253144 633079.3410163528)))"
poly1 = ogr.CreateGeometryFromWkt(wkt1)
poly2 = ogr.CreateGeometryFromWkt(wkt2)
union = poly1.Union(poly2)
print(f'Union is: {union.ExportToWkt()}')

# Write Geometry to GeoJSON
# option 1
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.GetDriverByName
outDriver = ogr.GetDriverByName('GeoJSON')
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver.CreateDataSource
outDataSource = outDriver.CreateDataSource('test.geojson')
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.DataSource.CreateLayer
outLayer = outDataSource.CreateLayer('test.geojson', geom_type=ogr.wkbPolygon)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.GetLayerDefn
fetDef = outLayer.GetLayerDefn()
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Feature
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.FeatureDefn
# check infostring
outFeature = ogr.Feature(fetDef)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Feature.SetGeometry
outFeature.SetGeometry(poly)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.CreateFeature
outLayer.CreateFeature(outFeature)
outFeature = None
outDataSource = None
# option 2
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.ExportToJson
geojson = poly.ExportToJson()
print(geojson)

# https://pcjericks.github.io/py-gdalogr-cookbook/geometry.html#write-geometry-to-wkt

# Write Geometry to WKT
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
wkt = poly.ExportToWkt()
print(wkt)

# Write Geometry to KML
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(91.1646903288, 82.8838459781)
ring.AddPoint(53.0218226474, 56.2684348812)
ring.AddPoint(04.933941905, 72.8288590391)
ring.AddPoint(80.428455506, 19.3123998424)
ring.AddPoint(05.0658121984, 8.1805541387)
ring.AddPoint(91.1646903288, 82.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
print(poly.ExportToKML())

# Write Geometry to WKB
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)
print(poly.ExportToWkb())

# Force polygon to multipolygon
poly_wkt= "POLYGON ((1179091.164690328761935 712782.883845978067257,1161053.021822647424415 667456.268434881232679,1214704.933941904921085 641092.828859039116651,1228580.428455505985767 682719.312399842427112,1218405.065812198445201 721108.180554138729349,1179091.164690328761935 712782.883845978067257))"
poly = ogr.CreateGeometryFromWkt(poly_wkt)
if poly.GetGeometryType() == ogr.wkbPolygon:
    poly = ogr.ForceToMultiPolygon(poly)
print(poly.ExportToWkt())



# Quarter polygon and create centroids
poly_Wkt= "POLYGON((-107.42631019589980212 40.11971708125970082,-107.42455436683293613 40.12061219666851741,-107.42020981542387403 40.12004414402532859,-107.41789122063043749 40.12149008687303819,-107.41419947746419439 40.11811617239460048,-107.41915181585792993 40.11761695654455906,-107.41998470913324581 40.11894245264452508,-107.42203317637793702 40.1184088144647788,-107.42430674991324224 40.1174448122981957,-107.42430674991324224 40.1174448122981957,-107.42631019589980212 40.11971708125970082))"
poly = ogr.CreateGeometryFromWkt(poly_Wkt)

# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.GetEnvelope
poly_envelope = poly.GetEnvelope()
minX = poly_envelope[0]
minY = poly_envelope[2]
maxX = poly_envelope[1]
maxY = poly_envelope[3]

'''
coord0----coord1----coord2
|           |           |
coord3----coord4----coord5
|           |           |
coord6----coord7----coord8
'''
coord0 = minX, maxY
coord1 = minX+(maxX-minX)/2, maxY
coord2 = maxX, maxY
coord3 = minX, minY+(maxY-minY)/2
coord4 = minX+(maxX-minX)/2, minY+(maxY-minY)/2
coord5 = maxX, minY+(maxY-minY)/2
coord6 = minX, minY
coord7 = minX+(maxX-minX)/2, minY
coord8 = maxX, minY

ringTopLeft = ogr.Geometry(ogr.wkbLinearRing)
# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.AddPoint_2D
ringTopLeft.AddPoint_2D(*coord0)
ringTopLeft.AddPoint_2D(*coord1)
ringTopLeft.AddPoint_2D(*coord4)
ringTopLeft.AddPoint_2D(*coord3)
ringTopLeft.AddPoint_2D(*coord0)
polyTopLeft = ogr.Geometry(ogr.wkbPolygon)
polyTopLeft.AddGeometry(ringTopLeft)

ringTopRight = ogr.Geometry(ogr.wkbLinearRing)
ringTopRight.AddPoint_2D(*coord1)
ringTopRight.AddPoint_2D(*coord2)
ringTopRight.AddPoint_2D(*coord5)
ringTopRight.AddPoint_2D(*coord4)
ringTopRight.AddPoint_2D(*coord1)
polyTopRight = ogr.Geometry(ogr.wkbPolygon)
polyTopRight.AddGeometry(ringTopRight)


ringBottomLeft = ogr.Geometry(ogr.wkbLinearRing)
ringBottomLeft.AddPoint_2D(*coord3)
ringBottomLeft.AddPoint_2D(*coord4)
ringBottomLeft.AddPoint_2D(*coord7)
ringBottomLeft.AddPoint_2D(*coord6)
ringBottomLeft.AddPoint_2D(*coord3)
polyBottomLeft = ogr.Geometry(ogr.wkbPolygon)
polyBottomLeft.AddGeometry(ringBottomLeft)


ringBottomRight = ogr.Geometry(ogr.wkbLinearRing)
ringBottomRight.AddPoint_2D(*coord4)
ringBottomRight.AddPoint_2D(*coord5)
ringBottomRight.AddPoint_2D(*coord8)
ringBottomRight.AddPoint_2D(*coord7)
ringBottomRight.AddPoint_2D(*coord4)
polyBottomRight = ogr.Geometry(ogr.wkbPolygon)
polyBottomRight.AddGeometry(ringBottomRight)

# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.Intersection
quarterPolyTopLeft = poly.Intersection(polyTopLeft)
quarterPolyTopRight = poly.Intersection(polyTopRight)
quarterPolyBottomLeft = poly.Intersection(polyBottomLeft)
quarterPolyBottomRight = poly.Intersection(polyBottomRight)

# https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry.Centroid
centroidTopLeft = quarterPolyTopLeft.Centroid()
centroidTopRight = quarterPolyTopRight.Centroid()
centroidBottomLeft = quarterPolyBottomLeft.Centroid()
centroidBottomRight = quarterPolyBottomRight.Centroid()

print(f'centroid 1: {centroidTopLeft.ExportToJson()}')
print(f'centroid 2: {centroidTopRight.ExportToJson()}')
print(f'centroid 3: {centroidBottomLeft.ExportToJson()}')
print(f'centroid 4: {centroidBottomRight.ExportToJson()}')