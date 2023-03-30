from osgeo import ogr
from osgeo import osr
import os

# from https://gis.stackexchange.com/questions/122736/making-buffer-from-line-using-gdal-and-python
def create_buffer(inputf='SHP/input_lines.shp', outputf='SHP/output_buffer.shp', bufferDist=1000.0):

    # create an osgeo.ogr.DataSource object
    inputds = ogr.Open(inputf)

    # create a layer from datasource
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.DataSource
    inputlr = inputds.GetLayer()

    # create driver oblect by its name. list of drivers: https://gdal.org/drivers/vector/index.html
    shpdriver = ogr.GetDriverByName('ESRI Shapefile')

    # delete the output file if it already exists
    if os.path.exists(outputf):
        # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver
        shpdriver.DeleteDataSource(outputf)

    # create output datasource
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Driver
    outputBufferds = shpdriver.CreateDataSource(outputf)

    # create layer from the output datasource object
    # create a spatial reference object and set it's crs from EPSG
    # https://gdal.org/api/python/osgeo.osr.html#osgeo.osr.SpatialReference
    dest_srs = ogr.osr.SpatialReference()
    dest_srs.ImportFromEPSG(32643)
    # or get a spatial reference object from the input layer
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer
    dest_srs = inputlr.GetSpatialRef()
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.DataSource
    bufferlyr = outputBufferds.CreateLayer(outputf, srs=dest_srs, geom_type=ogr.wkbPolygon)

    # create the feature definition object from the layer object
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer
    # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.FeatureDefn
    feature_defn = bufferlyr.GetLayerDefn()

    # loop through the features in the input layer
    for feature in inputlr:

        # get feature's geometry
        # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer
        # returns a Geometry object https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Geometry
        cur_in_geom = feature.GetGeometryRef()

        # build a buffer from current input geometry
        cur_buf_geom = cur_in_geom.Buffer(bufferDist, quadsecs=50)

        # create an output feature
        # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Feature
        # check the infostring to understand the arguments
        cur_buf_f = ogr.Feature(feature_defn)
        # set the geometry for the new feature
        cur_buf_f.SetGeometry(cur_buf_geom)
        # add the current buffer feature to the output layer
        # https://gdal.org/api/python/osgeo.ogr.html#osgeo.ogr.Layer
        bufferlyr.CreateFeature(cur_buf_f)


create_buffer(bufferDist=2000.0)
