import FreeSimpleGUI as Sg

label1 = Sg.Text("Enter feet: ")
input_1 = Sg.Input()

label2 = Sg.Text("Enter inches: ")
input_2 = Sg.Input()

button = Sg.Button("Convert")

window = Sg.Window("Convertor", layout=[[label1, input_1],
                                        [label2, input_2],
                                        [button]])

window.read()
window.close()
