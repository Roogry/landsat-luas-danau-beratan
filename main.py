from tubes import HomeFrame

import wx
import wx.xrc

class MainApp(wx.App):
    def OnInit(self):
        myframe = HomeFrame(None)
        myframe.Show(True)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()


# Lokasi Danau Bratan
# -8.262105, 115.163603
# -8.284933, 115.187487

# cara nampilin foto
# bitmap = wx.Bitmap(event.GetPath(), wx.BITMAP_TYPE_TIF)
# image = wx.ImageFromBitmap(bitmap)
# image = image.Scale(150, 150, wx.IMAGE_QUALITY_HIGH)
# result = wx.BitmapFromImage(image)

# self.sbBand6.SetBitmap(result)