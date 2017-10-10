# -*- coding: utf-8 -*-
import random

from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

'''
--------------------------------------------------------------------------------
Inicia pruebas login
--------------------------------------------------------------------------------
'''


@step(u'Dado que yo tecleo en el campo usuario "([^"]*)" y \
en el campo password "([^"]*)"')
def dado_que_tecleo_el_usuario_y_el_password(step, usuario, password):
    iniciar_driver()
    login(usuario, password)


@step(u'cuando presiono el botón Ingresar')
def cuando_presiono_el_boton_ingresar(step):
    world.driver.find_element_by_xpath("//button[@type='submit']").click()


@step(u'entonces puedo ver la barra de menú principal del sistema')
def entonces_puedo_ver_la_barra_de_menu_principal_del_sistema(step):
    assert is_element_present(By.XPATH, "//div[@id='wrapper']/nav"), \
        "No se encuentra el elemento"


@step(u'entonces puedo ver mensaje "([^"]*)" y \
vuelve a la pantalla de ingreso')
def entonces_puedo_ver_mensaje_y_vuelve_a_pantalla_de_ingreso(step, mensaje):
    time.sleep(3)
    resultado = world.driver.find_element_by_tag_name("h2")
    assert resultado.text == mensaje, \
        'No coinciden los mensajes ' + resultado.text + " y " + mensaje
    time.sleep(3)
    assert is_element_present(By.ID, "login"), \
        "No se encuentra el elemento"


'''
--------------------------------------------------------------------------------
Inicia pruebas de registro de usuario
--------------------------------------------------------------------------------
'''


@step(u'Given I login to the system')
def given_i_login_to_the_system(step):
    iniciar_driver()
    login('elAdmin', 102030)
    send_login()


@step(u'And I click Usuarios menu')
def and_i_click_usuarios_menu(step):
    world.driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a').click()


