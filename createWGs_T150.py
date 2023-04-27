# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

centreOfObj = 5.8555

# INPUT OF WAVE GAUGES
location_waveGauge1 = [centreOfObj - 1, 0, 0.05]
location_waveGauge2 = [centreOfObj - 0.3333333333, 0, 0.05]
location_waveGauge3 = [centreOfObj + 0.3333333333, 0, 0.05]
location_waveGauge4 = [centreOfObj + 1, 0, 0.05]

# Get the current working directory
cwd = os.getcwd()

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = 'output'
filename = 'case.foam'

path = os.path.join(script_dir,filename)

# Create OpenFOAMReader with the selected file
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=path)

casefoam.MeshRegions = ['internalMesh', 'group/empty', 'group/wall', 'patch/inlet', 'patch/bottom', 'patch/outlet', 'patch/atmosphere', 'patch/frontBack', 'patch/floatingObject']
casefoam.CellArrays = ['U', 'alpha.water', 'p', 'p_rgh', 'rAU']
casefoam.PointArrays = ['pointDisplacement']

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# Properties modified on casefoam
# casefoam.CaseType = 'Decomposed Case'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get the material library
materialLibrary1 = GetMaterialLibrary()

# get display properties
casefoamDisplay = GetDisplayProperties(casefoam, view=renderView1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

##############################################################################################################
##############################################################################################################

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=casefoam)
contour1.ContourBy = ['POINTS', 'p']
contour1.Isosurfaces = [1494.7734800577164]
contour1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'p']
contour1Display.LookupTable = pLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'p'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'U'
contour1Display.ScaleFactor = 1.1711000442504884
contour1Display.SelectScaleArray = 'p'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'p'
contour1Display.GaussianRadius = 0.05855500221252442
contour1Display.SetScaleArray = ['POINTS', 'p']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'p']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.SelectInputVectors = ['POINTS', 'U']
contour1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=contour1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'alphawater'
alphawaterLUT = GetColorTransferFunction('alphawater')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = ['POINTS', 'alpha.water']
extractSurface1Display.LookupTable = alphawaterLUT
extractSurface1Display.SelectTCoordArray = 'None'
extractSurface1Display.SelectNormalArray = 'None'
extractSurface1Display.SelectTangentArray = 'None'
extractSurface1Display.OSPRayScaleArray = 'alpha.water'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'U'
extractSurface1Display.ScaleFactor = 1.1711000442504884
extractSurface1Display.SelectScaleArray = 'alpha.water'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'alpha.water'
extractSurface1Display.GaussianRadius = 0.05855500221252442
extractSurface1Display.SetScaleArray = ['POINTS', 'alpha.water']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'alpha.water']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface1Display.SelectInputVectors = ['POINTS', 'U']
extractSurface1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=extractSurface1)
calculator1.Function = ''

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'alpha.water']
calculator1Display.LookupTable = alphawaterLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'alpha.water'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 1.1711000442504884
calculator1Display.SelectScaleArray = 'alpha.water'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'alpha.water'
calculator1Display.GaussianRadius = 0.05855500221252442
calculator1Display.SetScaleArray = ['POINTS', 'alpha.water']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'alpha.water']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.SelectInputVectors = ['POINTS', 'U']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=calculator1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = location_waveGauge1

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = location_waveGauge1

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.HyperTreeGridSlicer)

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = -2.0000000000000002e+298
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = -1e+297
slice1Display.SetScaleArray = [None, '']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = [None, '']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = [None, '']
slice1Display.WriteLog = ''

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(casefoam)

##############################################################################################################
##############################################################################################################

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=casefoam)
contour2.ContourBy = ['POINTS', 'p']
contour2.Isosurfaces = [1494.7734800577164]
contour2.PointMergeMethod = 'Uniform Binning'

# show data in view
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'p']
contour2Display.LookupTable = pLUT
contour2Display.SelectTCoordArray = 'None'
contour2Display.SelectNormalArray = 'None'
contour2Display.SelectTangentArray = 'None'
contour2Display.OSPRayScaleArray = 'p'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'U'
contour2Display.ScaleFactor = 1.1711000442504884
contour2Display.SelectScaleArray = 'p'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'p'
contour2Display.GaussianRadius = 0.05855500221252442
contour2Display.SetScaleArray = ['POINTS', 'p']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'p']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'
contour2Display.SelectInputVectors = ['POINTS', 'U']
contour2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=contour2)

