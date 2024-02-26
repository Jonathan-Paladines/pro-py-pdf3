from fpdf import FPDF

from referencias import *

class PDF(FPDF):

    def header(self):
        self.image('img/logo-ulvr-blue.png',
                x = 10, y = 10, w = 30, h = 30)
        
        self.image('img/codigoBarras.jpeg',
                x = 95, y = 70, w = 100, h = 30)

        self.set_font('Arial', '', 12)

        tcol_set(self, 'blue')
        tfont_size(self,14)
        tfont(self,'B')
        self.cell(w = 35, h = 9, txt = '', border = 0,
                align = 'C', fill = 0)
        self.cell(w = 65, h = 9, txt = 'Factura', border = 0,
                align = 'L', fill = 0)
        self.multi_cell(w = 0, h = 9, txt = 'No. 001-002-000001729', border = 0,
                align = 'L', fill = 0)

        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'I')
        self.cell(w = 35, h = 8, txt = '', border = 0,
                align = 'C', fill = 0)
        self.cell(w = 65, h = 8, txt = 'Número de autorización', border = 0,
                align = 'L', fill = 0)
        self.multi_cell(w = 0, h = 8, txt = '0602202401099288649800120010020000017293941061611', border = 0,
                align = 'L', fill = 0)
        self.cell(w = 35, h = 8, txt = '', border = 0,
                align = 'C', fill = 0)
        self.cell(w = 65, h = 8, txt = 'Fecha de autorización', border = 0,
                align = 'L', fill = 0)
        self.multi_cell(w = 0, h = 8, txt = '06/02/2024  15:09:21', border = 0,
                align = 'L', fill = 0)
        self.cell(w = 35, h = 6, txt = '', border = 0,
                align = 'C', fill = 0)
        self.cell(w = 65, h = 6, txt = '', border = 0,
                align = 'L', fill = 0)
        self.multi_cell(w = 0, h = 6, txt = '', border = 0,
                align = 'L', fill = 0)
        
        #_-----------------------------------------
        #información institucional (LINEA 4)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 6, txt = 'Emisor:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 6, txt = 'Universidad Laica Vicente Rocafuerte de Guayaquil', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 6, txt = 'Ambiente:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 6, txt = 'Producción', border = 0,
                align = 'L', fill = 0)

        #_-----------------------------------------
        #información institucional (LINEA 5)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = 'RUC:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = '099097237001', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = 'Emisión:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = 'Normal', border = 0,
                align = 'L', fill = 0) 
        
        #_-----------------------------------------
        #información institucional (LINEA 6)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = 'Dirección:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = 'Ave. de las Américas s/n frente', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = 'Clave de acceso:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = 'Normal', border = 0,
                align = 'L', fill = 0)         

        #_-----------------------------------------
        #información institucional (LINEA 7)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = '', border = 0,
                align = 'C', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = 'al Cuartel Modelo AP 11-33', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)    
        
        
        #_-----------------------------------------
        #información institucional (LINEA 8)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = '', border = 0,
                align = 'C', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = 'Guayaquil, Ecuador', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        #_-----------------------------------------
        #información institucional (LINEA 9)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = 'Correo:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = 'financiero@ulvr.edu.ec', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)            


        #_-----------------------------------------
        #información institucional (LINEA 10)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 25, h = 5, txt = 'Teléfono:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 90, h = 5, txt = '042596500', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)              


        #_-----------------------------------------
        #información institucional (LINEA 11)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 60, h = 5, txt = 'Obligado a llevar', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 55, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)   


        #_-----------------------------------------
        #información institucional (LINEA 12)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 24, h = 5, txt = 'contabilidad:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 55, h = 5, txt = 'Si', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,10)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)   


        #_-----------------------------------------
        #información institucional (LINEA 13)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 60, h = 5, txt = 'Agente de Retención', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 55, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)  

        #_-----------------------------------------
        #información institucional (LINEA 14)
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 30, h = 5, txt = 'Resolución No:', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.cell(w = 85, h = 5, txt = 'NAC-DNCRASC20-00000001', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'B')
        self.cell(w = 35, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)
        
        tfont_size(self,9)
        tcol_set(self, 'black')
        tfont(self,'')
        self.multi_cell(w = 0, h = 5, txt = '', border = 0,
                align = 'L', fill = 0)  
        
        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-12)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
                 border = 0,
                align = 'C', fill = 0)   



lista_datos = (
    (254312, 350.00, 'Pago de cuota # 1', 'N/A', 350.00, 0.00, 350.00),
    (781231, 5.00, 'Especie Valorada, Solicitud notas último semestre', 'N/A', 5.00, 0.00, 5.00),
    (234123, 350.00, 'Pago Cuota # 1', 'Beca 50%', 350.00, 0.50, 175.00),
    (251277, 350.00, 'Pago de cuota # 2', 'Dscto pronto pago', 350.00, 0.10, 315.00),
    )#*8


pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 10) 


# 1er encabezado ----

bcol_set(pdf, 'ulvr2')
tfont_size(pdf,10)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 8, txt = 'Cliente / Usuario', border = 0,
         align = 'C', fill = 1)
tfont(pdf,'')


h_sep = 7
pdf.ln(3)
tfont_size(pdf,8)

# fila 1 --

