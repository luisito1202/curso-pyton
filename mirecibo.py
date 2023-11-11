txt_cliente = input('ingrese el nombre del cliente:')
txt_cedula = input('ingrese la cedula del cliente:')

monto_producto1 = float(input('monto de producto 1:'))
monto_producto2 = float(input('monto de producto 2:'))

subtotal = monto_producto1 + monto_producto2 
iva = 1.16
# aca se calcula el IVA
monto_iva = subtotal*iva 
total = monto_iva + subtotal
print('cliente: ', txt_cliente)
print('cedula del cliente:' ,txt_cedula)
print('monto del producto 1:' ,monto_producto1)
print('monto del producto 2:' ,monto_producto2)
print('subtotal:' ,subtotal)
print('monto del iva:' ,monto_iva)
print('total:' ,total)
print('gracias por su compra')