# show data in view
extractSurface2Display = Show(extractSurface2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface2Display.Representation = 'Surface'
extractSurface2Display.ColorArrayName = ['POINTS', 'alpha.water']
extractSurface2Display.LookupTable = alphawaterLUT
extractSurface2Display.SelectTCoordArray = 'None'
extractSurface2Display.SelectNormalArray = 'None'
extractSurface2Display.SelectTangentArray = 'None'
extractSurface2Display.OSPRayScaleArray = 'alpha.water'
extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface2Display.SelectOrientationVectors = 'U'
extractSurface2Display.ScaleFactor = 1.1711000442504884
extractSurface2Display.SelectScaleArray = 'alpha.water'
extractSurface2Display.GlyphType = 'Arrow'
extractSurface2Display.GlyphTableIndexArray = 'alpha.water'
extractSurface2Display.GaussianRadius = 0.05855500221252442
extractSurface2Display.SetScaleArray = ['POINTS', 'alpha.water']
extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface2Display.OpacityArray = ['POINTS', 'alpha.water']
extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface2Display.SelectInputVectors = ['POINTS', 'U']
extractSurface2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface2Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface2Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour2, renderView1)

# show color bar/color legend
extractSurface2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=extractSurface2)
calculator2.Function = ''

# show data in view
calculator2Display = Show(calculator2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'alpha.water']
calculator2Display.LookupTable = alphawaterLUT
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'alpha.water'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'U'
calculator2Display.ScaleFactor = 1.1711000442504884
calculator2Display.SelectScaleArray = 'alpha.water'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'alpha.water'
calculator2Display.GaussianRadius = 0.05855500221252442
calculator2Display.SetScaleArray = ['POINTS', 'alpha.water']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'alpha.water']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.SelectInputVectors = ['POINTS', 'U']
calculator2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface2, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=calculator2)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = location_waveGauge2

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = location_waveGauge2

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice2.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice2.HyperTreeGridSlicer)

# show data in view
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = [None, '']
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = -2.0000000000000002e+298
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = -1e+297
slice2Display.SetScaleArray = [None, '']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = [None, '']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.SelectInputVectors = [None, '']
slice2Display.WriteLog = ''

# hide data in view
Hide(calculator2, renderView1)

##############################################################################################################
##############################################################################################################

# create a new 'Contour'
contour3 = Contour(registrationName='Contour3', Input=casefoam)
contour3.ContourBy = ['POINTS', 'p']
contour3.Isosurfaces = [1494.7734800577164]
contour3.PointMergeMethod = 'Uniform Binning'

# show data in view
contour3Display = Show(contour3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour3Display.Representation = 'Surface'
contour3Display.ColorArrayName = ['POINTS', 'p']
contour3Display.LookupTable = pLUT
contour3Display.SelectTCoordArray = 'None'
contour3Display.SelectNormalArray = 'None'
contour3Display.SelectTangentArray = 'None'
contour3Display.OSPRayScaleArray = 'p'
contour3Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour3Display.SelectOrientationVectors = 'U'
contour3Display.ScaleFactor = 1.1711000442504884
contour3Display.SelectScaleArray = 'p'
contour3Display.GlyphType = 'Arrow'
contour3Display.GlyphTableIndexArray = 'p'
contour3Display.GaussianRadius = 0.05855500221252442
contour3Display.SetScaleArray = ['POINTS', 'p']
contour3Display.ScaleTransferFunction = 'PiecewiseFunction'
contour3Display.OpacityArray = ['POINTS', 'p']
contour3Display.OpacityTransferFunction = 'PiecewiseFunction'
contour3Display.DataAxesGrid = 'GridAxesRepresentation'
contour3Display.PolarAxes = 'PolarAxesRepresentation'
contour3Display.SelectInputVectors = ['POINTS', 'U']
contour3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour3Display.ScaleTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour3Display.OpacityTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
contour3Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(registrationName='ExtractSurface3', Input=contour3)

# show data in view
extractSurface3Display = Show(extractSurface3, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'alphawater'
alphawaterLUT = GetColorTransferFunction('alphawater')

# trace defaults for the display properties.
extractSurface3Display.Representation = 'Surface'
extractSurface3Display.ColorArrayName = ['POINTS', 'alpha.water']
extractSurface3Display.LookupTable = alphawaterLUT
extractSurface3Display.SelectTCoordArray = 'None'
extractSurface3Display.SelectNormalArray = 'None'
extractSurface3Display.SelectTangentArray = 'None'
extractSurface3Display.OSPRayScaleArray = 'alpha.water'
extractSurface3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface3Display.SelectOrientationVectors = 'U'
extractSurface3Display.ScaleFactor = 1.1711000442504884
extractSurface3Display.SelectScaleArray = 'alpha.water'
extractSurface3Display.GlyphType = 'Arrow'
extractSurface3Display.GlyphTableIndexArray = 'alpha.water'
extractSurface3Display.GaussianRadius = 0.05855500221252442
extractSurface3Display.SetScaleArray = ['POINTS', 'alpha.water']
extractSurface3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface3Display.OpacityArray = ['POINTS', 'alpha.water']
extractSurface3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface3Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface3Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface3Display.SelectInputVectors = ['POINTS', 'U']
extractSurface3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface3Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface3Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
extractSurface3Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=extractSurface3)
calculator3.Function = ''

# show data in view
calculator3Display = Show(calculator3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'alpha.water']
calculator3Display.LookupTable = alphawaterLUT
calculator3Display.SelectTCoordArray = 'None'
calculator3Display.SelectNormalArray = 'None'
calculator3Display.SelectTangentArray = 'None'
calculator3Display.OSPRayScaleArray = 'alpha.water'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'U'
calculator3Display.ScaleFactor = 1.1711000442504884
calculator3Display.SelectScaleArray = 'alpha.water'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'alpha.water'
calculator3Display.GaussianRadius = 0.05855500221252442
calculator3Display.SetScaleArray = ['POINTS', 'alpha.water']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'alpha.water']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.SelectInputVectors = ['POINTS', 'U']
calculator3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=calculator3)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = location_waveGauge3

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = location_waveGauge3

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice3.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice3.HyperTreeGridSlicer)