tcol_set(pdf, 'gray')
pdf.cell(w = 40, h = h_sep, txt = 'Razón Social', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')         
pdf.cell(w = 80, h = h_sep, txt = 'Luis Alfredo Pincay Pilay', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 22, h = h_sep, txt = 'RUC/CI:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black') 
pdf.multi_cell(w = 0, h = h_sep, txt = '0909912312', border = 0,
         align = 'L', fill = 0)


# fila 2 --
tcol_set(pdf, 'gray')
pdf.cell(w = 40, h = h_sep, txt = 'Dirección:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.cell(w = 80, h = h_sep, txt = 'Lomas de urdesa Mz 1203 Villa 04', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 22, h = h_sep, txt = 'Telefono:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.multi_cell(w = 0, h = h_sep, txt = '0995555555', border = 0,
         align = 'L', fill = 0)

# fila 3 --
tcol_set(pdf, 'gray')
pdf.cell(w = 40, h = h_sep, txt = 'Fecha de Emisión:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.cell(w = 80, h = h_sep, txt = '12/02/2024', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 22, h = h_sep, txt = 'Correo:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.multi_cell(w = 0, h = h_sep, txt = 'lpincayl@ulvr.edu.ec', border = 0,
         align = 'L', fill = 0)




pdf.ln(5)
# tabla ----

bcol_set(pdf, 'ulvr2')
tfont_size(pdf,12)
tfont(pdf,'B')
pdf.cell(w = 0, h = 8, txt = 'Detalle Factura', border = 0,ln = 2, align = 'C', fill = 1)
tfont(pdf,'')

tfont_size(pdf,8)
bcol_set(pdf, 'blue')

pdf.cell(w = 15, h = 8, txt = 'Código', border = 0, align = 'C', fill = 1)
pdf.cell(w = 15, h = 8, txt = 'Cantidad', border = 0, align = 'C', fill = 1)
pdf.cell(w = 70, h = 8, txt = 'Descripción', border = 0, align = 'C', fill = 1)
pdf.cell(w = 40, h = 8, txt = 'Detalles Adicionales', border = 0, align = 'C', fill = 1)
pdf.cell(w = 15, h = 8, txt = 'P. Unitario', border = 0, align = 'C', fill = 1)
pdf.cell(w = 15, h = 8, txt = 'Dscto', border = 0, align = 'C', fill = 1)
pdf.multi_cell(w = 0, h = 8, txt = 'Total', border = 0, align = 'C',
             fill = 1)


tfont_size(pdf,9)
dcol_set(pdf, 'blue')
tcol_set(pdf, 'gray')
pdf.rect(x= 10, y= 10, w= 190, h= 128)
c = 0
for datos in lista_datos:

    c+=1
    if(c%2==0):bcol_set(pdf, 'gray2')
    else:bcol_set(pdf, 'white')

    pdf.cell(w = 15, h = 10, txt = str(datos[0]), border = 'TBL', align = 'L', fill = 1)
    pdf.cell(w = 15, h = 10, txt = str(datos[1]), border = 'TB', align = 'L', fill = 1)
    pdf.cell(w = 70, h = 10, txt = str(datos[2]), border = 'TB', align = 'L', fill = 1)
    pdf.cell(w = 40, h = 10, txt = str(datos[3]), border = 'TB', align = 'C', fill = 1)
    pdf.cell(w = 15, h = 10, txt = str(datos[4]), border = 'TB', align = 'C', fill = 1)
    pdf.cell(w = 15, h = 10, txt = str(datos[5]), border = 'TB', align = 'C', fill = 1)
    pdf.multi_cell(w = 0, h = 10, txt = str(datos[6]), border = 'TBR', align = 'C', fill = 1)



#_-----------------------------------------
#Totales de Factura (1)
pdf.ln(5)
#pdf.rect(x= 10, y= 229, w= 190, h= 47)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = 'Información Adicional:', border = 'TL',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Subtotal Sin Impuestos:', border = 'T',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'TR',
        align = 'L', fill = 0)
          

#_-----------------------------------------
#Totales de Factura (2)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = '', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Subtotal 12%:', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)

#_-----------------------------------------
#Totales de Factura (3)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = 'Descripción:', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Subtotal 0%:', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (4)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = '', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Subtotal No Objeto del IVA:', border = 0,
        align = 'L', fill = 0)

        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (5)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = 'Formas de Pago', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Descuentos:', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (6)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = '', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'ICE:', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (7)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = 'Otros con utilización sistema financiero:', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'IVA 12%:', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (8)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = '', border = 'L',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Servicio %::', border = 0,
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'R',
        align = 'L', fill = 0)


#_-----------------------------------------
#Totales de Factura (9)
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 90, h = 5, txt = '', border ='BL',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'B')
pdf.cell(w = 70, h = 5, txt = 'Valor Total:', border = 'B',
        align = 'L', fill = 0)
        
tfont_size(pdf,8)
tcol_set(pdf, 'black')
tfont(pdf,'')
pdf.multi_cell(w = 0, h = 5, txt = '$ 0.00', border = 'BR',
        align = 'L', fill = 0)


#Metadatos

pdf.set_title(title='Hoja metadatos reporte ULVR')
pdf.set_author(author='Jonathan Paladines - JonasDev')
pdf.set_creator('Kodexam')
pdf.set_keywords(keywords='Hoja, PDF, Factura, ULVR')
pdf.set_subject(subject='Detalle de factura ULVR')


pdf.output('sreporte.pdf')
