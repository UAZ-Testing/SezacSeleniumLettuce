Feature: Editar bodega
  Como un administrador del sistema
  Quiero editar una bodega
  Con la finalidad de que sus datos sean actualizados

  Scenario: Editar el campo "Estado"
    Given I login to the system
    And I click Bodegas menu
    And I click Consultar bodegas menu
    And I fill in <search> "Mi Bodeguita"
    When I select the Option <Editar> from menu <Opciones>
    And I fill in <Estado> "Sonora"
    And I click <Actualizar Datos> button
    Then I can see the new Estado for the bodega