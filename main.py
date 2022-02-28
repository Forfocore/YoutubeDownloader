from pytube import YouTube
import wx
import os

class My_Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='VideoDownloader')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.textEntryURL = wx.TextCtrl(panel)
        my_sizer.Add(self.textEntryURL, 0, wx.ALL | wx.EXPAND, 5)
        self.textEntryPath = wx.TextCtrl(panel)
        my_sizer.Add(self.textEntryPath, 0, wx.ALL | wx.EXPAND, 5)
        buttonEnter = wx.Button(panel, label='Download')
        buttonEnter.Bind(wx.EVT_BUTTON, self.YoutubeDownload)
        my_sizer.Add(buttonEnter, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def YoutubeDownload(self, event):
        url = self.textEntryURL.GetValue()
        path = self.textEntryPath.GetValue()
        if url:
            print(f'Ваша ссылка: "{url}"')
            if path:
                print(f'Путь сохранения файла - {path}')
                yt = YouTube(url)
                stream = yt.streams.get_by_itag(22)
                stream.download(path)
            else:
                print("Вы не ввели путь сохранения файла.")
        else:
            print("Вы не ввели ссылку на видео.")



if __name__ == '__main__':
    app = wx.App()
    frame = My_Frame()
    app.MainLoop()
