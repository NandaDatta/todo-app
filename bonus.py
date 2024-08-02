import FreeSimpleGUI as Sg

label1 = Sg.Text("Select files to compress: ")
input1 = Sg.Input()
choose_btn_1 = Sg.FileBrowse("Choose")

label2 = Sg.Text("Select destination folder: ")
input2 = Sg.Input()
choose_btn_2 = Sg.FolderBrowse("Choose")

compress_btn = Sg.Button("Compress")

window = Sg.Window("File Compressor", layout=[[label1, input1, choose_btn_1],
                                              [label2, input2, choose_btn_2],
                                              [compress_btn]])

window.read()
window.close()