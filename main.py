import sqlite3
conn = sqlite3.connect("gbf.db")
curs = conn.cursor()
zap1 = """CREATE TABLE IF NOT EXISTS Spravochn_Dann(ФИО TEXT, ученая_степень TEXT, научное_направление TEXT,
место_работы TEXT, кафедра TEXT,  должность TEXT, страна TEXT, город TEXT, адрес TEXT,рабочий_телефон TEXT,
 адреc_электронной_почты TEXT);"""

zap333="""UPDATE Spravochn_Dann SET ФИО='Volkov I.I.' WHERE ФИО='Carl Besson';"""
curs.execute(zap333)
zap333_1="""UPDATE Spravochn_Dann SET ученая_степень='Docent' WHERE ученая_степень='Carl Besson';"""
curs.execute(zap333_1)
zap333_2="""UPDATE Spravochn_Dann SET научное_направление='Radioelectronics' WHERE научное_направление='Radioelectronicss';"""
curs.execute(zap333_2)
zap333_3="""UPDATE Spravochn_Dann SET место_работы='NAN RB' WHERE место_работы=' НАН РБ';"""
curs.execute(zap333_3)
zap333_4="""UPDATE Spravochn_Dann SET кафедра='ETT' WHERE кафедра=' ЭТТ';"""
curs.execute(zap333_4)
zap333_5="""UPDATE Spravochn_Dann SET должность='Docent' WHERE должность=' Docent';"""
curs.execute(zap333_5)
zap333_6="""UPDATE Spravochn_Dann SET страна='RB' WHERE страна='РБ';"""
curs.execute(zap333_6)
zap333_7="""UPDATE Spravochn_Dann SET город='Minsk' WHERE город='Минск';"""
curs.execute(zap333_7)
zap333_8="""UPDATE Spravochn_Dann SET адрес='ul. Surganova' WHERE адрес=' ул. Сурганова';"""
curs.execute(zap333_8)
zap333_9="""UPDATE Spravochn_Dann SET рабочий_телефон='2134' WHERE рабочий_телефон='8346234067';"""
curs.execute(zap333_9)
zap333_10="""UPDATE Spravochn_Dann SET адреc_электронной_почты='@eef' WHERE адреc_электронной_почты='V_doc_dw@uu.uy';"""
curs.execute(zap333_10)
conn.commit()

zap333_2_1="""UPDATE Spravochn_Dann SET ФИО='Danilov I.G.' WHERE ФИО='Volkov I.I.';"""
curs.execute(zap333_2_1)
zap333_2_2="""UPDATE Spravochn_Dann SET ученая_степень='Professor' WHERE ученая_степень='Docent';"""
curs.execute(zap333_2_2)
zap333_2_3="""UPDATE Spravochn_Dann SET научное_направление='biology' WHERE научное_направление='Radioelectronicss';"""
curs.execute(zap333_2_3)
zap333_2_4="""UPDATE Spravochn_Dann SET место_работы='NAN RB' WHERE место_работы=' НАН РБ';"""
curs.execute(zap333_2_4)
zap333_2_5="""UPDATE Spravochn_Dann SET кафедра='ETF' WHERE кафедра='ETK';"""
curs.execute(zap333_2_5)
zap333_2_6="""UPDATE Spravochn_Dann SET должность='Docent' WHERE должность=' Docent';"""
curs.execute(zap333_2_6)
zap333_2_7="""UPDATE Spravochn_Dann SET страна='RB' WHERE страна='РБ';"""
curs.execute(zap333_2_7)
zap333_2_8="""UPDATE Spravochn_Dann SET город='Minsk' WHERE город='Минск';"""
curs.execute(zap333_2_8)
zap333_2_9="""UPDATE Spravochn_Dann SET адрес='ul. Mira' WHERE адрес=' ul. Kazintsa';"""
curs.execute(zap333_2_9)
zap333_2_10="""UPDATE Spravochn_Dann SET рабочий_телефон='234324234335445' WHERE рабочий_телефон='83446734067';"""
curs.execute(zap333_2_10)
zap333_2_11="""UPDATE Spravochn_Dann SET адреc_электронной_почты='@etghtykjhgfdrgtyt' WHERE адреc_электронной_почты='D_doc_dgh@uu.uy';"""
curs.execute(zap333_2_11)
conn.commit()

