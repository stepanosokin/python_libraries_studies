# https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html
from osgeo import ogr
from osgeo import gdal
from osgeo import osr
import sys
import os
import csv
from math import ceil
import numpy as np


# # Delete a file
# # https://gdal.org/drivers/vector/shapefile.html#vector-shapefile
# DriverName = 'ESRI Shapefile'
# FileName = 'SHP/test.shp'
# shpdriver = ogr.GetDriverByName(DriverName)
# if os.path.exists(FileName):
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver.DeleteDataSource
#     shpdriver.DeleteDataSource(FileName)
#
#
# # Is Ogr Installed
# try:
#     from osgeo import ogr
#     print('Import of ogr from osgeo worked.  Hurray!\n')
# except:
#     print('Import of ogr from osgeo failed\n\n')
#
#
# # View Auto Generated Ogr Help
# #print(help(ogr))
#
#
# # Get List of Ogr Drivers Alphabetically (A- Z)
# cnt = ogr.GetDriverCount()
# formatsList = []
# for i in range(cnt):
#     driver = ogr.GetDriver(i)
#     driverName = driver.GetName()
#     if not driverName in formatsList:
#         formatsList.append(driverName)
# print(*map(lambda x: f'[{x}]', sorted(formatsList)))
#
#
# # Is Ogr Driver Available by Driver Name
# driverNames = ['ESRI Shapefile', "PostgreSQL", "FileGDB", "SDE"]
# for driverName in driverNames:
#     drv = ogr.GetDriverByName(driverName)
#     if drv is None:
#         print(f'driver [{driverName}] is not available')
#     else:
#         print(f'driver [{driverName}] is available')
#
#
# # Force Ogr Use Named Driver
# # def main(in_file, in_format, out_file, out_format):
# #     if in_format == 'CSV' and in_file[-3:].lower() != 'csv':
# #         in_file = 'CSV:' + in_file
# #     in_ds = ogr.GetDriverByName(in_format).Open(in_file)
# #     out_ds = ogr.GetDriverByName(out_format).CopyDataSource(in_ds, out_file)
# #
# # if __name__ == '__main__':
# #     main(*sys.argv[1:])
#
#
# # Get Shapefile Feature Count
# daShapefile = r"SHP\input_lines.shp"
# driver = ogr.GetDriverByName('ESRI Shapefile')
# dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.
# if dataSource is None:
#     print(f'could not open {daShapefile}')
# else:
#     print(f'opened {daShapefile}')
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.DataSource.GetLayer
#     layer = dataSource.GetLayer()
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.GetFeatureCount
#     fCount = layer.GetFeatureCount()
#     print(f'number of features in {os.path.basename(daShapefile)}: {fCount}')
#
#
# # Get All PostGIS layers in a PostgreSQL Database
# databaseServer = "localhost"
# databaseName = "vgdb"
# databaseUser = "s.osokin"
# databasePW = "Stepanadze"
# databasePort = '5432'
# # https://gdal.org/drivers/vector/pg.html
# connString = f'PG: host={databaseServer} dbname={databaseName} user={databaseUser} password={databasePW} port={databasePort}'
# # or
# # connString = f'postgresql://{databaseUser}:{databasePW}@{databaseServer}:{databasePort}/{databaseName}'
# # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Open
# conn = ogr.Open(connString)
# layerList = sorted([i.GetName() for i in conn])
# print(*layerList, sep='\n')
# print(conn.GetLayerCount())
# conn = None
#
#
# # Get PostGIS Layer Feature Count By Layer Name
# databaseServer = "localhost"
# databaseName = "vgdb"
# databaseUser = "s.osokin"
# databasePW = "Stepanadze"
# databasePort = '5432'
# # https://gdal.org/drivers/vector/pg.html
# connString = f'PG: host={databaseServer} dbname={databaseName} user={databaseUser} password={databasePW} port={databasePort}'
# conn = ogr.Open(connString)
# layerList = sorted([i.GetName() for i in conn])
# lyr = conn.GetLayer(layerList[0])
# featureCount = lyr.GetFeatureCount()
# print(f'Number of features in {layerList[0]} is {featureCount}')
# conn = None
#
#
# # Get all layers in an Esri File GeoDataBase
# # ogr.UseExceptions()
# # driver = ogr.GetDriverByName("OpenFileGDB")
# # try:
# #     gdb = driver.Open('gdb_path', 0)
# # except:
# #     sys.exit()
# # featsClassList = []
# # for featsClass_idx in range(gdb.GetLayerCount()):
# #     featsClass = gdb.GetLayerByIndex(featsClass_idx)
# #     featsClassList.append(featsClass.GetName())
# # featsClassList.sort()
# # for featsClass in featsClassList:
# #     print(featsClass)
# # del gdb
#
#
# # Iterate over Features
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer()
# defn = layer.GetLayerDefn()
# for feature in layer:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name}: {feature.GetField(i)}', end=' | ')
#     print()
#
#
# # Get Geometry from each Feature in a Layer
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer()
# defn = layer.GetLayerDefn()
# for feature in layer:
#     print(feature.GetGeometryRef().ExportToWkt())
#
#
# # Filter by attribute
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer()
# # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.SetAttributeFilter
# layer.SetAttributeFilter("name = 'road 2'")
# defn = layer.GetLayerDefn()
# for feature in layer:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name}: {feature.GetField(i)}', end=' | ')
#     print()
#
#
# # Spatial Filter
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer()
# wkt = 'POLYGON ((-103.81402655265633 50.253951270672125,-102.94583419409656 51.535568561879401,-100.34125711841725 51.328856095555651,-100.34125711841725 51.328856095555651,-93.437060743203844 50.460663736995883,-93.767800689321859 46.450441890315041,-94.635993047881612 41.613370178339181,-100.75468205106476 41.365315218750681,-106.12920617548238 42.564247523428456,-105.96383620242338 47.277291755610058,-103.81402655265633 50.253951270672125))'
# layer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))
# defn = layer.GetLayerDefn()
# print('this is the result of spatial filter: ')
# for feature in layer:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name}: {feature.GetField(i)}', end=' | ')
#     print()
#
#
# # Get Shapefile Fields - Get the user defined fields
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer(0)
# # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.SetAttributeFilter
# defn = layer.GetLayerDefn()
# for feature in layer:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name}: {feature.GetField(i)}', end=' | ')
#     print()
#
#
# # Get Shapefile Fields and Types - Get the user defined fields
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer(0)
# defn = layer.GetLayerDefn()
# for feature in layer:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name} ({ogr.GetFieldTypeName(defn.GetFieldDefn(i).GetType())}, {defn.GetFieldDefn(i).GetWidth()}): {feature.GetField(i)}', end=' | ')
#     print()
#
#
#
# # Get PostGIS Layer Fields - Get the user defined fields
# databaseServer = "localhost"
# databaseName = "vgdb"
# databaseUser = "s.osokin"
# databasePW = "Stepanadze"
# databasePort = '5432'
# # https://gdal.org/drivers/vector/pg.html
# connString = f'PG: host={databaseServer} dbname={databaseName} user={databaseUser} password={databasePW} port={databasePort}'
# conn = ogr.Open(connString)
# layerList = sorted([i.GetName() for i in conn])
# lyr = conn.GetLayer(layerList[0])
# defn = lyr.GetLayerDefn()
# print('\nfields of features from PostGIS layer:')
# print(lyr.GetName())
# for feature in lyr:
#     for i in range(defn.GetFieldCount()):
#         print(f'| {defn.GetFieldDefn(i).name} ({ogr.GetFieldTypeName(defn.GetFieldDefn(i).GetType())}, {defn.GetFieldDefn(i).GetWidth()}): {feature.GetField(i)}', end=' | ')
#     print()
#
# conn = None
#
#
#
# # Get a Layer’s Capabilities
# shapefile = 'SHP/input_lines.shp'
# driver = ogr.GetDriverByName('ESRI Shapefile')
# ds = driver.Open(shapefile)
# layer = ds.GetLayer(0)
# # list of capabilities available by command print(help(ogr)) in the DATA section
# capabilities = [
#     ogr.OLCRandomRead,
#     ogr.OLCSequentialWrite,
#     ogr.OLCRandomWrite,
#     ogr.OLCFastSpatialFilter,
#     ogr.OLCFastFeatureCount,
#     ogr.OLCFastGetExtent,
#     ogr.OLCCreateField,
#     ogr.OLCDeleteField,
#     ogr.OLCReorderFields,
#     ogr.OLCAlterFieldDefn,
#     ogr.OLCTransactions,
#     ogr.OLCDeleteFeature,
#     ogr.OLCFastSetNextByIndex,
#     ogr.OLCStringsAsUTF8,
#     ogr.OLCIgnoreFields
# ]
# print()
# print('Layer capabilities:')
# print(*[f'{cap}: {layer.TestCapability(cap)}' for cap in capabilities], sep='\n')
#
#
# # Create a new Layer from the extent of an existing Layer
# print('Create a new Layer from the extent of an existing Layer:')
# inShapefile = 'SHP/input_lines.shp'
# inDriver = ogr.GetDriverByName('ESRI Shapefile')
# inDataSource = inDriver.Open(inShapefile)
# inLayer = inDataSource.GetLayer()
# extent = inLayer.GetExtent()
#
# ring = ogr.Geometry(ogr.wkbLinearRing)
# ring.AddPoint(extent[0],extent[2])
# ring.AddPoint(extent[1], extent[2])
# ring.AddPoint(extent[1], extent[3])
# ring.AddPoint(extent[0], extent[3])
# ring.AddPoint(extent[0],extent[2])
# poly = ogr.Geometry(ogr.wkbPolygon)
# poly.AddGeometry(ring)
#
# outShapefile = 'SHP/input_lines_extent.shp'
# outDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outShapefile):
#     outDriver.DeleteDataSource(outShapefile)
#
# outDataSource = outDriver.CreateDataSource(outShapefile)
# outLayer = outDataSource.CreateLayer('input_lines_extent', srs=inLayer.GetSpatialRef(), geom_type=ogr.wkbPolygon)
#
# idField = ogr.FieldDefn('id', ogr.OFTInteger)
# outLayer.CreateField(idField)
#
# featureDefn = outLayer.GetLayerDefn()
# feature = ogr.Feature(featureDefn)
# feature.SetGeometry(poly)
# feature.SetField('id', 1)
# outLayer.CreateFeature(feature)
# feature = None
# for feature in outLayer:
#     print(feature.GetGeometryRef().ExportToWkt())
# inDataSource = None
# outDataSource = None
#
#
#
# # Save the convex hull of all geometry from an input Layer to an output Layer
# print('Save the convex hull of all geometry from an input Layer to an output Layer:')
# inShapefile = 'SHP/input_lines.shp'
# inDriver = ogr.GetDriverByName('ESRI Shapefile')
# inDataSource = inDriver.Open(inShapefile)
# inLayer = inDataSource.GetLayer()
#
# geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
# for feature in inLayer:
#     geomcol.AddGeometry(feature.GetGeometryRef())
#
# convexhull = geomcol.ConvexHull()
#
# outShapefile = 'SHP/input_lines_convex.shp'
# outDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outShapefile):
#     outDriver.DeleteDataSource(outShapefile)
#
# outDataSource = outDriver.CreateDataSource(outShapefile)
# outLayer = outDataSource.CreateLayer('input_lines_convex', srs=inLayer.GetSpatialRef(), geom_type=ogr.wkbPolygon)
#
# idField = ogr.FieldDefn('id', ogr.OFTInteger)
# outLayer.CreateField(idField)
#
# featureDefn = outLayer.GetLayerDefn()
# feature = ogr.Feature(featureDefn)
# feature.SetGeometry(convexhull)
# feature.SetField('id', 1)
# outLayer.CreateFeature(feature)
# feature = None
# for feature in outLayer:
#     print(feature.GetGeometryRef().ExportToWkt())
# inDataSource = None
# outDataSource = None



