from osgeo import osr, ogr

# # Create Projection
# #
# # When transforming coordinates between datums, 7 parameters must be specified:
# # dX, dY, dZ, aX, aY, aZ, m
# # which are x, y, z translation, x, y, z axis rotation and scale coefficient.
# # These parameters are applied in matrix formula, example here (Helmert method) https://en.wikipedia.org/wiki/Helmert_transformation
# #
# # there are two 7-parameters transformation methods (e.g., formulas), which differ in the sign of axis rotation angles.
# # a) Position Vector (also called Helmert) - positive rotation clockwise to the vector direction
# # b) Coordinate Frame Rotation (also called Bursa-Wolf sometimes) - positive rotation counterclockwise to the vector direction
# #
# # OSR uses Proj4 library for transformations, which supports both options, but OSR uses Position Vector always.
# #
# # So, when you have 7 transformation parameters, you must know for which method they are given.
# # If Coordinate Frame Rotation, then you must negate aX, aY and aZ to use them in osr.SpatialReference.SetTOWGS84 method
# #
# # However, if you use the osr.SpatialReference.ImportFromWkt method, you can specify the transformation method inside
# # your WKT string, and it will be automatically converted to Position Vector by OSR.
#
# # Example 1: Create Pulkovo-1942 CRS from EPSG 4284
# Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044 = osr.SpatialReference()
# Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.ImportFromEPSG(4284)
# # Currently the 7 ToWGS84 parameters of the CSR are zeros:
# print('default ToWGS84 parameters are zeros:', Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.GetTOWGS84())
# # Now we specify the ToWGS84 parameters for Position Vector method using .SetToWGS84 class method
# Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.SetTOWGS84(23.57, -140.95, -79.8, 0.0, 0.35, 0.79, -0.22)
# # now the ToWGS84 parameters are configured for Position Vector method
# print('configured ToWGS84 Position Vector parameters:', Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.GetTOWGS84())
# # now print the crs as wkt with position vector parameters
# print('CRS as WKT with position vector parameters:', Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.ExportToWkt())
# # and same in Proj4String format:
# print('CRS as Proj4String with position vector parameters:', Pulkovo_1942_EPSG4284_to_WGS_84_20_EPSG5044.ExportToProj4())
#
# # Now let's make an experiment. Russian GOST 32453-2017 specifies transformation parameters for GSK-2011
# # for Coordinate Frame Rotation method.
# # Let's specify the CRS in wkt, using the Coordinate Frame rotation method:
# wkt = """BOUNDCRS[
#     SOURCECRS[
#         GEOGCRS["GSK-2011 / GOST",
#             DATUM["GSK-2011 / GOST",
#                 ELLIPSOID["GSK-2011",6378136.5,298.2564151,
#                     LENGTHUNIT["metre",1,
#                         ID["EPSG",9001]]]],
#             PRIMEM["Greenwich",0,
#                 ANGLEUNIT["degree",0.0174532925199433],
#                 ID["EPSG",8901]],
#             CS[ellipsoidal,2],
#                 AXIS["geodetic latitude (Lat)",north,
#                     ORDER[1],
#                     ANGLEUNIT["degree",0.0174532925199433,
#                         ID["EPSG",9122]]],
#                 AXIS["geodetic longitude (Lon)",east,
#                     ORDER[2],
#                     ANGLEUNIT["degree",0.0174532925199433,
#                         ID["EPSG",9122]]]]],
#     TARGETCRS[
#         GEOGCRS["WGS 84",
#             DATUM["World Geodetic System 1984",
#                 ELLIPSOID["WGS 84",6378137,298.257223563,
#                     LENGTHUNIT["metre",1]]],
#             PRIMEM["Greenwich",0,
#                 ANGLEUNIT["degree",0.0174532925199433]],
#             CS[ellipsoidal,2],
#                 AXIS["geodetic latitude (Lat)",north,
#                     ORDER[1],
#                     ANGLEUNIT["degree",0.0174532925199433]],
#                 AXIS["geodetic longitude (Lon)",east,
#                     ORDER[2],
#                     ANGLEUNIT["degree",0.0174532925199433]],
#             ID["EPSG",4326]]],
#     ABRIDGEDTRANSFORMATION["Transformation from GSK2011 GOST to WGS84",
#         METHOD["Coordinate Frame rotation (geog2D domain)",
#             ID["EPSG",9607]],
#         PARAMETER["X-axis translation",0.013,
#             ID["EPSG",8605]],
#         PARAMETER["Y-axis translation",-0.092,
#             ID["EPSG",8606]],
#         PARAMETER["Z-axis translation",-0.03,
#             ID["EPSG",8607]],
#         PARAMETER["X-axis rotation",0.001738,
#             ID["EPSG",8608]],
#         PARAMETER["Y-axis rotation",-0.003559,
#             ID["EPSG",8609]],
#         PARAMETER["Z-axis rotation",0.004263,
#             ID["EPSG",8610]],
#         PARAMETER["Scale difference",1.0000000074,
#             ID["EPSG",8611]]]]"""
#
# # now we create new SpatialReference and import it from our WKT with GSK-2011 parameters
# GSK2011_GOST = osr.SpatialReference()
# GSK2011_GOST.ImportFromWkt(wkt)
#
# # Print GSK-2011 as wkt. We can see that parameters are automatically converted to Position Vector
# print('GSK-2011 in WKT format', GSK2011_GOST.ExportToWkt())
#
# # Now lets just print the GSK-2011 ToWGS84 parameters. We can see that they have been automatically converted to Position Vector
# print('GSK-2011 ToWGS84 parameters', GSK2011_GOST.GetTOWGS84())





