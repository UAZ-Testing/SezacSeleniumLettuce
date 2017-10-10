Feature: Create administrator
  As a system administrator
  I want to add a new administrator
  In order that he can access to the system

  Scenario: Register to Juan
    Given I login to the system
    And I click Usuarios menu
    And I click Registrar submenu
    When I fill in Nombre de Usuario "JuanAldamraedreeaaa"
    And I fill in Nombre Completo "Juan Aldama Bañuelos"
    And I select in Registrar Como Administrador de Sistema
    And I fill in Dirección "Av. González Ortega #43"
    And I fill in Teléfono "4949428616"
    And I fill in Código Postal "99300"
    And I select in Estado Tlaxcala
    And I fill in Municipio "Jerez"
    And I fill in Correo Electrónico "porfirioads@gmail.com"
    And I fill in Password "hola1234"
    And I fill in Confirmar Password "hola1234"
    And I click Registrar Administrador
    Then I can see the new Administrador in the tab Consulta de Administradores

  Scenario: Register to Juan failed
    Given I login to the system
    And I click Usuarios menu
    And I click Registrar submenu
    When I fill in Nombre Completo "Juan Aldama Bañuelos"
    And I select in Registrar Como Administrador de Sistema
    And I fill in Dirección "Av. González Ortega #43"
    And I fill in Teléfono "4949428616"
    And I fill in Código Postal "99300"
    And I select in Estado Tlaxcala
    And I fill in Municipio "Jerez"
    And I fill in Correo Electrónico "porfirioads@gmail.com"
    And I fill in Password "hola1234"
    And I fill in Confirmar Password "hola1234"
    And I click Registrar Administrador
    Then I see the error message This field is required in Nombre de Usuario