# # Save centroids of input Layer to an output Layer
# print('Save centroids of input Layer to an output Layer:')
# inShapefile = 'SHP/input_lines.shp'
# inDriver = ogr.GetDriverByName('ESRI Shapefile')
# inDataSource = inDriver.Open(inShapefile)
# inLayer = inDataSource.GetLayer()
#
# outShapefile = 'SHP/input_lines_centroids.shp'
# outDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outShapefile):
#     outDriver.DeleteDataSource(outShapefile)
#
# outDataSource = outDriver.CreateDataSource(outShapefile)
# outLayer = outDataSource.CreateLayer('input_lines_centroids', srs=inLayer.GetSpatialRef(), geom_type=ogr.wkbPoint)
#
# inLayerDefn = inLayer.GetLayerDefn()
# for i in range(inLayerDefn.GetFieldCount()):
#     fieldDefn = inLayerDefn.GetFieldDefn(i)
#     outLayer.CreateField(fieldDefn)
#
# outLayerDefn = outLayer.GetLayerDefn()
# for (i, inFeature) in enumerate(inLayer):
#     outFeature = ogr.Feature(outLayerDefn)
#     for j in range(outLayerDefn.GetFieldCount()):
#         outFeature.SetField(outLayerDefn.GetFieldDefn(j).GetNameRef(), inFeature.GetField(j))
#     geom = inFeature.GetGeometryRef()
#     centroid = geom.Centroid()
#     outFeature.SetGeometry(centroid)
#     outLayer.CreateFeature(outFeature)
#
# for feature in outLayer:
#     print(feature.GetGeometryRef().ExportToWkt())



