# https://pcjericks.github.io/py-gdalogr-cookbook/gdal_general.html
# https://gdal.org/api/python/osgeo.ogr.html


# Imports python GDAL and exits the program if the modules are not found.
import sys
try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERRER: cannot find GDAL/OGR modules')


# This code checks the version of the GDAL/OGR on the imported module
version_num = int(gdal.VersionInfo('VERSION_NUM'))
#print(version_num)

# Enable GDAL/OGR exceptions
gdal.UseExceptions()
# open dataset that does not exist
#ds = gdal.Open('test.tif')
#gdal.DontUseExceptions()


## example GDAL error handler function
# def gdal_error_handler(err_class, err_num, err_msg):
#     errtype = {
#             gdal.CE_None:'None',
#             gdal.CE_Debug:'Debug',
#             gdal.CE_Warning:'Warning',
#             gdal.CE_Failure:'Failure',
#             gdal.CE_Fatal:'Fatal'
#     }
#     err_msg = err_msg.replace('\n',' ')
#     err_class = errtype.get(err_class, 'None')
#     print('Error Number: %s' % (err_num))
#     print('Error Type: %s' % (err_class))
#     print('Error Message: %s' % (err_msg))
#
# if __name__=='__main__':
#
#     # install error handler
#     gdal.PushErrorHandler(gdal_error_handler)
#
#     # Raise a dummy error
#     gdal.Error(1, 2, 'test error')
#
#     #uninstall error handler
#     gdal.PopErrorHandler()