def exchange_money(budget, exchange_rate):
    return budget * exchange_rate

presupuesto_brasil = 9000
tasa_cambio_brasil = 0.18

monto_convertido_brasil = exchange_money(presupuesto_brasil, tasa_cambio_brasil)
print(f"El monto equivalente en Brasil es: {monto_convertido_brasil} en la moneda local.")

presupuesto_rd = 90000
tasa_cambio_rd = 0.017

monto_convertido_rd = exchange_money(presupuesto_rd, tasa_cambio_rd)
print(f"El monto equivalente en Republica Dominicana es: {monto_convertido_rd} en la moneda local.")

presupuesto_mex = 29500
tasa_cambio_mex = 0.051

monto_convertido_mex = exchange_money(presupuesto_mex, tasa_cambio_mex)
print(f"El monto equivalente en Mexico es: {monto_convertido_mex} en la moneda local.")