# # Create a New Shapefile and Add Data
# with open('volcano_data.csv', 'r') as f:
#     # https://docs.python.org/3/library/csv.html#csv.DictReader
#     reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
#
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.GetDriverByName
#     driver = ogr.GetDriverByName('ESRI Shapefile')
#
#     if os.path.exists('volcanoes.shp'):
#         # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver.DeleteDataSource
#         driver.DeleteDataSource('volcanoes.shp')
#
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver.CreateDataSource
#     data_source = driver.CreateDataSource('volcanoes.shp')
#
#     # https://gdal.org/api/python/osgeo.osr.html#osgeo.osr.SpatialReference
#     srs = osr.SpatialReference()
#     # https://gdal.org/api/python/osgeo.osr.html#osgeo.osr.SpatialReference.ImportFromEPSG
#     srs.ImportFromEPSG(4326)
#
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.DataSource.CreateLayer
#     layer = data_source.CreateLayer('volcanoes', srs, ogr.wkbPoint)
#
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.FieldDefn
#     field_name = ogr.FieldDefn('Name', ogr.OFTString)
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.FieldDefn.SetWidth
#     field_name.SetWidth(24)
#     # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.CreateField
#     layer.CreateField(field_name)
#     field_region = ogr.FieldDefn('Region', ogr.OFTString)
#     field_region.SetWidth(24)
#     layer.CreateField(field_region)
#     layer.CreateField(ogr.FieldDefn('Latitude', ogr.OFTReal))
#     layer.CreateField(ogr.FieldDefn('Longitude', ogr.OFTReal))
#     layer.CreateField(ogr.FieldDefn('Elevation', ogr.OFTInteger))
#
#     for row in reader:
#         feature = ogr.Feature(layer.GetLayerDefn())
#         for fname in row:
#             feature.SetField(fname, row[fname])
#         point = ogr.Geometry(ogr.wkbPoint)
#         point.AddPoint(float(row['Longitude']), float(row['Latitude']))
#         feature.SetGeometry(point)
#         layer.CreateFeature(feature)