# show data in view
slice3Display = Show(slice3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = [None, '']
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.ScaleFactor = -2.0000000000000002e+298
slice3Display.SelectScaleArray = 'None'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'None'
slice3Display.GaussianRadius = -1e+297
slice3Display.SetScaleArray = [None, '']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = [None, '']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'
slice3Display.SelectInputVectors = [None, '']
slice3Display.WriteLog = ''

# hide data in view
Hide(calculator3, renderView1)

# set active source
SetActiveSource(casefoam)

##############################################################################################################
##############################################################################################################

# create a new 'Contour'
contour4 = Contour(registrationName='Contour4', Input=casefoam)
contour4.ContourBy = ['POINTS', 'p']
contour4.Isosurfaces = [1494.7734800577164]
contour4.PointMergeMethod = 'Uniform Binning'

# show data in view
contour4Display = Show(contour4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour4Display.Representation = 'Surface'
contour4Display.ColorArrayName = ['POINTS', 'p']
contour4Display.LookupTable = pLUT
contour4Display.SelectTCoordArray = 'None'
contour4Display.SelectNormalArray = 'None'
contour4Display.SelectTangentArray = 'None'
contour4Display.OSPRayScaleArray = 'p'
contour4Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour4Display.SelectOrientationVectors = 'U'
contour4Display.ScaleFactor = 1.1711000442504884
contour4Display.SelectScaleArray = 'p'
contour4Display.GlyphType = 'Arrow'
contour4Display.GlyphTableIndexArray = 'p'
contour4Display.GaussianRadius = 0.05855500221252442
contour4Display.SetScaleArray = ['POINTS', 'p']
contour4Display.ScaleTransferFunction = 'PiecewiseFunction'
contour4Display.OpacityArray = ['POINTS', 'p']
contour4Display.OpacityTransferFunction = 'PiecewiseFunction'
contour4Display.DataAxesGrid = 'GridAxesRepresentation'
contour4Display.PolarAxes = 'PolarAxesRepresentation'
contour4Display.SelectInputVectors = ['POINTS', 'U']
contour4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour4Display.ScaleTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour4Display.OpacityTransferFunction.Points = [1491.0933837890625, 0.0, 0.5, 0.0, 1491.3433837890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
contour4Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(registrationName='ExtractSurface4', Input=contour4)

# show data in view
extractSurface4Display = Show(extractSurface4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface4Display.Representation = 'Surface'
extractSurface4Display.ColorArrayName = ['POINTS', 'alpha.water']
extractSurface4Display.LookupTable = alphawaterLUT
extractSurface4Display.SelectTCoordArray = 'None'
extractSurface4Display.SelectNormalArray = 'None'
extractSurface4Display.SelectTangentArray = 'None'
extractSurface4Display.OSPRayScaleArray = 'alpha.water'
extractSurface4Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface4Display.SelectOrientationVectors = 'U'
extractSurface4Display.ScaleFactor = 1.1711000442504884
extractSurface4Display.SelectScaleArray = 'alpha.water'
extractSurface4Display.GlyphType = 'Arrow'
extractSurface4Display.GlyphTableIndexArray = 'alpha.water'
extractSurface4Display.GaussianRadius = 0.05855500221252442
extractSurface4Display.SetScaleArray = ['POINTS', 'alpha.water']
extractSurface4Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface4Display.OpacityArray = ['POINTS', 'alpha.water']
extractSurface4Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface4Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface4Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface4Display.SelectInputVectors = ['POINTS', 'U']
extractSurface4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface4Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface4Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour4, renderView1)

# show color bar/color legend
extractSurface4Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=extractSurface4)
calculator4.Function = ''

# show data in view
calculator4Display = Show(calculator4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = ['POINTS', 'alpha.water']
calculator4Display.LookupTable = alphawaterLUT
calculator4Display.SelectTCoordArray = 'None'
calculator4Display.SelectNormalArray = 'None'
calculator4Display.SelectTangentArray = 'None'
calculator4Display.OSPRayScaleArray = 'alpha.water'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'U'
calculator4Display.ScaleFactor = 1.1711000442504884
calculator4Display.SelectScaleArray = 'alpha.water'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'alpha.water'
calculator4Display.GaussianRadius = 0.05855500221252442
calculator4Display.SetScaleArray = ['POINTS', 'alpha.water']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'alpha.water']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'
calculator4Display.SelectInputVectors = ['POINTS', 'U']
calculator4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface4, renderView1)

# show color bar/color legend
calculator4Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice4 = Slice(registrationName='Slice4', Input=calculator4)
slice4.SliceType = 'Plane'
slice4.HyperTreeGridSlicer = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = location_waveGauge4

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice4.HyperTreeGridSlicer.Origin = location_waveGauge4

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice4.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice4.HyperTreeGridSlicer)

