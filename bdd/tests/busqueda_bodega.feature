Feature: Búsqueda por nombre
  Como un adminsitrador del sistema
  Quiero buscar una bodega por nombre
  Con la finalidad de visualizar los resultados

  Scenario: Bodega existente
    Given I login to the system
    And I click Bodegas menu
    And I click Consultar bodegas menu
    When I fill in <search> "Mi Bodeguita"
    Then I can see results in the table of bodegas

  Scenario: Bodega inexistente
    Given I login to the system
    And I click Bodegas menu
    And I click Consultar bodegas menu
    When I fill in <search> "Una bodega que no existe"
    Then I cant see results in the table of bodegas