# # Create a PostGIS table from WKT
# databaseServer = 'localhost'
# database = 'test'
# user = 's.osokin'
# pw = 'Stepanadze'
# table = 'test'
# dbPort = '5432'
#
# wkt = 'POINT (1120351.5712494177 741921.4223245403)'
# point = ogr.CreateGeometryFromWkt(wkt)
# cString = f'PG: host={databaseServer} dbname={database} user={user} password={pw} port={dbPort}'
# ogrds = ogr.Open(cString)
#
# srs = osr.SpatialReference()
# srs.ImportFromEPSG(4326)
#
# layer = ogrds.CreateLayer(table, srs, ogr.wkbPoint, ['OVERWRITE=YES'])
#
# layerdefn = layer.GetLayerDefn()
#
# feature = ogr.Feature(layerdefn)
# feature.SetGeometry(point)
# layer.StartTransaction()
# layer.CreateFeature(feature)
# feature = None
# layer.CommitTransaction()




# # Filter and Select Input Shapefile to New Output Shapefile Like ogr2ogr CLI
# inShapefile = 'SHP/bnd-political-boundary-a.shp'
# inDriver = ogr.GetDriverByName('ESRI Shapefile')
# inDataSource = inDriver.Open(inShapefile, 0)
# inLayer = inDataSource.GetLayer()
# inLayer.SetAttributeFilter("NA2_DESCRI = 'France'")
#
# outShapefile = 'SHP/ogr_api_filter.shp'
# outDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outShapefile):
#     outDriver.DeleteDataSource(outShapefile)
#
# outDataSource = outDriver.CreateDataSource(outShapefile)
# out_lyr_name = 'ogr_api_filter'
# outLayer = outDataSource.CreateLayer(out_lyr_name, srs=inLayer.GetSpatialRef(), geom_type=ogr.wkbMultiPolygon)
#
# inLayerDefn = inLayer.GetLayerDefn()
# for i in range(inLayerDefn.GetFieldCount()):
#     fieldDefn = inLayerDefn.GetFieldDefn(i)
#     fieldName = fieldDefn.GetName()
#     # if fieldName not in field_name_target:
#     #     continue
#     outLayer.CreateField(fieldDefn)
#
# outLayerDefn = outLayer.GetLayerDefn()
#
# for inFeature in inLayer:
#     outFeature = ogr.Feature(outLayerDefn)
#     for i in range(outLayerDefn.GetFieldCount()):
#         fieldDefn = outLayerDefn.GetFieldDefn(i)
#         fieldName = fieldDefn.GetName()
#         outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
#     geom = inFeature.GetGeometryRef()
#     outFeature.SetGeometry(geom.Clone())
#     outLayer.CreateFeature(outFeature)
#     # outFeature = None
#
# inDataSource = None
# outDataSource = None



