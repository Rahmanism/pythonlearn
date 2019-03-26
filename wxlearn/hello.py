
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        self.textCtrl = wx.TextCtrl(panel, pos=(5, 5,))
        myBtn = wx.Button(panel, label='Press Me', pos=(5, 55))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