zap333_3_1="""UPDATE Spravochn_Dann SET ФИО='Sarychev E.V.' WHERE ФИО='Сарычев Е.В.';"""
curs.execute(zap333_3_1)
zap333_3_2="""UPDATE Spravochn_Dann SET ученая_степень='Professor' WHERE ученая_степень='Профессор';"""
curs.execute(zap333_3_2)
zap333_3_3="""UPDATE Spravochn_Dann SET научное_направление='Radiotechnics' WHERE научное_направление='радиотехника';"""
curs.execute(zap333_3_3)
zap333_3_4="""UPDATE Spravochn_Dann SET место_работы='NAN RB' WHERE место_работы=' НАН РБ';"""
curs.execute(zap333_3_4)
zap333_3_5="""UPDATE Spravochn_Dann SET кафедра='ETK' WHERE кафедра='ETF';"""
curs.execute(zap333_3_5)
zap333_3_6="""UPDATE Spravochn_Dann SET должность='Professor' WHERE должность=' Docent';"""
curs.execute(zap333_3_6)
zap333_3_7="""UPDATE Spravochn_Dann SET страна='RB' WHERE страна='РБ';"""
curs.execute(zap333_3_7)
zap333_3_8="""UPDATE Spravochn_Dann SET город='Minsk' WHERE город='Минск';"""
curs.execute(zap333_3_8)
zap333_3_9="""UPDATE Spravochn_Dann SET адрес='ul. Kazintsa' WHERE адрес='ul. Mira';"""
curs.execute(zap333_3_9)
zap333_3_10="""UPDATE Spravochn_Dann SET рабочий_телефон='11111111111' WHERE рабочий_телефон='1435434067';"""
curs.execute(zap333_3_10)
zap333_3_11="""UPDATE Spravochn_Dann SET адреc_электронной_почты='@e1111111' WHERE адреc_электронной_почты='S_doc_erh@uu.uy';"""
curs.execute(zap333_3_11)
conn.commit()

zap444="""DELETE FROM Spravochn_Dann WHERE ФИО='Медведев И.К.';"""
curs.execute(zap444)
zap444_1="""DELETE FROM Spravochn_Dann WHERE ФИО='Абрамов И.С.';"""
curs.execute(zap444_1)
zap444_2="""DELETE FROM Spravochn_Dann WHERE ФИО='Алекссев И.Р.';"""
curs.execute(zap444_2)
conn.commit()
# curs.execute(zap1)
# zap11="""SELECT * FROM Spravochn_Dann;"""
# curs.execute(zap11)
# vib_11=curs.fetchone()
# print(vib_11)

# tuple1=('Волков И.И.','Доцент', 'радиоэлектроника',' НАН РБ',' ЭТТ',' Доцент', 'РБ', 'Минск', ' ул. Сурганова',
#         '8346234067','V_doc_dw@uu.uy')
# zapp1="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1,tuple1)

# tuple1_2=('Данилов И.Г.','Профессор', 'биология',' НАН РБ',' ЭТФ',' Профессор', 'РБ', 'Минск', ' ул. Мира',
#         '83446734067','D_doc_dgh@uu.uy')
# zapp1_2="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1_2,tuple1_2)
#
# tuple1_3=('Сарычев Е.В.','Профессор', 'радиотехника',' НАН РБ',' ЭТК',' Профессор', 'РБ', 'Минск', ' ул. Казинца',
#         '1435434067','S_doc_erh@uu.uy')
# zapp1_3="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1_3,tuple1_3)
#
# tuple1_4=('Медведев И.К.','Доктор наук', 'радиотехника',' НАН РБ',' ЭТБ',' Доктор наук', 'РБ', 'Минск', ' ул. Столетова',
#         '35435434067','М_doc_sfh@uu.uy')
# zapp1_4="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1_4,tuple1_4)
#
# tuple1_5=('Абрамов И.С.','Профессор', 'квантовая механика',' НАН РБ',' ЭТМ',' Профессор ', 'РБ', 'Минск', ' ул. Якуба Коласа',
#         '623577245','А_doc_sfh@uu.uy')
# zapp1_5="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1_5,tuple1_5)
#
# tuple1_6=('Алекссев И.Р.','Доцент', 'квантовая механика',' НАН РБ',' ИТМ',' Доцент ', 'РБ', 'Минск', ' ул. М.Танка',
#         '92357546245','А_doc_sкпh@uu.uy')
# zapp1_6="""INSERT INTO  Spravochn_Dann VALUES(?,?,?,?,?,?,?,?,?,?,?);"""
# curs.execute(zapp1_6,tuple1_6)