# # Merge OGR Layers
# outputMergefn = 'SHP/merge.shp'
# directory = 'D:/PROG/QGIS/gdal_ogr/SHP/'
# fileStartsWith = 'test'
# fileEndsWith = '.shp'
# driverName = 'ESRI Shapefile'
# geometryType = ogr.wkbPolygon
#
# out_driver = ogr.GetDriverByName(driverName)
# if os.path.exists(outputMergefn):
#     out_driver.DeleteDataSource(outputMergefn)
# out_ds = out_driver.CreateDataSource(outputMergefn)
# wgs84 = osr.SpatialReference()
# wgs84.ImportFromEPSG(4326)
# out_layer = out_ds.CreateLayer(outputMergefn.replace('SHP/', ''), srs=wgs84, geom_type=geometryType)
#
# filelist = os.listdir(directory)
#
# for file in filelist:
#     if file.startswith(fileStartsWith) and file.endswith(fileEndsWith):
#         print(file)
#         ds = ogr.Open(directory + file)
#         lyr = ds.GetLayer()
#         for feat in lyr:
#             out_feat = ogr.Feature(out_layer.GetLayerDefn())
#             out_feat.SetGeometry(feat.GetGeometryRef().Clone())
#             out_layer.CreateFeature(out_feat)
#             # out_feat = None
#             # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer.SyncToDisk
#             out_layer.SyncToDisk()



