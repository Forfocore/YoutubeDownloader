from xml.dom.pulldom import default_bufsize
from numpy import size
from pytube import YouTube
import wx

class My_Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='VideoDownloader')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.path=''
        self.text1 = wx.StaticText(panel, label="Введите ссылку на видео, которое хотите скачать: ")
        my_sizer.Add(self.text1, 0, wx.ALL | wx.EXPAND, 5)
        self.textEntryURL = wx.TextCtrl(panel)
        my_sizer.Add(self.textEntryURL, 0, wx.ALL | wx.EXPAND, 5)
        self.text2 = wx.StaticText(panel, label="Выберите директорию скачивания: ")
        my_sizer.Add(self.text2, 0, wx.ALL | wx.EXPAND, 5)
        buttonGetPath = wx.Button(panel, label='GetPath')
        buttonGetPath.Bind(wx.EVT_BUTTON, self.GetPath)
        my_sizer.Add(buttonGetPath, 0, wx.ALL | wx.CENTER, 5)
        self.text3 = wx.StaticText(panel, label=f"Директория скачивания: {self.path}")
        my_sizer.Add(self.text3, 0, wx.ALL | wx.EXPAND, 5)
        buttonEnter = wx.Button(panel, label='Download')
        buttonEnter.Bind(wx.EVT_BUTTON, self.YoutubeDownload)
        my_sizer.Add(buttonEnter, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Centre()
        self.Show()

    def YoutubeDownload(self, event):
        url = self.textEntryURL.GetValue()
        path = self.path
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
        

    def GetPath(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if (dialog.ShowModal() == wx.ID_OK):
            dialog.GetPath()
        self.path = dialog.GetPath()
        


if __name__ == '__main__':
    app = wx.App()
    frame = My_Frame()
    app.MainLoop()