zap2= """CREATE TABLE IF NOT EXISTS Conf_INFO(докладчик_или_участник TEXT, дата_рассылки_приглашения TEXT, дата_поступления_заявки TEXT,
 тема_доклада TEXT, отметка_о_поступлении_тезисов TEXT,  дата_приезда TEXT, потребность_в_гостинице TEXT,
  дата_отъезда TEXT);"""
curs.execute(zap2)

zap555="""DELETE FROM Conf_INFO WHERE дата_приезда='10.09.2021';"""
curs.execute(zap555)
zap555_1="""DELETE FROM Conf_INFO WHERE дата_приезда='15.02.2021';"""
curs.execute(zap555_1)
zap555_2="""DELETE FROM Conf_INFO WHERE дата_приезда='18.02.2021';"""
curs.execute(zap555_2)
conn.commit()

# zap22="""SELECT * FROM Conf_INFO;"""
# curs.execute(zap22)
# vib_22=curs.fetchmany(2)
# print(vib_22)

# tuple2=('Докладчик','01.05.2021', '01.04.2021',' Environment',' Присутствует',' 03.05.2021', 'Есть', '05.05.2021')
# zapp2="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2,tuple2)

# tuple2_2=('Участник','10.12.2021', '11.12.2021',' Ocean',' Присутствует',' 06.03.2021', 'Есть', '08.03.2021')
# zapp2_2="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2_2,tuple2_2)
#
# tuple2_3=('Участник','11.11.2021', '11.12.2021',' Time',' Присутствует',' 14.03.2021', 'Есть', '18.03.2021')
# zapp2_3="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2_3,tuple2_3)
#
# tuple2_4=('Докладчик','15.08.2021', '16.11.2021',' Computers',' Присутствует',' 10.09.2021', 'Есть', '08.03.2021')
# zapp2_4="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2_4,tuple2_4)
#
# tuple2_5=('Докладчик','11.02.2021', '16.04.2021',' Animals',' Присутствует',' 15.02.2021', 'Есть', '14.02.2021')
# zapp2_5="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2_5,tuple2_5)
#
# tuple2_6=('Участник','12.02.2021', '26.04.2021',' life',' Присутствует',' 18.02.2021', 'Есть', '22.02.2021')
# zapp2_6="""INSERT INTO Conf_INFO VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp2_6,tuple2_6)

zap3 = """CREATE TABLE IF NOT EXISTS Dop_i(названиe_конференции TEXT, датa_проведения TEXT, местo_проведения TEXT,
организaторы TEXT, спонсоpы TEXT,  количествo_днeй_проведeния_конфeренции TEXT, количествo_участникoв TEXT,
 количествo_докладчикoв TEXT);"""
zap_33="""SELECT * FROM Dop_i WHERE организaторы='IT_SCHOOL';"""

zap666="""DELETE FROM Dop_i WHERE названиe_конференции='FOREST';"""
curs.execute(zap666)
zap666_1="""DELETE FROM Dop_i WHERE названиe_конференции='HOUSE';"""
curs.execute(zap666_1)
zap666_2="""DELETE FROM Dop_i WHERE названиe_конференции='CAR';"""
curs.execute(zap666_2)
conn.commit()

# curs.execute(zap_33)
# vib_33=curs.fetchall()
# print(vib_33)

# curs.execute(zap3)
# tuple3=('IT_START','01.06.2022','Pr-t Nezavisimosti','IT_SCHOOL','Alfa-bank','3','100','200')
# zapp3 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3,tuple3)

# tuple3_2=('SCHOOL_TIME','03.06.2022','Pr-t Nezavisimosti','IT_SCHOOL','Alfa-bank','3','100','200')
# zapp3_2 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3_2,tuple3_2)
#
# tuple3_3=('ENVIRONMEMT','12.06.2022','Pr-t Nezavisimosti','ENVIRONMEMT','GAZ-PROM','120','820','1030')
# zapp3_3 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3_3,tuple3_3)
#
# tuple3_4=('FOREST','12.06.2022','Pr-t Nezavisimosti','FOREST','BMW_COMPANY','12000','2540','11030')
# zapp3_4 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3_4,tuple3_4)
#
# tuple3_5=('HOUSE','11.06.2022','Pr-t Nezavisimosti','FOREST','TINK_BANK','100','820','11030')
# zapp3_5 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3_5,tuple3_5)
#
# tuple3_6=('CAR','30.06.2022','Pr-t Nezavisimosti','CAR','TINK_BANK','100','80','130')
# zapp3_6 = """ INSERT INTO  Dop_i VALUES(?,?,?,?,?,?,?,?);"""
# curs.execute(zapp3_6,tuple3_6)

conn.commit()
curs.close()
conn.close()