# # Create fishnet grid
# outputGridFn = 'SHP/grid.shp'
# xmin = 992325.66
# xmax = 1484723.41
# ymin = 494849.32
# ymax = 781786.14
# gridWidth = 10000
# gridHeight = 10000
#
# rows = ceil((ymax-ymin)/gridHeight)
# cols = ceil((xmax - xmin) / gridWidth)
#
# ringXleftOrigin = xmin
# ringXrightOrigin = xmin + gridWidth
# ringYtopOrigin = ymax
# ringYbottomOrigin = ymax - gridHeight
#
# outDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outputGridFn):
#     outDriver.DeleteDataSource(outputGridFn)
# outputDataSource = outDriver.CreateDataSource(outputGridFn)
# merc = osr.SpatialReference()
# merc.ImportFromEPSG(3857)
# outLayer = outputDataSource.CreateLayer(outputGridFn, srs=merc, geom_type=ogr.wkbPolygon)
# featureDefn = outLayer.GetLayerDefn()
#
# countcols = 0
# while countcols < cols:
#     countcols += 1
#
#     ringYtop = ringYtopOrigin
#     ringYbottom = ringYbottomOrigin
#     countrows = 0
#
#     while countrows < rows:
#         countrows += 1
#         ring = ogr.Geometry(ogr.wkbLinearRing)
#         ring.AddPoint(ringXleftOrigin, ringYtop)
#         ring.AddPoint(ringXrightOrigin, ringYtop)
#         ring.AddPoint(ringXrightOrigin, ringYbottom)
#         ring.AddPoint(ringXleftOrigin, ringYbottom)
#         ring.AddPoint(ringXleftOrigin, ringYtop)
#         poly = ogr.Geometry(ogr.wkbPolygon)
#         poly.AddGeometry(ring)
#
#         outFeature = ogr.Feature(featureDefn)
#         outFeature.SetGeometry(poly)
#         outLayer.CreateFeature(outFeature)
#
#         ringYtop = ringYtop - gridHeight
#         ringYbottom = ringYbottom - gridHeight
#
#     ringXleftOrigin += gridWidth
#     ringXrightOrigin += gridWidth



# # Convert polygon shapefile to line shapefile
# input_poly = 'SHP/polygon.shp'
# output_line = 'SHP/line.shp'
#
# source_ds = ogr.Open(input_poly)
# source_layer = source_ds.GetLayer()
#
# geom_col = ogr.Geometry(ogr.wkbGeometryCollection)
# for feat in source_layer:
#     geom = feat.GetGeometryRef()
#     ring = geom.GetGeometryRef(0)
#     geom_col.AddGeometry(ring)
#
# driver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(output_line):
#     driver.DeleteDataSource(output_line)
# output_ds = driver.CreateDataSource(output_line)
# i_srs = source_layer.GetSpatialRef()
#
# output_layer = output_ds.CreateLayer(output_line.replace('SHP/', ''), srs=i_srs, geom_type=ogr.wkbMultiLineString)
# featureDefn = output_layer.GetLayerDefn()
# out_feature = ogr.Feature(featureDefn)
# out_feature.SetGeometry(geom_col)
# output_layer.CreateFeature(out_feature)



# # Create point shapefile with attribute data
# pointCoord = -124.4577,48.0135
# fieldName = 'test'
# fieldType = ogr.OFTString
# fieldValue = 'test'
# outSHPfn = 'test_field.shp'
#
# driver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(f'SHP/{outSHPfn}'):
#     driver.DeleteDataSource(f'SHP/{outSHPfn}')
# out_ds = driver.CreateDataSource(f'SHP/{outSHPfn}')
# o_srs = osr.SpatialReference()
# o_srs.ImportFromEPSG(4326)
# out_layer = out_ds.CreateLayer(outSHPfn, srs=o_srs, geom_type=ogr.wkbPoint)
#
# idField = ogr.FieldDefn(fieldName, fieldType)
# out_layer.CreateField(idField)
#
# geom = ogr.Geometry(ogr.wkbPoint)
# geom.AddPoint(*pointCoord)
#
# featureDefn = out_layer.GetLayerDefn()
# feat = ogr.Feature(featureDefn)
# feat.SetGeometry(geom)
# feat.SetField(fieldName, fieldValue)
# out_layer.CreateFeature(feat)



# # Create buffer
# inputfn = 'SHP/input_lines.shp'
# outputBufferfn = 'SHP/output_buffer.shp'
# bufferDist = 1000
#
# inputds = ogr.Open(inputfn)
# inputlyr = inputds.GetLayer()
#
# outdriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(outputBufferfn):
#     outdriver.DeleteDataSource(outputBufferfn)
# out_ds = outdriver.CreateDataSource(outputBufferfn)
# i_srs = inputlyr.GetSpatialRef()
# out_lyr = out_ds.CreateLayer(outputBufferfn.replace('SHP/', ''), srs=i_srs, geom_type=ogr.wkbPolygon)
# for i_feature in inputlyr:
#     i_geom = i_feature.GetGeometryRef()
#     b_geom = i_geom.Buffer(bufferDist)
#     featureDef = out_lyr.GetLayerDefn()
#     o_feature = ogr.Feature(featureDef)
#     o_feature.SetGeometry(b_geom)
#     out_lyr.CreateFeature(o_feature)



