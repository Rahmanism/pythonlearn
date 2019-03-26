
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        mySizer = wx.BoxSizer(wx.VERTICAL)

        self.textCtrl = wx.TextCtrl(panel)
        mySizer.Add(self.textCtrl, 0, wx.ALL | wx.EXPAND, 5)

        myBtn = wx.Button(panel, label='Press Me')
        myBtn.Bind(wx.EVT_BUTTON, self.onPress)
        mySizer.Add(myBtn, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.msgTxt = wx.StaticText(panel)
        mySizer.Add(self.msgTxt, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(mySizer)

        self.Show()

    def onPress(self, event):
        value = self.textCtrl.GetValue()
        msg = self.msgTxt.GetLabelText() # .GetValue()
        if not value:
            msg += "You didn't enter anything!\n"
        else:
            msg += f'You typed: {value}\n'
        
        self.msgTxt.SetLabelText(msg) # SetValue(msg)
        self.textCtrl.SetFocus()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
