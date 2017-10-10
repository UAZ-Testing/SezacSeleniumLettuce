Feature: Eliminar usuario
  Como un administrador del sistema
  Quiero eliminar un usuario
  Para que ya no esté disponible

  Scenario: Eliminación exitosa
    Given I login to the system
    And I click Usuarios menu
    And I click Consultar usuarios menu
    And I fill in <search> "Alfredo"
    When I select the option <Dar de baja> from menu <Opciones>
    Then I can see how the user is now disabled