# # Convert vector layer to array
# vector_fn = 'SHP/test_array.shp'
# pixel_size = 3000
# NoData_value = 255
#
# source_ds = ogr.Open(vector_fn)
# source_layer = source_ds.GetLayer()
# source_srs = source_layer.GetSpatialRef()
# x_min, x_max, y_min, y_max = source_layer.GetExtent()
#
# x_res = int((x_max - x_min) / pixel_size)
# y_res = int((y_max - y_min) / pixel_size)
#
# # https://gdal.org/drivers/raster/mem.html#raster-mem
# # https://gdal.org/api/gdaldriver_cpp.html#_CPPv4N10GDALDriver6CreateEPKciii12GDALDataType12CSLConstList
# target_ds = gdal.GetDriverByName('MEM').Create('', x_res, y_res, gdal.GDT_Byte)
#
# # https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.Dataset.SetGeoTransform
# # https://stackoverflow.com/questions/27166739/description-of-parameters-of-gdal-setgeotransform
# # https://gdal.org/tutorials/geotransforms_tut.html
# target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
#
# band = target_ds.GetRasterBand(1)
#
# band.SetNoDataValue(NoData_value)
#
# # https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.RasterizeLayer
# gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])
#
# # https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.Band.ReadAsArray
# array = band.ReadAsArray()
#
# print(array)




# # Convert polygon to points
#
# polygon_fn = 'SHP/test_pol2pts.shp'
# out_points_fn = 'SHP/test_ptsFrompol.shp'
#
# pixel_size = 1000
#
# source_ds = ogr.Open(polygon_fn)
# source_layer = source_ds.GetLayer()
# source_srs = source_layer.GetSpatialRef()
# x_min, x_max, y_min, y_max = source_layer.GetExtent()
#
# x_res = int((x_max - x_min) / pixel_size)
# y_res = int((y_max - y_min) / pixel_size)
# # https://gdal.org/api/gdaldriver_cpp.html#_CPPv4N10GDALDriver6CreateEPKciii12GDALDataType12CSLConstList
# target_ds = gdal.GetDriverByName('GTiff').Create('temp.tif', x_res, y_res, gdal.GDT_Byte)
# # https://gdal.org/tutorials/geotransforms_tut.html
# target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
# band = target_ds.GetRasterBand(1)
# band.SetNoDataValue(255)
#
# gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])
#
# array = band.ReadAsArray()
#
# raster = gdal.Open('temp.tif')
# geotransform = raster.GetGeoTransform()
#
# count = 0
# roadList = np.where(array == 1)
# multipoint = ogr.Geometry(ogr.wkbMultiPoint)
# for indexY in roadList[0]:
#     indexX = roadList[1][count]
#     geotransform = raster.GetGeoTransform()
#     originX = geotransform[0]
#     originY = geotransform[3]
#     pixelWidth = geotransform[1]
#     pixelHeight = geotransform[5]
#     Xcoord = originX + pixelWidth * indexX
#     Ycoord = originY + pixelHeight * indexY
#     point = ogr.Geometry(ogr.wkbPoint)
#     point.AddPoint(Xcoord, Ycoord)
#     multipoint.AddGeometry(point)
#     count += 1
#
# shpDriver = ogr.GetDriverByName('ESRI Shapefile')
# if os.path.exists(out_points_fn):
#     shpDriver.DeleteDataSource(out_points_fn)
# outDataSource = shpDriver.CreateDataSource(out_points_fn)
# outLayer = outDataSource.CreateLayer(out_points_fn.replace('SHP/', ''), srs=source_srs, geom_type=ogr.wkbMultiPoint)
# featureDefn = outLayer.GetLayerDefn()
# outFeature = ogr.Feature(featureDefn)
# outFeature.SetGeometry(multipoint)
# outLayer.CreateFeature(outFeature)
# tifdriver = gdal.GetDriverByName('GTiff')
# tifdriver.Delete('temp.tif')
#
# # os.remove('temp.tif')