@step(u'And I click Registrar submenu')
def and_i_click_registrar_submenu(step):
    world.driver.find_element_by_xpath(
        '//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()


@step(u'When I fill in Nombre de Usuario "([^"]*)"')
def and_i_fill_in_username_group1(step, username):
    txt_nombre_usuario = world.driver.find_element_by_xpath(
        '//*[@id="matricula"]')
    txt_nombre_usuario.send_keys(username + str(random.randint(0, 10000)))


@step(u'And I fill in Nombre Completo "([^"]*)"')
def and_i_fill_in_nombre_completo_group1(step, nombre_completo):
    fill_nombre_completo(nombre_completo)


@step(u'When I fill in Nombre Completo "([^"]*)"')
def when_i_fill_in_nombre_completo_group1(step, nombre_completo):
    fill_nombre_completo(nombre_completo)


@step(u'And I select in Registrar Como Administrador de Sistema')
def and_i_select_in_registrar_como_administrador_de_sistema(step):
    cbox_reg_como = world.driver.find_element_by_xpath('//*[@id="type"]')
    cbox_reg_como.click()
    cbox_option = cbox_reg_como.find_element_by_xpath(
        '//*[@id="type"]/option[1]')
    cbox_option.click()


@step(u'And I fill in Dirección "([^"]*)"')
def and_i_fill_in_direccion_group1(step, direccion):
    txt_direccion = world.driver.find_element_by_xpath('//*[@id="direccion"]')
    txt_direccion.send_keys(direccion)


@step(u'And I fill in Teléfono "([^"]*)"')
def and_i_fill_in_telefono_group1(step, telefono):
    txt_telefono = world.driver.find_element_by_xpath('//*[@id="telefono"]')
    txt_telefono.send_keys(telefono)


@step(u'And I fill in Código Postal "([^"]*)"')
def and_i_fill_in_codigo_postal_group1(step, codigo_postal):
    txt_cod_pos = world.driver.find_element_by_xpath('//*[@id="cp"]')
    txt_cod_pos.send_keys(codigo_postal)


@step(u'And I select in Estado Tlaxcala')
def and_i_select_in_estado_tlaxcala(step):
    cbox_estado = world.driver.find_element_by_xpath('//*[@id="estado"]')
    cbox_estado.click()
    cbox_option = cbox_estado.find_element_by_xpath(
        '//*[@id="estado"]/option[29]')
    cbox_option.click()


@step(u'And I fill in Municipio "([^"]*)"')
def and_i_fill_in_municipio_group1(step, municipio):
    txt_municipio = world.driver.find_element_by_xpath('//*[@id="municipio"]')
    txt_municipio.send_keys(municipio)


@step(u'And I fill in Correo Electrónico "([^"]*)"')
def and_i_fill_in_correo_electronico_group1(step, email):
    txt_email = world.driver.find_element_by_xpath('//*[@id="correo"]')
    txt_email.send_keys(email)


@step(u'And I fill in Password "([^"]*)"')
def and_i_fill_in_password_group1(step, password):
    txt_password = world.driver.find_element_by_xpath('//*[@id="clave"]')
    txt_password.send_keys(password)


@step(u'And I fill in Confirmar Password "([^"]*)"')
def and_i_fill_in_confirmar_password_group1(step, password):
    txt_password = world.driver.find_element_by_xpath('//*[@id="rclave"]')
    txt_password.send_keys(password)


@step(u'And I click Registrar Administrador')
def and_i_click_registrar_administrador(step):
    btn_registrar = world.driver.find_element_by_xpath(
        '//*[@id="addAlumno"]/div/div/div[2]/div/button[1]')
    btn_registrar.click()


@step(
    u'Then I can see the new Administrador in the tab Consulta de Administradores')
def then_i_can_see_the_new_administrador_in_the_tab_consulta_de_administradores(
        step):
    world.driver.implicitly_wait(3)
    header = world.driver.find_elements_by_class_name('page-header')
    assert len(
        header) == 1, 'No encuentra el título de la lista de usuarios (' + str(
        len(header)) + ')'
    title = header[0].get_attribute('innerText')
    assert 'Consulta de Administradores' in title, 'Título no coincide "' + title + '"'


@step(
    u'Then I see the error message This field is required in Nombre de Usuario')
def then_i_see_the_error_message_this_field_is_required_in_nombre_de_usuario(
        step):
    error_label = world.driver.find_element_by_xpath(
        '//*[@id="addAlumno"]/div/div/div[1]/div[1]/label[2]')


'''
--------------------------------------------------------------------------------
Inicia pruebas de registro de bodega
--------------------------------------------------------------------------------
'''


@step(u'And I click Bodegas menu')
def and_i_click_bodegas_menu(step):
    world.driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a').click()


@step(u'And I click Registrar Bodega menu')
def and_i_click_registrar_bodega_menu(step):
    world.driver.find_element_by_xpath(
        '//*[@id="side-menu"]/li[4]/ul/li[1]/a').click()


@step(u'When I fill in Nombre de la Bodega "([^"]*)"')
def when_i_fill_in_nombre_de_la_bodega_group1(step, nombre):
    txt_nombre = world.driver.find_element_by_xpath('//*[@id="nombre"]')
    txt_nombre.send_keys(nombre)
    world.new_bodega = nombre


@step(u'And I select in Elija un Administrador <Chuck Norris>')
def and_i_select_in_elija_un_administrador_chuck_norris(step):
    cbox_administrador = world.driver.find_element_by_xpath(
        '//*[@id="id_admin"]')
    cbox_administrador.click()
    cbox_option = cbox_administrador.find_element_by_xpath(
        '//*[@id="id_admin"]/option')
    cbox_option.click()


@step(u'And I select in País <México>')
def and_i_select_in_pais_mexico(step):
    cbox_paises = world.driver.find_element_by_xpath(
        '//*[@id="pais"]')
    cbox_paises.click()
    cbox_option = cbox_paises.find_element_by_xpath(
        '//*[@id="pais"]/option[1]')
    cbox_option.click()


@step(u'And I fill in Estado "([^"]*)"')
def and_i_fill_in_estado_group1(step, estado):
    txt_estado = world.driver.find_element_by_xpath('//*[@id="estado"]')
    txt_estado.send_keys(estado)


@step(u'And I click Registrar Bodega button')
def and_i_click_registrar_bodega_button(step):
    button_registrar = world.driver.find_element_by_xpath(
        '//*[@id="addBodega"]/div/div/div/button[1]').click()


@step(u'Then I can see the new Bodega in the tab <Consultar Bodegas>')
def then_i_can_see_the_new_bodega_in_the_tab_consultar_bodegas(step):
    assert find_bodega_in_table(
        world.new_bodega), u'No se insertó la bodega' + u'' + world.new_bodega


'''
--------------------------------------------------------------------------------
Inicia pruebas de búsqueda de bodega
--------------------------------------------------------------------------------
'''


@step(u'And I click Consultar bodegas menu')
def and_i_click_consultar_bodegas_menu(step):
    world.driver.find_element_by_xpath(
        '//*[@id="side-menu"]/li[4]/ul/li[2]/a').click()


@step(u'When I fill in <search> "([^"]*)"')
def when_i_fill_in_search_group1(step, nombre):
    search_bodega(nombre)


@step(u'Then I can see results in the table of bodegas')
def then_i_can_see_results_in_the_table_of_bodegas(step):
    assert find_bodega_in_table(world.busqueda_bodega), \
        'No se encuentra la bodega ' + world.busqueda_bodega


@step(u'Then I cant see results in the table of bodegas')
def then_i_can_t_see_results_in_the_table_of_bodegas(step):
    td_item_not_found = world.driver.find_element_by_xpath(
        '//*[@id="dataTables-example"]/tbody/tr/td')
    assert td_item_not_found.text == u'No matching records found', \
        'No se muestra el mensaje de resultados no encontrados'


'''
--------------------------------------------------------------------------------
Inicia pruebas de edición de bodega
--------------------------------------------------------------------------------
'''


@step(u'And I fill in <search> "([^"]*)"')
def and_i_fill_in_search_group1(step, nombre):
    search_bodega(nombre)


@step(u'When I select the Option <Editar> from de menu <Opciones>')
def when_i_select_the_option_editar_from_de_menu_opciones(step):
    tb_body = world.driver.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')
    opts_button = filas[0].find_elements_by_tag_name('button')[0]
    opts_button.click()
    opts_menu = filas[0].find_elements_by_class_name('dropdown-menu')[0]
    edit_opt = opts_menu.find_elements_by_tag_name('a')[0]
    edit_opt.click()


@step(u'And I fill in <Estado> "([^"]*)"')
def and_i_fill_in_estado_group1(step, estado):
    txt_estado = world.driver.find_element_by_xpath('//*[@id="estado"]')
    world.new_estado = estado + str(random.randint(0, 10000))
    value = txt_estado.get_attribute('value')

    for i in range(0, len(value)):
        txt_estado.send_keys(Keys.BACKSPACE)

    txt_estado.send_keys(world.new_estado)


@step(u'And I click <Actualizar Datos> button')
def and_i_click_actualizar_datos_button(step):
    btn_actualizar = world.driver.find_element_by_xpath(
        '//*[@id="addBodega"]/div/div/div/button[1]')
    btn_actualizar.click()


@step(u'Then I can see the new Estado for the bodega')
def then_i_can_see_the_new_estado_for_the_bodega(step):
    select_100_bodega_entries()

    tb_body = world.driver.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')
    bodega_actualizada = False

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')
        if world.new_estado in u'' + celdas[4].text:
            bodega_actualizada = True
            break

    assert bodega_actualizada, 'No se pudo actualizar la bodega'


'''
--------------------------------------------------------------------------------
Helpers
--------------------------------------------------------------------------------
'''


def is_element_present(how, what):
    try:
        world.driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def login(usuario, password):
    world.driver.get(
        "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login")
    world.driver.find_element_by_id("id").clear()
    world.driver.find_element_by_id("id").send_keys(usuario)
    world.driver.find_element_by_id("pass").clear()
    world.driver.find_element_by_id("pass").send_keys(password)


def send_login():
    world.driver.find_element_by_xpath("//button[@type='submit']").click()


def iniciar_driver():
    if not hasattr(world, 'driver'):
        # world.driver = webdriver.Chrome("chromedriver")
        world.driver = webdriver.Firefox()
    else:
        world.driver.get(
            "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login&accion=logout")
    world.driver.implicitly_wait(1)


def finalizar_driver():
    world.driver.get(
        "http://148.217.200.108/application/index.php?mod=usuarios&controlador=login&accion=logout")
    world.driver.quit()


def fill_nombre_completo(nombre_completo):
    txt_nombre_completo = world.driver.find_element_by_xpath(
        '//*[@id="nombre"]')
    txt_nombre_completo.send_keys(nombre_completo)


def select_100_bodega_entries():
    world.driver.find_element_by_xpath(
        '//*[@id="dataTables-example_length"]/label/select').click()
    world.driver.find_element_by_xpath(
        '//*[@id="dataTables-example_length"]/label/select/option[4]').click()


def find_bodega_in_table(nombre_bodega):
    select_100_bodega_entries()

    tb_body = world.driver.find_element_by_tag_name('tbody')
    filas = tb_body.find_elements_by_tag_name('tr')
    bodega_insertada = False

    for fila in filas:
        celdas = fila.find_elements_by_tag_name('td')
        if nombre_bodega in u'' + celdas[0].text:
            bodega_insertada = True
            break

    return bodega_insertada


def search_bodega(nombre):
    txt_search = world.driver.find_element_by_xpath(
        '//*[@id="dataTables-example_filter"]/label/input')
    txt_search.send_keys(nombre)
    world.busqueda_bodega = nombre