# Reproject a Geometry

# The point is that when you import CRS from EPSG, Proj4 uses its metadata and chooses the best datum transformation
# according to it, also depending on the Proj version used. This overrides the parameters set by .SetTOWGS84().
# To have a 100% control of which datum transformation you are using, we can use a 'Bound CRS' which is a CRS
# without identifier, just specified by the parameters inside a projstring or wkt string.
# It is possible to create a Bound CRS using ImportFromProj4() or ImportDromWkt() methods.
# It is possible to use a trick when you first create a CRS from EPSG, and then recreate it from its
# Proj4 representation, like
# source.ImportFromEPSG(28467)
# source.ImportFromProj4(source.ExportToProj4())
# detailed info available here: https://proj.org/operations/operations_computation.html

# First let's create CRS:

# source crs imported from EPSG
source_EPSG = osr.SpatialReference()
source_EPSG.ImportFromEPSG(28467)

# source crs imported from Proj (Bound) without TOWGS84 (Ballpark)
source_Bound_Ballpark = osr.SpatialReference()
source_Bound_Ballpark.ImportFromProj4(source_EPSG.ExportToProj4())

# source crs imported from Proj (Bound) with TOWGS84 parameters from GOST 32457-2017 (same as Pulkovo 1942 to WGS 84 (20) EPSG:5044)
source_Bound_GOST = osr.SpatialReference()
source_Bound_GOST.ImportFromProj4(source_EPSG.ExportToProj4())
source_Bound_GOST.SetTOWGS84(23.57, -140.95, -79.8, 0.0, 0.35, 0.79, -0.22)

# source crs imported from Proj (Bound) with TOWGS84 parameters from Pulkovo 1942 to WGS 84 (16) EPSG:15865)
source_Bound_16_15865 = osr.SpatialReference()
source_Bound_16_15865.ImportFromProj4(source_EPSG.ExportToProj4())
source_Bound_16_15865.SetTOWGS84(25, -141, -78.5, 0, 0.35, 0.736)

# target CRS which is EPSG:4326 WGS-1984
target_EPSG = osr.SpatialReference()
target_EPSG.ImportFromEPSG(4326)

# Now let's print the crs info
print()
print('source_EPSG:', source_EPSG.GetName())
print('source_Bound_Ballpark:', source_Bound_Ballpark.ExportToProj4())
print('source_Bound_GOST:', source_Bound_GOST.ExportToProj4())
print('source_Bound_16_15865:', source_Bound_16_15865.ExportToProj4())
print('target_EPSG:', target_EPSG.GetName())

# Now we create transformation objects for each source CRS
transform_epsg_to_epsg = osr.CoordinateTransformation(source_EPSG, target_EPSG)
transform_bound_ballpark_to_epsg = osr.CoordinateTransformation(source_Bound_Ballpark, target_EPSG)
transform_bound_gost_to_epsg = osr.CoordinateTransformation(source_Bound_GOST, target_EPSG)
transform_bound_15865_to_epsg = osr.CoordinateTransformation(source_Bound_16_15865, target_EPSG)

# Now we create a source point for each of 3 transformations
# EPSG:28467 stores northing first and easting second, which can be checked by EPSGTreatsAsNorthingEasting()
point_yx_epsg_to_epsg = ogr.CreateGeometryFromWkt("POINT (6122289.252252 443731.993780)")
point_xy_bound_ballpark_to_epsg = ogr.CreateGeometryFromWkt("POINT (443731.993780 6122289.252252)")
point_xy_bound_gost_to_epsg = ogr.CreateGeometryFromWkt("POINT (443731.993780 6122289.252252)")
point_xy_bound_15865_to_epsg = ogr.CreateGeometryFromWkt("POINT (443731.993780 6122289.252252)")

# print the coordinates of the point before transformation
print('Point before transformation:', '\t\t\t\t\t', point_xy_bound_ballpark_to_epsg.ExportToWkt())

# make transformations
point_yx_epsg_to_epsg.Transform(transform_epsg_to_epsg)
point_xy_bound_ballpark_to_epsg.Transform(transform_bound_ballpark_to_epsg)
point_xy_bound_gost_to_epsg.Transform(transform_bound_gost_to_epsg)
point_xy_bound_15865_to_epsg.Transform(transform_bound_15865_to_epsg)

# print the transformed points coordinates
print('Point after transformation selected by EPSG:', '\t', point_yx_epsg_to_epsg.ExportToWkt())
print('Point after Ballpark transformation:', '\t\t\t', point_xy_bound_ballpark_to_epsg.ExportToWkt())
print('Point after Bound GOST transformation:', '\t\t\t', point_xy_bound_gost_to_epsg.ExportToWkt())
print('Point after Bound EPSG:15865 transformation:', '\t', point_xy_bound_15865_to_epsg.ExportToWkt())

if point_yx_epsg_to_epsg.ExportToWkt() == point_xy_bound_gost_to_epsg.ExportToWkt():
    print('we can see that EPSG and Bound GOST transformations give the same result,')
    print('which means that Proj has chosen GOST automatically using EPSG metadata')
print()


