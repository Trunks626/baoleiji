

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from baoleiji import baolei

import threading


class loginTk():

    def chushihua(self):
        # Use a breakpoint in the code line below to debug your script.
        root = tk.Tk()
        root.geometry('500x300+100+100')
        root.title('云匣子登录')
        # 变量接收动态验证码
        pwd = tk.StringVar()
        # 变量接收下拉框选择
        comvalue = tk.StringVar()
        comvalue1 = tk.StringVar()
        tk.Label(root,text='动态验证码',font=24,padx=30,pady=10).grid(row=0, column=1)
        tk.Entry(root,textvariable=pwd,  width=10).grid(row=0,column=2)

        def comboxSelect(*args):
            print(comboxList.get())

        tk.Label(root, text='服务器选择', font=24,padx=30,pady=20).grid(row=1, column=1)
        comboxList = ttk.Combobox(root,textvariable=comvalue)
        comboxList['values'] = ('集团正式','抛账中心')
        comboxList.current(0)
        comboxList.bind('<<ComboboxSelected>>', comboxSelect)
        comboxList.grid(row=1, column=2)

        file = open('account.txt', 'r', encoding='UTF-8')

        acountList = []

        for line in file.readlines():
            curline = line.strip().split(' ')
            acountList.append(curline[:])

        file.close()
        print(acountList)




        def comboxSelect(*args):
            print(comboxList1.get())

        tk.Label(root, text='登录账号', font=24,padx=30,pady=25).grid(row=2, column=1)
        comboxList1 = ttk.Combobox(root,textvariable=comvalue1)
        comboxList1['values'] = acountList
        comboxList1.current(0)
        comboxList1.bind('<<ComboboxSelected>>', comboxSelect)
        comboxList1.grid(row=2, column=2)



        def commit():
            pwdInput = pwd.get()
            comInput = comboxList.get()
            comInput1 = comboxList1.get()

            str = comInput1.split('||')
            print(str)

            if pwdInput == '':
                messagebox.showerror(title='出错了',message='动态验证码不能为空！')
            elif comInput == '':
                messagebox.showerror(title='出错了', message='请选择服务器！')
            elif comInput1 == '':
                messagebox.showerror(title='出错了', message='请选择登录账号！')
            else:
                baolei(pwdInput,comInput,str[0],str[1])




        def thread_it(func):
            t = threading.Thread(target=func)
            t.setDaemon(True)
            t.start()




        b1 = tk.Button(root, text='堡垒机',command=lambda: thread_it(commit)).place(relx=0.3, rely=0.7, anchor=tk.CENTER)

        # b2 = tk.Button(root, text='VPN登录', command=lambda: thread_it(vpnCommit)).place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        b3 = tk.Button(root, text='取消',command=root.destroy).place(relx=0.7, rely=0.7, anchor=tk.CENTER)






        # def on_exit():
        #     messagebox.showwarning(title='提示',message='此路不通')
        #
        # root.protocol('WM_DELETE_WINDOW',on_exit)







        root.mainloop()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sc = loginTk()
    sc.chushihua()
