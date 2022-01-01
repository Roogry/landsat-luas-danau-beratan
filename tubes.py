# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import numpy as np
from osgeo import gdal
import rasterio
import wx
from wx.core import Bitmap, NullBitmap
import wx.xrc

###########################################################################
## Class HomeFrame
###########################################################################

class HomeFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GIS Ukur Luas Danau Beratan", pos = wx.DefaultPosition, size = wx.Size( 721,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizerLeft = wx.BoxSizer( wx.VERTICAL )
		
		self.txtTitle = wx.StaticText( self, wx.ID_ANY, u"Geographic Information System", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.txtTitle.Wrap( -1 )
		self.txtTitle.SetFont( wx.Font( 12, 70, 90, 92, False, "Roboto Condensed" ) )
		
		bSizerLeft.Add( self.txtTitle, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.txtSubtitle = wx.StaticText( self, wx.ID_ANY, u"Sistem ini mengukur luas Danau Beratan dari citra Landsat 8 dengan path 116 dan row 66. Citra akan di potong dari titik -8.258128, 115.160672 sampai -8.286073, 115.187365", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
		self.txtSubtitle.Wrap( 380 )
		self.txtSubtitle.SetFont( wx.Font( 8, 70, 90, 91, False, "Roboto Condensed Light" ) )
		
		bSizerLeft.Add( self.txtSubtitle, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"MTL    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		bSizer81.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fileMTL = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Pilih File Metadata MTL", u"*.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		bSizer81.Add( self.fileMTL, 1, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerLeft.Add( bSizer81, 1, wx.EXPAND|wx.TOP, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Band 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fileBand3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Pilih Citra Band 3", u"*.TIF", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		bSizer8.Add( self.fileBand3, 1, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerLeft.Add( bSizer8, 0, wx.EXPAND|wx.TOP, 8 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Band 6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		bSizer9.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fileBand6 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Pilih Citra Band 6", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		bSizer9.Add( self.fileBand6, 1, wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizerLeft.Add( bSizer9, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 8 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Preview Citra " ), wx.HORIZONTAL )
		
		self.sbBand3 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		self.sbBand3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.sbBand3.SetToolTip( u"Preview Citra Band 3" )
		
		sbSizer4.Add( self.sbBand3, 0, wx.ALL, 5 )
		
		self.sbBand6 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		self.sbBand6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.sbBand6.SetToolTip( u"Preview Citra Band 6" )
		
		sbSizer4.Add( self.sbBand6, 0, wx.ALL, 5 )
		
		
		bSizerLeft.Add( sbSizer4, 0, wx.ALL, 5 )
		
		self.btnLuas = wx.Button( self, wx.ID_ANY, u"Kalkulasi Luas", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizerLeft.Add( self.btnLuas, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizerLeft, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10 )
		
		sbSizerRight = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hasil Hitung Luas" ), wx.VERTICAL )
		
		self.sbImageResult = wx.StaticBitmap( sbSizerRight.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 320,300 ), 0 )
		self.sbImageResult.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.sbImageResult.SetToolTip( u"Hasil Pengolahan Citra" )
		
		sbSizerRight.Add( self.sbImageResult, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txtLuas = wx.StaticText( sbSizerRight.GetStaticBox(), wx.ID_ANY, u"Luas Danau : - cm2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtLuas.Wrap( -1 )
		sbSizerRight.Add( self.txtLuas, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnReset = wx.Button( sbSizerRight.GetStaticBox(), wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnReset, 0, wx.ALL, 5 )
		
		
		sbSizerRight.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( sbSizerRight, 0, wx.ALL, 15 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.fileMTL.Bind( wx.EVT_FILEPICKER_CHANGED, self.onChangedMTL )
		self.fileBand3.Bind( wx.EVT_FILEPICKER_CHANGED, self.onChangedBand3 )
		self.fileBand6.Bind( wx.EVT_FILEPICKER_CHANGED, self.onChangedBand6 )
		self.btnLuas.Bind( wx.EVT_BUTTON, self.onClickedLuas )
		self.btnReset.Bind( wx.EVT_BUTTON, self.onClickedReset )
		
		# added variables
		# self.required_cols = 7591
		# self.required_rows = 7731
		self.required_path = 116
		self.required_row = 66
		self.BAND3 = None
		self.BAND6 = None
		self.multBandValue = None
		self.addBandValue = None
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def onChangedMTL( self, event ):
		(self.multBandValue, self.addBandValue) = (None, None)
		if not self.validateMTL(event.GetPath()):
			self.showMessageError("Metadata MTL is not valid! Required Landsat 8 with path " + str(self.required_path) + " and row " + str(self.required_row))
			self.fileMTL.SetPath('')
			return event.Skip()
		
		(self.multBandValue, self.addBandValue) = self.getMultAddMTLValue(event.GetPath())
		self.showMessage("Nilai reflektance mult : " + str(self.multBandValue) + " dan add : " + str(self.addBandValue))

	def onChangedBand3( self, event ):
		self.BAND3 = None
		if not self.validateBand(event.GetPath()):
			self.fileBand3.SetPath('')
			return event.Skip()

		self.BAND3 = rasterio.open(event.GetPath())
		arrBand = self.BAND3.read(1).astype('float64')
		imgBitmap = self.showImage(arrBand, "band3")

		self.sbBand3.SetBitmap(imgBitmap)
		event.Skip()
	
	def onChangedBand6( self, event ):
		self.BAND6 = None
		if not self.validateBand(event.GetPath()):
			self.fileBand6.SetPath('')
			return event.Skip()
		
		self.BAND6 = rasterio.open(event.GetPath())
		arrBand = self.BAND6.read(1).astype('float64')
		imgBitmap = self.showImage(arrBand, "band6")

		self.sbBand6.SetBitmap(imgBitmap)
		event.Skip()
	
	def onClickedLuas( self, event ):
		if not self.validateField():
			return event.Skip()

		arrBand3 = self.BAND3.read(1).astype('float64')
		arrBand6 = self.BAND6.read(1).astype('float64')

		# koreksi Top of Atmosphere
		arrBand3TOA = (self.multBandValue * arrBand3 + self.addBandValue)
		arrBand6TOA = (self.multBandValue * arrBand6 + self.addBandValue)

		arrGSWIR = self.calcGSWIR(arrBand3TOA, arrBand6TOA)
		imgBitmap = self.showImage(arrGSWIR, "gswir", True)
		self.sbImageResult.SetBitmap(imgBitmap)

		# without correction
		# luasDanau = np.count_nonzero(arrGSWIR >= 0.7)

		# with correction
		danauOffset = np.count_nonzero(arrGSWIR >= -0.0055)
		danauInOffset = np.count_nonzero(arrGSWIR >= -0.008)
		luasDanau = danauInOffset - danauOffset

		luas = luasDanau * 900
		self.txtLuas.SetLabel("Luas Danau : " + str(luas) + " m2")
		self.showMessage("Kalkulasi ditekan!")
		
		event.Skip()
	
	def onClickedReset( self, event ):
		self.fileMTL.SetPath('')
		self.fileBand3.SetPath('')
		self.fileBand6.SetPath('')
		self.sbBand3.SetBitmap(NullBitmap)
		self.sbBand6.SetBitmap(NullBitmap)
		self.sbImageResult.SetBitmap(NullBitmap)

		self.txtLuas.SetLabel("Luas Danau : - m2")
		self.showMessage("Hasil telah di reset!")
		event.Skip()

	
	def calcGSWIR(
		self, 
		arrBand3: np.ndarray, 
		arrBand6: np.ndarray
	) -> np.ndarray:
		print()
		print("Calculating with GSWIR..")

		gswirValue = np.where(
			(arrBand3+arrBand6)==0., 0, 
			(arrBand3-arrBand6)/(arrBand3+arrBand6)
		)
		print("Success calculate GSWIR!")
		return gswirValue

	def showImage(self, 
		arrBand: np.ndarray, 
		nameFile: str, 
		isLarge: bool = False
	) -> Bitmap:
		print()
		print("Showing image..")

		if(self.BAND3 != None and self.BAND3 != ""): band = self.BAND3
		else: band = self.BAND6

		imagePath = 'output/' + nameFile
		image = rasterio.open(imagePath +'.tif', 'w', driver='Gtiff', width=band.width,
								  height=band.height, count=1, crs=band.crs, transform=band.transform,
								  dtype='float64')
		image.write(arrBand, 1)
		image.close()
		print("TIF image saved!")

		options_list = [
			'-ot Byte',
			'-of PNG',
			'-scale'
		]
		options_string = " ".join(options_list)
		gdal.Translate(
			imagePath + '.png',
			imagePath + '.tif',
			options=options_string
		)
		print("PNG image saved!")

		print("Importing PNG image...")
		imageBitmap = wx.Bitmap(imagePath + ".png", wx.BITMAP_TYPE_ANY)
		image = wx.Bitmap.ConvertToImage(imageBitmap)
		
		if isLarge: scaledImage = image.Scale(320, 300, wx.IMAGE_QUALITY_HIGH)
		else: scaledImage = image.Scale(150, 150, wx.IMAGE_QUALITY_HIGH)
		
		print("Bitmap image returned!")
		return wx.Bitmap(scaledImage)

	def validateMTL(self, 
		mtlPath: str
	) -> bool:
		print()
		print("Checking metadata MTL file..")
		
		if mtlPath == None or mtlPath == "":
			print("MTL file is empty!")
			return False

		mtl = open(mtlPath, 'r')
		mtlData = mtl.readlines()

		spacecraftFinished = False
		pathFinished = False
		rowFinished = False

		for line in mtlData:
			if spacecraftFinished and pathFinished and rowFinished:
				break
			elif 'SPACECRAFT_ID = ' in line and not spacecraftFinished:
				spacecraft_id = line.split('=')[1][2:11]
				print(spacecraft_id + " metadata is inserted.")
				spacecraftFinished = True
			elif "WRS_PATH = " in line and not pathFinished:
				path = int(line.split('=')[1])
				print("WRS_PATH = ", path)
				pathFinished = True
			elif "WRS_ROW = " in line and not rowFinished:
				row = int(line.split('=')[1])
				print("WRS_ROW = ", row)
				rowFinished = True

		if spacecraft_id != "LANDSAT_8":
			print(spacecraft_id + " metadata is not valid! Required LANDSAT_8 MTL File")
			return False
		
		if path != self.required_path:
			print("metadata with path "+ str(path) +" is not valid! Required metadata with path "+ str(self.required_path))
			return False
		
		if row != self.required_row:
			print("metadata with row "+ str(row) +" is not valid! Required metadata with row "+ str(self.required_row))
			return False
		
		print(spacecraft_id + " metadata is validated!")
		return True

	def getMultAddMTLValue(self,
		mtlPath: str
	) -> bool:
		"""return (multBandValue, addBandValue)"""

		print()
		print("Reading metadata MTL file...")
		
		if mtlPath == None or mtlPath == "":
			print("MTL file is empty!")
			return False

		mtl = open(mtlPath, 'r')
		mtlData = mtl.readlines()

		multFinished = False
		addFinished = False

		for line in mtlData:
			if multFinished and addFinished:
				break
			if "REFLECTANCE_MULT_BAND_3 = " in line and not multFinished:
				multBandValue = float(line.split('=')[1])
				print("REFLECTANCE_MULT_BAND_3 = ", multBandValue)
				multFinished = True
			elif "REFLECTANCE_ADD_BAND_3 = " in line and not addFinished:
				addBandValue = float(line.split('=')[1])
				print("REFLECTANCE_ADD_BAND_3 = ", addBandValue)
				addFinished = True
		
		return (multBandValue, addBandValue)

	def validateBand(self, 
		bandPath: str
	) -> bool:
		print()
		print("validating band file...")
		
		if bandPath == None or bandPath == "":
			print("Band file is empty!")
			self.showMessageError("Band kosong!")
			return False

		bandImage = gdal.Open(bandPath, gdal.GA_ReadOnly)
		
		if bandImage is None: 
			print("Band invalid!")
			self.showMessageError("Citra tidak valid!")
			return False

		# cols = bandImage.RasterXSize
		# rows = bandImage.RasterYSize

		# if (cols != self.required_cols or rows != self.required_rows):
		# 	self.showMessageError("Citra tidak berada pada Bali bagian timur!")
		# 	return False

		print("Band valid!")
		return True

	def validateField(self):
		print()
		print("validating band is not empty...")

		isValid = True
		if ((self.BAND3 == None or self.BAND3 == "") and (self.BAND6 == None or self.BAND6 == "")):
			isValid = False
			print("Band 3 and band 6 is empty")
			self.showMessageError("Band 3 dan Band 6 Belum Dimasukkan!")
		elif (self.BAND3 == None or self.BAND3 == ""):
			isValid = False
			print("Band 3 is empty")
			self.showMessageError("Band 3 Belum Dimasukkan!")
		elif (self.BAND6 == None or self.BAND6 == ""):
			isValid = False
			print("Band 6 is empty")
			self.showMessageError("Band 6 Belum Dimasukkan!")

		if ((self.multBandValue == None or self.multBandValue == "") and 
			(self.addBandValue == None or self.addBandValue == "")):
			isValid = False
			print("Reflectance value is empty")
			self.showMessageError("Nilai reflectance tidak ditemukan!")
		
		if isValid: print("All field is ready to go!")
		else: print("Please input valid data file!")
		
		return isValid

	def showMessage(self, message: str):
		dialog = wx.MessageDialog(None, message, "Info", wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()

	def showMessageError(self, message: str):
		dialog = wx.MessageDialog(None, message, "Error", wx.OK | wx.ICON_ERROR)
		dialog.ShowModal()

