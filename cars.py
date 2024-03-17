from customtkinter import *


class Container:
    def __init__(self, root):
        # Лічильник натискань на кнопку
        self.clicks = 0
        # Перший фрейм для вибору нової чи бу машини
        self.oldNew = CTkFrame(root, width=220, height=100, border_width=1, border_color='#a85705', fg_color='transparent')
        self.labelFrame = CTkLabel(root, text='Виберіть нова чи бу машина')
        self.labelFrame.place(x=20, y=0)
        self.oldNew.place(x=0, y=13)

        self.Btn1Value = IntVar()
        self.btn1 = CTkRadioButton(self.oldNew, text='Нова машина', variable=self.Btn1Value, value=1, command=self.unlock)
        self.btn1.place(x=5, y=20)
        self.btn2 = CTkRadioButton(self.oldNew, text='Бу машина', variable=self.Btn1Value, value=2, command=self.unlock)
        self.btn2.place(x=5, y=60)

        # Кнопка для показу питань
        self.buttonQuestion = CTkButton(root, text='Показати питання', width=20, fg_color='#a85705',
                                        text_color='white', command=self.frameYear, state='disabled')
        self.buttonQuestion.place(x=300, y=50)

    def frameYear(self):
        self.clicks += 1
        self.animationFrameY = 500
        self.animationLabelY = 500
        if self.clicks <= 1:
            self.frame = CTkFrame(root, width=220, height=130, border_width=1,
                                  border_color='#a85705', fg_color='transparent')
            self.label = CTkLabel(root, text='Виберіть рік випуску авто', fg_color='transparent')
            self.animationFrameLabelY()
            self.var = IntVar()
            self.btnYear1 = CTkRadioButton(self.frame, text='2020 - 2024 рік', variable=self.var, value=1)
            self.btnYear1.place(x=10, y=20)
            self.btnYear2 = CTkRadioButton(self.frame, text='2015 - 2019 рік', variable=self.var, value=2)
            self.btnYear2.place(x=10, y=45)
            self.btnYear3 = CTkRadioButton(self.frame, text='2008 - 2014 рік', variable=self.var, value=3)
            self.btnYear3.place(x=10, y=70)
            self.btnYear4 = CTkRadioButton(self.frame, text='Раніше 2008 року', variable=self.var, value=4)
            self.btnYear4.place(x=10, y=95)
        self.frameBrendsCar()

    def frameBrendsCar(self):
        self.animationFrameX = 0
        self.animationLabelX = 0
        if self.clicks <= 1:
            self.frameBrands = CTkFrame(root, width=220, height=130, border_width=1,
                                      border_color='#a85705', fg_color='transparent')
            self.labelBrands = CTkLabel(root, text='Виберіть марку автомобілю', fg_color='transparent')
            self.varBrands = IntVar()
            self.btnAudi = CTkRadioButton(self.frameBrands, text='Audi', variable=self.varBrands, value=1)
            self.btnAudi.place(x=10, y=20)
            self.btnBmw = CTkRadioButton(self.frameBrands, text='Bmw', variable=self.varBrands, value=2)
            self.btnBmw.place(x=10, y=45)
            self.btnMercedes = CTkRadioButton(self.frameBrands, text='Mercedes', variable=self.varBrands, value=3)
            self.btnMercedes.place(x=10, y=70)
            self.btnPorsche = CTkRadioButton(self.frameBrands, text='Porsche', variable=self.varBrands, value=4)
            self.btnPorsche.place(x=10, y=95)
            self.animationFrameBrandX()
        self.motors()

    def motors(self):
        self.animationFrameMotorY = 500
        self.animationLabelMotorY = 500

        if self.clicks <= 1:
            self.frameMotors = CTkFrame(root, width=220, height=130, border_width=1,
                                      border_color='#a85705', fg_color='transparent')
            self.labelMotors = CTkLabel(root, text='Об\'єм двигуна', fg_color='transparent')

            self.varMotors = IntVar()

            self.btnMotors1 = CTkRadioButton(self.frameMotors, text='Менше 1200', variable=self.varMotors, value=1)
            self.btnMotors1.place(x=10, y=20)

            self.btnMotors2 = CTkRadioButton(self.frameMotors, text='1200 - 1500', variable=self.varMotors, value=2)
            self.btnMotors2.place(x=10, y=45)

            self.btnMotors3 = CTkRadioButton(self.frameMotors, text='1501 - 2200', variable=self.varMotors, value=3)
            self.btnMotors3.place(x=10, y=70)

            self.btnMotors4 = CTkRadioButton(self.frameMotors, text='Більше 2200', variable=self.varMotors, value=4)
            self.btnMotors4.place(x=10, y=95)
            self.animationFrameMotorsY()
        self.contenent()

    def contenent(self):
        self.animationFrameContenentX = 0
        self.animationLabelContenentX = 0
        if self.clicks <= 1:
            self.frameContenent = CTkFrame(root, width=220, height=130, border_width=1,
                                      border_color='#a85705', fg_color='transparent')
            self.labelContenent = CTkLabel(root, text='Континент виробник', fg_color='transparent')

            self.varContenent = IntVar()

            self.btnContenent1 = CTkRadioButton(self.frameContenent, text='Західна Європа', variable=self.varContenent, value=1)
            self.btnContenent1.place(x=10, y=20)

            self.btnContenent2 = CTkRadioButton(self.frameContenent, text='Cхідна Європа', variable=self.varContenent, value=2)
            self.btnContenent2.place(x=10, y=45)

            self.btnContenent3 = CTkRadioButton(self.frameContenent, text='Азія', variable=self.varContenent, value=3)
            self.btnContenent3.place(x=10, y=70)

            self.btnContenent4 = CTkRadioButton(self.frameContenent, text='Америка', variable=self.varContenent, value=4)
            self.btnContenent4.place(x=10, y=95)
            self.animationFrameContenent()

    def animationFrameContenent(self):
        if self.animationFrameContenentX <= 260:
            self.animationFrameContenentX += 10
        if self.animationLabelContenentX <= 280:
            self.animationLabelContenentX += 10
        self.frameContenent.place(x=self.animationFrameContenentX, y=293)
        self.labelContenent.place(x=self.animationLabelContenentX, y=283)
        root.after(10, self.animationFrameContenent)
    def animationFrameBrandX(self):
        if self.animationFrameX <= 260:
            self.animationFrameX += 10
        if self.animationLabelX <= 280:
            self.animationLabelX += 10
        self.frameBrands.place(x=self.animationFrameX, y=150)
        self.labelBrands.place(x=self.animationLabelX, y=138)
        root.after(10, self.animationFrameBrandX)

    def animationFrameLabelY(self):
        if self.animationFrameY >= 150:
            self.animationFrameY -= 9
        if self.animationLabelY >= 144:
            self.animationLabelY -= 9.1
        self.frame.place(x=0, y=self.animationFrameY)
        self.label.place(x=20, y=self.animationLabelY)
        root.after(10, self.animationFrameLabelY)

    def animationFrameMotorsY(self):
        if self.animationFrameMotorY >= 300:
            self.animationFrameMotorY -= 9
        if self.animationLabelMotorY >= 285:
            self.animationLabelMotorY -= 9
        self.frameMotors.place(x=0, y=self.animationFrameMotorY)
        self.labelMotors.place(x=20, y=self.animationLabelMotorY)
        root.after(10, self.animationFrameMotorsY)
    def unlock(self):
        self.buttonQuestion.configure(state='normal')


root = CTk()
root.geometry('500x500')
root.configure(fg_color='#211f1d')
start = Container(root)
root.mainloop()