# show data in view
slice4Display = Show(slice4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice4Display.Representation = 'Surface'
slice4Display.ColorArrayName = [None, '']
slice4Display.SelectTCoordArray = 'None'
slice4Display.SelectNormalArray = 'None'
slice4Display.SelectTangentArray = 'None'
slice4Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice4Display.SelectOrientationVectors = 'None'
slice4Display.ScaleFactor = -2.0000000000000002e+298
slice4Display.SelectScaleArray = 'None'
slice4Display.GlyphType = 'Arrow'
slice4Display.GlyphTableIndexArray = 'None'
slice4Display.GaussianRadius = -1e+297
slice4Display.SetScaleArray = [None, '']
slice4Display.ScaleTransferFunction = 'PiecewiseFunction'
slice4Display.OpacityArray = [None, '']
slice4Display.OpacityTransferFunction = 'PiecewiseFunction'
slice4Display.DataAxesGrid = 'GridAxesRepresentation'
slice4Display.PolarAxes = 'PolarAxesRepresentation'
slice4Display.SelectInputVectors = [None, '']
slice4Display.WriteLog = ''

# hide data in view
Hide(calculator4, renderView1)

##############################################################################################################
##############################################################################################################

# set active source
SetActiveSource(slice1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice4.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = location_waveGauge1

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice2)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice2.SliceType)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = location_waveGauge2

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice3)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice2.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice3.SliceType)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = location_waveGauge3

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice4)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice3.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice4.SliceType)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice4.SliceType
slice4.SliceType.Origin = location_waveGauge4

# update the view to ensure updated data information
renderView1.Update()

