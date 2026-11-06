program SaldoBancario;
var 
  saldo, montoDeposito, montoRetiro : Real;
  menu : Integer;
  salir : Boolean;
begin 
  saldo := 0;
  salir := false;
  
  while not salir do
  begin
    writeln('--- SELECCIONE OPCION ---');
    writeln('1. Ver Saldo');
    writeln('2. Depositar Saldo');
    writeln('3. Retirar Saldo');
    writeln('4. Salir');
    write('Ingrese su opcion (1-4): ');
    readln(menu);
     
    case menu of 
      1:
      begin
        writeln('Su saldo actual es: $', saldo : 0:2);
      end;
      2:
      begin
        write('Ingrese el monto a Depositar: ');
        readln(montoDeposito);
        if montoDeposito > 0 then
        begin
        saldo := saldo + montoDeposito;
        writeln('Saldo actual: ', saldo : 0:2);
        end
        else 
         write('Ingrese un monto positivo')
      end;
      3:
      begin
        write('Ingrese cuanto quiere retirar: ');
        readln(montoRetiro);
        if montoRetiro > 0 then
        begin
         if saldo >= montoRetiro then
          begin
           saldo := saldo - montoRetiro;
           writeln('Saldo actual: ', saldo : 0:2);
           end
         else 
           writeln('Sin saldo suficiente para retirar');
        end
        else
         write('Ingrese un valor valido para retirar');
      end;
      4:
      begin
        salir := true;
        writeln('Gracias por usar el cajero. Hasta luego');
      end;
    else
      writeln('Ingrese una de las opciones validas (1-4).');
    end;
  end;
end.
