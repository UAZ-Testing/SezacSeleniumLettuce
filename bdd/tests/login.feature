Feature: Acceso al sistema
  Como Administrador del Sistema/Bodega
  quiero acceder al sistema
  para realizar actividades de administrador

  Scenario: Acceso a usuario no válido
  Dado que yo tecleo en el campo usuario "elAdmin" y en el campo password "10203043"
  cuando presiono el botón Ingresar
  entonces puedo ver mensaje "Clave de acceso o contraseña incorrecta" y vuelve a la pantalla de ingreso

  Scenario: Acceso a usuario válido
  Dado que yo tecleo en el campo usuario "elAdmin" y en el campo password "102030"
  cuando presiono el botón Ingresar