##############################################################################################################
##############################################################################################################

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
slice1Display_1 = Show(slice1, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# set active source
SetActiveSource(slice1)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime1 = PlotDataOverTime(registrationName='PlotDataOverTime1', Input=slice1)

# Create a new 'Quartile Chart View'
quartileChartView1 = CreateView('QuartileChartView')

# show data in view
plotDataOverTime1Display = Show(plotDataOverTime1, quartileChartView1, 'QuartileChartRepresentation')

# trace defaults for the display properties.
plotDataOverTime1Display.AttributeType = 'Row Data'
plotDataOverTime1Display.UseIndexForXAxis = 0
plotDataOverTime1Display.XArrayName = 'Time'
plotDataOverTime1Display.SeriesVisibility = ['alpha.water ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'U (Magnitude) ( block=1)']
plotDataOverTime1Display.SeriesLabel = ['alpha.water ( block=1)', 'alpha.water ( block=1)', 'Normals (0) ( block=1)', 'Normals (0) ( block=1)', 'Normals (1) ( block=1)', 'Normals (1) ( block=1)', 'Normals (2) ( block=1)', 'Normals (2) ( block=1)', 'Normals (Magnitude) ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'Result ( block=1)', 'U (0) ( block=1)', 'U (0) ( block=1)', 'U (1) ( block=1)', 'U (1) ( block=1)', 'U (2) ( block=1)', 'U (2) ( block=1)', 'U (Magnitude) ( block=1)', 'U (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
plotDataOverTime1Display.SeriesColor = ['alpha.water ( block=1)', '0', '0', '0', 'Normals (0) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Normals (1) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Normals (2) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Normals (Magnitude) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'pointDisplacement (0) ( block=1)', '0', '0', '0', 'pointDisplacement (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'pointDisplacement (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'pointDisplacement (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'rAU ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Result ( block=1)', '1', '0.5000076295109483', '0', 'U (0) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U (1) ( block=1)', '0', '0', '0', 'U (2) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U (Magnitude) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'X ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Y ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Z ( block=1)', '1', '0.5000076295109483', '0', 'N ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Time ( block=1)', '0', '0', '0', 'vtkValidPointMask ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotDataOverTime1Display.SeriesOpacity = ['alpha.water ( block=1)', '1.0', 'Normals (0) ( block=1)', '1.0', 'Normals (1) ( block=1)', '1.0', 'Normals (2) ( block=1)', '1.0', 'Normals (Magnitude) ( block=1)', '1.0', 'p ( block=1)', '1.0', 'p_rgh ( block=1)', '1.0', 'pointDisplacement (0) ( block=1)', '1.0', 'pointDisplacement (1) ( block=1)', '1.0', 'pointDisplacement (2) ( block=1)', '1.0', 'pointDisplacement (Magnitude) ( block=1)', '1.0', 'rAU ( block=1)', '1.0', 'Result ( block=1)', '1.0', 'U (0) ( block=1)', '1.0', 'U (1) ( block=1)', '1.0', 'U (2) ( block=1)', '1.0', 'U (Magnitude) ( block=1)', '1.0', 'X ( block=1)', '1.0', 'Y ( block=1)', '1.0', 'Z ( block=1)', '1.0', 'N ( block=1)', '1.0', 'Time ( block=1)', '1.0', 'vtkValidPointMask ( block=1)', '1.0']
plotDataOverTime1Display.SeriesPlotCorner = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesLabelPrefix = ''
plotDataOverTime1Display.SeriesLineStyle = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime1Display.SeriesLineThickness = ['alpha.water ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'Result ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime1Display.SeriesMarkerStyle = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesMarkerSize = ['alpha.water ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'Result ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=quartileChartView1, layout=layout1, hint=2)

# Properties modified on plotDataOverTime1Display
plotDataOverTime1Display.SeriesOpacity = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime1Display.SeriesPlotCorner = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesLineStyle = ['N ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'Result ( block=1)', '1', 'Time ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.water ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime1Display.SeriesLineThickness = ['N ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'Result ( block=1)', '2', 'Time ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.water ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime1Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime1Display.SeriesMarkerSize = ['N ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'Result ( block=1)', '4', 'Time ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.water ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# update the view to ensure updated data information
quartileChartView1.Update()

# set active source
SetActiveSource(slice2)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice2.SliceType)

# update the view to ensure updated data information
quartileChartView1.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime2 = PlotDataOverTime(registrationName='PlotDataOverTime2', Input=slice2)

# show data in view
plotDataOverTime2Display = Show(plotDataOverTime2, quartileChartView1, 'QuartileChartRepresentation')

# trace defaults for the display properties.
plotDataOverTime2Display.AttributeType = 'Row Data'
plotDataOverTime2Display.UseIndexForXAxis = 0
plotDataOverTime2Display.XArrayName = 'Time'
plotDataOverTime2Display.SeriesVisibility = ['alpha.water ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'U (Magnitude) ( block=1)']
plotDataOverTime2Display.SeriesLabel = ['alpha.water ( block=1)', 'alpha.water ( block=1)', 'Normals (0) ( block=1)', 'Normals (0) ( block=1)', 'Normals (1) ( block=1)', 'Normals (1) ( block=1)', 'Normals (2) ( block=1)', 'Normals (2) ( block=1)', 'Normals (Magnitude) ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'Result ( block=1)', 'U (0) ( block=1)', 'U (0) ( block=1)', 'U (1) ( block=1)', 'U (1) ( block=1)', 'U (2) ( block=1)', 'U (2) ( block=1)', 'U (Magnitude) ( block=1)', 'U (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
plotDataOverTime2Display.SeriesColor = ['alpha.water ( block=1)', '0', '0', '0', 'Normals (0) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Normals (1) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Normals (2) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Normals (Magnitude) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'pointDisplacement (0) ( block=1)', '0', '0', '0', 'pointDisplacement (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'pointDisplacement (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'pointDisplacement (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'rAU ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Result ( block=1)', '1', '0.5000076295109483', '0', 'U (0) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U (1) ( block=1)', '0', '0', '0', 'U (2) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U (Magnitude) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'X ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Y ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Z ( block=1)', '1', '0.5000076295109483', '0', 'N ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Time ( block=1)', '0', '0', '0', 'vtkValidPointMask ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotDataOverTime2Display.SeriesOpacity = ['alpha.water ( block=1)', '1.0', 'Normals (0) ( block=1)', '1.0', 'Normals (1) ( block=1)', '1.0', 'Normals (2) ( block=1)', '1.0', 'Normals (Magnitude) ( block=1)', '1.0', 'p ( block=1)', '1.0', 'p_rgh ( block=1)', '1.0', 'pointDisplacement (0) ( block=1)', '1.0', 'pointDisplacement (1) ( block=1)', '1.0', 'pointDisplacement (2) ( block=1)', '1.0', 'pointDisplacement (Magnitude) ( block=1)', '1.0', 'rAU ( block=1)', '1.0', 'Result ( block=1)', '1.0', 'U (0) ( block=1)', '1.0', 'U (1) ( block=1)', '1.0', 'U (2) ( block=1)', '1.0', 'U (Magnitude) ( block=1)', '1.0', 'X ( block=1)', '1.0', 'Y ( block=1)', '1.0', 'Z ( block=1)', '1.0', 'N ( block=1)', '1.0', 'Time ( block=1)', '1.0', 'vtkValidPointMask ( block=1)', '1.0']
plotDataOverTime2Display.SeriesPlotCorner = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime2Display.SeriesLabelPrefix = ''
plotDataOverTime2Display.SeriesLineStyle = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime2Display.SeriesLineThickness = ['alpha.water ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'Result ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime2Display.SeriesMarkerStyle = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime2Display.SeriesMarkerSize = ['alpha.water ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'Result ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# update the view to ensure updated data information
quartileChartView1.Update()

# Properties modified on plotDataOverTime2Display
plotDataOverTime2Display.SeriesOpacity = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime2Display.SeriesPlotCorner = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime2Display.SeriesLineStyle = ['N ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'Result ( block=1)', '1', 'Time ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.water ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime2Display.SeriesLineThickness = ['N ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'Result ( block=1)', '2', 'Time ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.water ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime2Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime2Display.SeriesMarkerSize = ['N ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'Result ( block=1)', '4', 'Time ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.water ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# # update the view to ensure updated data information
quartileChartView1.Update()

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(slice3)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice3.SliceType)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
# quartileChartView1.Update()
# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime3 = PlotDataOverTime(registrationName='PlotDataOverTime3', Input=slice3)

# Create a new 'Quartile Chart View'
quartileChartView2 = CreateView('QuartileChartView')

# show data in view
plotDataOverTime3Display = Show(plotDataOverTime3, quartileChartView2, 'QuartileChartRepresentation')

# trace defaults for the display properties.
plotDataOverTime3Display.AttributeType = 'Row Data'
plotDataOverTime3Display.UseIndexForXAxis = 0
plotDataOverTime3Display.XArrayName = 'Time'
plotDataOverTime3Display.SeriesVisibility = ['alpha.water ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'U (Magnitude) ( block=1)']
plotDataOverTime3Display.SeriesLabel = ['alpha.water ( block=1)', 'alpha.water ( block=1)', 'Normals (0) ( block=1)', 'Normals (0) ( block=1)', 'Normals (1) ( block=1)', 'Normals (1) ( block=1)', 'Normals (2) ( block=1)', 'Normals (2) ( block=1)', 'Normals (Magnitude) ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'Result ( block=1)', 'U (0) ( block=1)', 'U (0) ( block=1)', 'U (1) ( block=1)', 'U (1) ( block=1)', 'U (2) ( block=1)', 'U (2) ( block=1)', 'U (Magnitude) ( block=1)', 'U (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
plotDataOverTime3Display.SeriesColor = ['alpha.water ( block=1)', '0', '0', '0', 'Normals (0) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Normals (1) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Normals (2) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Normals (Magnitude) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'pointDisplacement (0) ( block=1)', '0', '0', '0', 'pointDisplacement (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'pointDisplacement (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'pointDisplacement (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'rAU ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Result ( block=1)', '1', '0.5000076295109483', '0', 'U (0) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U (1) ( block=1)', '0', '0', '0', 'U (2) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U (Magnitude) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'X ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Y ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Z ( block=1)', '1', '0.5000076295109483', '0', 'N ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Time ( block=1)', '0', '0', '0', 'vtkValidPointMask ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotDataOverTime3Display.SeriesOpacity = ['alpha.water ( block=1)', '1.0', 'Normals (0) ( block=1)', '1.0', 'Normals (1) ( block=1)', '1.0', 'Normals (2) ( block=1)', '1.0', 'Normals (Magnitude) ( block=1)', '1.0', 'p ( block=1)', '1.0', 'p_rgh ( block=1)', '1.0', 'pointDisplacement (0) ( block=1)', '1.0', 'pointDisplacement (1) ( block=1)', '1.0', 'pointDisplacement (2) ( block=1)', '1.0', 'pointDisplacement (Magnitude) ( block=1)', '1.0', 'rAU ( block=1)', '1.0', 'Result ( block=1)', '1.0', 'U (0) ( block=1)', '1.0', 'U (1) ( block=1)', '1.0', 'U (2) ( block=1)', '1.0', 'U (Magnitude) ( block=1)', '1.0', 'X ( block=1)', '1.0', 'Y ( block=1)', '1.0', 'Z ( block=1)', '1.0', 'N ( block=1)', '1.0', 'Time ( block=1)', '1.0', 'vtkValidPointMask ( block=1)', '1.0']
plotDataOverTime3Display.SeriesPlotCorner = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime3Display.SeriesLabelPrefix = ''
plotDataOverTime3Display.SeriesLineStyle = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime3Display.SeriesLineThickness = ['alpha.water ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'Result ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime3Display.SeriesMarkerStyle = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime3Display.SeriesMarkerSize = ['alpha.water ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'Result ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=quartileChartView2, layout=layout1, hint=1)

# Properties modified on plotDataOverTime3Display
plotDataOverTime3Display.SeriesOpacity = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime3Display.SeriesPlotCorner = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime3Display.SeriesLineStyle = ['N ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'Result ( block=1)', '1', 'Time ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.water ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime3Display.SeriesLineThickness = ['N ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'Result ( block=1)', '2', 'Time ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.water ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime3Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime3Display.SeriesMarkerSize = ['N ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'Result ( block=1)', '4', 'Time ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.water ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# update the view to ensure updated data information
spreadSheetView1.Update()

# update the view to ensure updated data information
quartileChartView1.Update()

# update the view to ensure updated data information
quartileChartView2.Update()

# set active source
SetActiveSource(slice4)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice4.SliceType)

# update the view to ensure updated data information
quartileChartView2.Update()

# create a new 'Plot Data Over Time'
plotDataOverTime4 = PlotDataOverTime(registrationName='PlotDataOverTime4', Input=slice4)

# show data in view
plotDataOverTime4Display = Show(plotDataOverTime4, quartileChartView2, 'QuartileChartRepresentation')

# trace defaults for the display properties.
plotDataOverTime4Display.AttributeType = 'Row Data'
plotDataOverTime4Display.UseIndexForXAxis = 0
plotDataOverTime4Display.XArrayName = 'Time'
plotDataOverTime4Display.SeriesVisibility = ['alpha.water ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'U (Magnitude) ( block=1)']
plotDataOverTime4Display.SeriesLabel = ['alpha.water ( block=1)', 'alpha.water ( block=1)', 'Normals (0) ( block=1)', 'Normals (0) ( block=1)', 'Normals (1) ( block=1)', 'Normals (1) ( block=1)', 'Normals (2) ( block=1)', 'Normals (2) ( block=1)', 'Normals (Magnitude) ( block=1)', 'Normals (Magnitude) ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (0) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (1) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (2) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'pointDisplacement (Magnitude) ( block=1)', 'rAU ( block=1)', 'rAU ( block=1)', 'Result ( block=1)', 'Result ( block=1)', 'U (0) ( block=1)', 'U (0) ( block=1)', 'U (1) ( block=1)', 'U (1) ( block=1)', 'U (2) ( block=1)', 'U (2) ( block=1)', 'U (Magnitude) ( block=1)', 'U (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
plotDataOverTime4Display.SeriesColor = ['alpha.water ( block=1)', '0', '0', '0', 'Normals (0) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Normals (1) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Normals (2) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Normals (Magnitude) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'pointDisplacement (0) ( block=1)', '0', '0', '0', 'pointDisplacement (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'pointDisplacement (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'pointDisplacement (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'rAU ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Result ( block=1)', '1', '0.5000076295109483', '0', 'U (0) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U (1) ( block=1)', '0', '0', '0', 'U (2) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U (Magnitude) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'X ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Y ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Z ( block=1)', '1', '0.5000076295109483', '0', 'N ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Time ( block=1)', '0', '0', '0', 'vtkValidPointMask ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotDataOverTime4Display.SeriesOpacity = ['alpha.water ( block=1)', '1.0', 'Normals (0) ( block=1)', '1.0', 'Normals (1) ( block=1)', '1.0', 'Normals (2) ( block=1)', '1.0', 'Normals (Magnitude) ( block=1)', '1.0', 'p ( block=1)', '1.0', 'p_rgh ( block=1)', '1.0', 'pointDisplacement (0) ( block=1)', '1.0', 'pointDisplacement (1) ( block=1)', '1.0', 'pointDisplacement (2) ( block=1)', '1.0', 'pointDisplacement (Magnitude) ( block=1)', '1.0', 'rAU ( block=1)', '1.0', 'Result ( block=1)', '1.0', 'U (0) ( block=1)', '1.0', 'U (1) ( block=1)', '1.0', 'U (2) ( block=1)', '1.0', 'U (Magnitude) ( block=1)', '1.0', 'X ( block=1)', '1.0', 'Y ( block=1)', '1.0', 'Z ( block=1)', '1.0', 'N ( block=1)', '1.0', 'Time ( block=1)', '1.0', 'vtkValidPointMask ( block=1)', '1.0']
plotDataOverTime4Display.SeriesPlotCorner = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime4Display.SeriesLabelPrefix = ''
plotDataOverTime4Display.SeriesLineStyle = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime4Display.SeriesLineThickness = ['alpha.water ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'Result ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime4Display.SeriesMarkerStyle = ['alpha.water ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'Result ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime4Display.SeriesMarkerSize = ['alpha.water ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'Result ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# update the view to ensure updated data information
quartileChartView2.Update()

# Properties modified on plotDataOverTime4Display
plotDataOverTime4Display.SeriesOpacity = ['alpha.water ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'Result ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime4Display.SeriesPlotCorner = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime4Display.SeriesLineStyle = ['N ( block=1)', '1', 'Normals (0) ( block=1)', '1', 'Normals (1) ( block=1)', '1', 'Normals (2) ( block=1)', '1', 'Normals (Magnitude) ( block=1)', '1', 'Result ( block=1)', '1', 'Time ( block=1)', '1', 'U (0) ( block=1)', '1', 'U (1) ( block=1)', '1', 'U (2) ( block=1)', '1', 'U (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.water ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'pointDisplacement (0) ( block=1)', '1', 'pointDisplacement (1) ( block=1)', '1', 'pointDisplacement (2) ( block=1)', '1', 'pointDisplacement (Magnitude) ( block=1)', '1', 'rAU ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
plotDataOverTime4Display.SeriesLineThickness = ['N ( block=1)', '2', 'Normals (0) ( block=1)', '2', 'Normals (1) ( block=1)', '2', 'Normals (2) ( block=1)', '2', 'Normals (Magnitude) ( block=1)', '2', 'Result ( block=1)', '2', 'Time ( block=1)', '2', 'U (0) ( block=1)', '2', 'U (1) ( block=1)', '2', 'U (2) ( block=1)', '2', 'U (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.water ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'pointDisplacement (0) ( block=1)', '2', 'pointDisplacement (1) ( block=1)', '2', 'pointDisplacement (2) ( block=1)', '2', 'pointDisplacement (Magnitude) ( block=1)', '2', 'rAU ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
plotDataOverTime4Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'Normals (0) ( block=1)', '0', 'Normals (1) ( block=1)', '0', 'Normals (2) ( block=1)', '0', 'Normals (Magnitude) ( block=1)', '0', 'Result ( block=1)', '0', 'Time ( block=1)', '0', 'U (0) ( block=1)', '0', 'U (1) ( block=1)', '0', 'U (2) ( block=1)', '0', 'U (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.water ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'pointDisplacement (0) ( block=1)', '0', 'pointDisplacement (1) ( block=1)', '0', 'pointDisplacement (2) ( block=1)', '0', 'pointDisplacement (Magnitude) ( block=1)', '0', 'rAU ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
plotDataOverTime4Display.SeriesMarkerSize = ['N ( block=1)', '4', 'Normals (0) ( block=1)', '4', 'Normals (1) ( block=1)', '4', 'Normals (2) ( block=1)', '4', 'Normals (Magnitude) ( block=1)', '4', 'Result ( block=1)', '4', 'Time ( block=1)', '4', 'U (0) ( block=1)', '4', 'U (1) ( block=1)', '4', 'U (2) ( block=1)', '4', 'U (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.water ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'pointDisplacement (0) ( block=1)', '4', 'pointDisplacement (1) ( block=1)', '4', 'pointDisplacement (2) ( block=1)', '4', 'pointDisplacement (Magnitude) ( block=1)', '4', 'rAU ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

# # update the view to ensure updated data information
quartileChartView2.Update()

# set active view
SetActiveView(spreadSheetView1)

# show data in view
plotDataOverTime1Display_1 = Show(plotDataOverTime1, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(os.path.join(script_dir,output_dir,'waveGauge1.csv'), view=spreadSheetView1)

# show data in view
plotDataOverTime1Display_1 = Show(plotDataOverTime2, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(os.path.join(script_dir,output_dir,'waveGauge2.csv'), view=spreadSheetView1)

# show data in view
plotDataOverTime1Display_1 = Show(plotDataOverTime3, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(os.path.join(script_dir,output_dir,'waveGauge3.csv'), view=spreadSheetView1)

# show data in view
plotDataOverTime4Display_1 = Show(plotDataOverTime4, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(os.path.join(script_dir,output_dir,'waveGauge4.csv'), view=spreadSheetView1)

# find view
spreadSheetView1 = FindViewOrCreate('SpreadSheetView1', viewtype='SpreadSheetView')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).