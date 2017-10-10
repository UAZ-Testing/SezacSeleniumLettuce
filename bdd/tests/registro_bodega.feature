Feature: Create bodega
  As a system administrator
  I want to add a new bodega
  In order that I can use it

  Scenario: Register to bodega 1
    Given I login to the system
    And I click Bodegas menu
    And I click Registrar Bodega menu
    When I fill in Nombre de la Bodega "Mi Bodeguita"
    And I select in Elija un Administrador <Chuck Norris>
    And I fill in Dirección "Av. Gonzáles Ortega #43"
    And I fill in Teléfono "4949428616"
    And I fill in Código Postal "99300"
    And I select in País <México>
    And I fill in Estado "Zacatecas"
    And I fill in Municipio "Jalpa"
    And I click Registrar Bodega button
    Then I can see the new Bodega in the tab <Consultar Bodegas>